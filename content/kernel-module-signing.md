Title: Kernel Module Signing
Date: 2018-11-11 22:35
Author: jinhaochan
Category: Security
Tags: Kernel Module
Slug: kernel-module-signing
Status: published

Linux Kernel Signing
====================

Kernel Tainting
---------------

------------------------------------------------------------------------

When dealing with offensive secuirty in the Linux space, we typically concern ourselves with kernel tainting. A kernel taint occurs when an unsigned module is loaded into the Linux kernel, which may potentially be used for malicious purposes.

A kernel taint does not always mean that something bad has happened to your machine, it just means that the machine's state has been unoffically modified. (Think of it as a warrantly for a device such as an Xbox. If you unoffically modify the hardware, its considered tainted, and the warranty is voided).

Some actions that may cause a kernel taint are:

\[code lang=text\]  
- The use of a proprietary (or non-GPL-compatible) kernel module—this is the most common cause of tainted kernels and usually results from loading proprietary NVIDIA or AMD video drivers

- The use of staging drivers, which are part of the kernel source code but are not fully tested

- The use of out-of-tree modules that are not included with the Linux kernel source code

- Forcible loading or unloading of a kernel module (such as forcibly inserting a module not built for the current version of the kernel)

- The use of an SMP (multiprocessor) kernel on certain unsupported uniprocessor CPUs, primarily older AMD Athlon processors

- Overriding of the ACPI DSDT, sometimes needed to correct for power-management bugs (see here for details)

- Certain critical error conditions, such as machine check exceptions and kernel oopses

- Certain serious bugs in the system firmware (BIOS, UEFI) which the kernel must work around

\[/code\]

