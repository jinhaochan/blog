Title: Kernel Modules in Linux
Date: 2018-10-29 22:31
Author: jinhaochan
Category: Security
Slug: kernel-modules-in-linux
Status: published

The Linux kernel is an open source operating system, as compared to propitiatory ones like Windows, or MacOS.

The entire source code of the Linux kernel can be found here: [Source Code](https://elixir.bootlin.com/linux/latest/source).

TLDR of a Linux kernel is that it's made up of many different modules.

The bare Linux kernel without any modules is amazingly small (Arch Linux, which is notorious for coming with minimal packages installed, has a base size of only 800MB. Compare that to your Windows OS, which requires 20GB)

Linux kernel modules are (relatively) small pieces of code that can be inserted and unloaded from the kernel.

This makes the kernel very configurable and open for customization, because anyone can write a kernel module and insert it into the kernel, giving it new custom functions and commands.

Kernel modules can be loaded by calling `insmod` and removed by calling `rmmod`

Note the distinction between kernel modules and kernel drivers. A kernel driver is a subset of a kernel module, and the driver is a piece of code that talks to some hardware (Sound speaker driver, USB driver etc). A kernel module is a generic description of any code that can be inserted into the kernel.

In this post, I'm going to give a crash course for writing and compiling a kernel module.

There are two components for writing a kernel module:

1.  The C file, which consists of the source code of the kernel module
2.  The Makefile, which specifies a number of parameters when building your module, including; which compiler to use, where to get the libraries from and what kind of object to produce

Lets talk about the C file first

C file
------

Below is a sample code of a C file that compiles to a kernel module

\[code lang=text\]  
// Required  
\#include &lt;linux/init.h&gt;  
\#include &lt;linux/module.h&gt;  
\#include &lt;linux/kernel.h&gt;

// Optional  
MODULE\_LICENSE("GPL");

// Optional  
int myint = 3;  
module\_param(myint, int, 0);  
MODULE\_PARM\_DESC(myint, "Value of my integer");

// Required  
static int \_\_init mymodule\_init(void){  
printk(KERN\_INFO "Init module. Number is %d!\\n", int);  
return 0;  
}

// Required  
static void \_\_exit mymodule\_exit(void){  
printk(KERN\_INFO "Exit module. Number is %d\\n", int);  
}

// Required  
module\_init(mymodule\_init);  
module\_exit(mymodule\_exit);  
\[/code\]

I've put some tags in the code to denote if those are optional or not. Lets go through each of them:

\[code lang=text\]  
// Required  
\#include &lt;linux/init.h&gt;  
\#include &lt;linux/module.h&gt;  
\#include &lt;linux/kernel.h&gt;

//Optional  
\#include &lt;linux/moduleparam.h&gt;  
\[/code\]

These are required for building any kernel module files. For a program as simple as this, these 3 headers are the bare minimum.

`#include` is only included if your module accepts parameters

------------------------------------------------------------------------

\[code lang=text\]  
// Optional  
MODULE\_LICENSE("GPL");  
\[/code\]

If you want to do things the "right" and proper way, this should be required, but you can compile the kernel module without it.

However, there are some kernel functions that require this licensed to be defined, before you can call them. (`kallsyms` is one of them)

------------------------------------------------------------------------

\[code lang=text\]  
// Optional  
int myint = 3;  
module\_param(myint, int, 0);  
MODULE\_PARM\_DESC(myint, "Value of my integer");  
\[/code\]

This code block here is for receiving inputs from the user during `insmod`. If no inputs are specified, the default value becomes 3.

An example would be `insmod  myint=5`, which will then set the value of `myint` to 5

The last value of `module_param(myint, int, 0);` describes the permissions of the file created under `/sys/module/p2/parameters/`

`MODULE_PARM_DESC(myint, "Value of my integer");` just describes the parameter

------------------------------------------------------------------------

\[code lang=text\]  
// Required  
static int \_\_init mymodule\_init(void){  
printk(KERN\_INFO "Init module. Number is %d!\\n", int);  
return 0;  
}

// Required  
static void \_\_exit mymodule\_exit(void){  
printk(KERN\_INFO "Exit module. Number is %d\\n", int);  
}  
\[/code\]

These two code blocks are absolutely required in a kernel module.

`__init` tells the module what to do on `insmod`, and `__exit` tells tells it what to do on `rmmod`

Notice that `__init` returns an integer, while `__exit` returns a void.

The integer returned by `__init` tells us if `insmod` has been successful or not.

From the code inside, when you run `insmod`, you will print a message in `dmesg` that says `"Init module. Number is %d`

And when you `rmmod` the module, it will print `Exit module. Number is %d`

------------------------------------------------------------------------

\[code lang=text\]  
// Required  
module\_init(mymodule\_init);  
module\_exit(mymodule\_exit);  
\[/code\]

Finally, these are required as well.  
It overrides `module_init` and `module_exit` functions with your `mymodule_init` and `mymodule_exit` modules

Makefile
--------

Once you're done with the C program, we can move on to the Makefile.

The make file for this toy program is extreme simple, but once you move on to larger, more complicated kernel modules, your Makefile will similary blow up in size

\[code lang=text\]  
obj-m+=mymodule.o

all:  
make -C /lib/modules/\$(shell uname -r)/build/ M=\$(PWD) modules  
clean:  
make -C /lib/modules/\$(shell uname -r)/build/ M=\$(PWD) clean  
\[/code\]

The whole contents of a make file are very arcane, and you can read up the full list here: [A Simple Makefile Tutorial](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)

I'll just go through things which are essential

\[code lang=text\]  
obj-m+=mymodule.o  
\[/code\]

This tells the make file what object name to output. Take note that the name `mymodule.o` should have exactly the same name as your C file.

------------------------------------------------------------------------

\[code lang=text\]  
all:  
make -C /lib/modules/\$(shell uname -r)/build/ M=\$(PWD) modules  
\[/code\]

This specifies where to get your libraries from when making your project.

The `-C` flag tells it to change directory to the folder containing the libraries. In this case, it is your kernel source code, since it's a kernel module you're building

The `M` variable (not flag) tells the make file where your original source code is, so it can grab the libraries specified in `-C`, and build the files specified in `M=`.

When you type the command `make`, by default, you are calling `make all`

------------------------------------------------------------------------

\[code lang=text\]  
clean:  
make -C /lib/modules/\$(shell uname -r)/build/ M=\$(PWD) clean  
\[/code\]

The clean command cleans up your working directory, by deleting all object files, and intermediate files.

Essentially, this reverts everything back to only having your C source code file.

To invoke the clean command, run `make clean`

That's it
=========

This is an extremely dumbed down, tldr version of how to write a kernel module.

It's way more complex than this, but hopefully it'll serve as a stepping stone to start out!