[Source from Stackoverflow](https://unix.stackexchange.com/questions/118116/what-is-a-tainted-kernel-in-linux)

Each of these actions will produce a certain flag that will be useful for debugging purposes by the vendor or sys admin.

When you insert a module that's unsigned, a message will be logged that says

`%s module verification failed: signature and/or required key missing - tainting kernel`

This can be found in the kernel source code here: [tainted message printing](https://elixir.bootlin.com/linux/latest/source/kernel/module.c#L3691)

In order to not taint the kernel, we must sign the module.

Kernel Module Signing
---------------------

------------------------------------------------------------------------

#### Recap on public-private keys

Before we talk about kernel module signing, lets briefly recap on public-private key encryption

![Public-Private key usage](https://i-technet.sec.s-msft.com/dynimg/IC19080.gif)

[Source from Microsoft](https://technet.microsoft.com/en-us/library/aa998077(v=exchg.65).aspx)

When I want to sign a module, I sign it using my private key. Anyone can use my public key to verify the signature. If another malicious software claims to be my module, the don't have my private key, and using my public key will thus result in a key mismatch.

As opposed to encryption, where I use your public key to lock a message, and only you have your private key to unlock it.

Signing ensures integrity, Encryption ensures confidentiality. (The last one in CIA being availability, but this is assuming the contents are always available)

#### Back to signing kernel modules

If you wanna read deeper, go to this post here: [A History of Linux Kernel Module Signing](http://cs.dartmouth.edu/~bx/blog/2015/10/02/a-history-of-linux-kernel-module-signing.html)

I'll be talking about the main ideas.

A general implementation of module signing is as follows:

1.  Developer builds module
2.  Developer hashes the module or parts of the module and signs the hash using their private key. The signature is embedded together with the module
3.  User retrieves the signed version of the module
4.  User hashes the same parts of the module that the developer hashed and checks that the hash they created matches the hash signed with the developer’s public key

Over the years, different signing mechanism have came (and gone)

#### First version

    - Signature is stored in an ELF section named `“module_sig”`
    - Only the contents of sections whose names contain the string “text” or “data” (but not “.rel.”) are hashed

\[code lang=text\]  
1 for (i = 1; i &lt; hdr-&gt;e\_shnum; i++) {  
2 name = secstrings+sechdrs\[i\].sh\_name;  
3  
4 /\* We only care about sections with "text" or  
5 "data" in their names \*/  
6 if ((strstr(name, "text") == NULL) &&  
7 (strstr(name, "data") == NULL))  
8 continue;  
9 /\* avoid the ".rel.\*" sections too. \*/  
10 if (strstr(name, ".rel.") != NULL)  
11 continue;  
12 /\* add contents of section to signature \*/  
13 ...  
14 }  
\[/code\]

#### Second version

    - Performs a large set of ELF metadata sanity checks before validating the signature
    - Signature itself is stored in a “.module_sig” section just like in first version
    - Code, data section contents are hashed. Corresponding section headers are hashed. Relocation section headers and entries along with any symbols they reference get hashed.

#### Third Version

    - Module signature is wrapped around the notes section `SHT_NOTE`, and named `.module.sig`
    - Everything in Second version + empty and allocatable sections (Second and first version do not hash empty and allocatable sections)

#### Fourth version and beyond

Lets take a deeper look into this version, as its the version thats most widely used for most kernels today.

The source code for kernel version 4.17 can be found here: [4.17 Source code](https://elixir.bootlin.com/linux/v4.17/source/kernel/module.c#L3659)

The function in question is `load_module`, which is called whenever you insmod a module.

In `load_module`, we see that we call `module_sig_check`

\[code lang=text\]  
/\* Allocate and load the module: note that size of section 0 is always  
zero, and we rely on this for optional sections. \*/  
static int load\_module(struct load\_info \*info, const char \_\_user \*uargs,  
int flags)  
{  
struct module \*mod;  
long err;  
char \*after\_dashes;

err = module\_sig\_check(info, flags);  
if (err)  
goto free\_copy;

...  
\[/code\]

Looking at the `module_sig_check` code, it calls `mod_verify_signature`

\[code lang=text\]  
static int module\_sig\_check(struct load\_info \*info, int flags)  
{  
int err = -ENOKEY;  
const unsigned long markerlen = sizeof(MODULE\_SIG\_STRING) - 1;  
const void \*mod = info-&gt;hdr;

/\*  
\* Require flags == 0, as a module with version information  
\* removed is no longer the module that was signed  
\*/  
if (flags == 0 &&  
info-&gt;len &gt; markerlen &&  
memcmp(mod + info-&gt;len - markerlen, MODULE\_SIG\_STRING, markerlen) == 0) {  
/\* We truncate the module to discard the signature \*/  
info-&gt;len -= markerlen;  
err = mod\_verify\_sig(mod, &info-&gt;len);  
}

if (!err) {  
info-&gt;sig\_ok = true;  
return 0;  
}

/\* Not having a signature is only an error if we're strict. \*/  
if (err == -ENOKEY && !sig\_enforce)  
err = 0;

return err;  
}  
\[/code\]

Take note that `mod_verify_sig` has to return `0` for it to call `info-&gt;sig_ok = true`

Finally, we look a code snippet of `mod_verify_sig`

\[code lang=text\]  
struct module\_signature {  
u8 algo; /\* Public-key crypto algorithm \[0\] \*/  
u8 hash; /\* Digest algorithm \[0\] \*/  
u8 id\_type; /\* Key identifier type \[PKEY\_ID\_PKCS7\] \*/  
u8 signer\_len; /\* Length of signer's name \[0\] \*/  
u8 key\_id\_len; /\* Length of key identifier \[0\] \*/  
u8 \_\_pad\[3\];  
\_\_be32 sig\_len; /\* Length of signature data \*/  
};

/\*  
\* Verify the signature on a module.  
\*/  
int mod\_verify\_sig(const void \*mod, unsigned long \*\_modlen)  
{  
struct module\_signature ms;  
size\_t modlen = \*\_modlen, sig\_len;

pr\_devel("==&gt;%s(,%zu)\\n", \_\_func\_\_, modlen);

if (modlen &lt;= sizeof(ms))  
return -EBADMSG;

memcpy(&ms, mod + (modlen - sizeof(ms)), sizeof(ms));  
modlen -= sizeof(ms);

sig\_len = be32\_to\_cpu(ms.sig\_len);  
if (sig\_len &gt;= modlen)  
return -EBADMSG;  
modlen -= sig\_len;  
\*\_modlen = modlen;

...

\[/code\]

We see that at the end of the module, we have two pieces of information:

1.  Module signature struct, which stores information about the module signature
2.  The signature itself

Cracking it
-----------

------------------------------------------------------------------------

I have no idea how to crack it, but if anyone finds a flaw in this and prevents kernel taint, it means that they can insert whatever malicious modules they like without tainting the kernel.

Without a kernel taint, forensics and incident responders would be duped.
