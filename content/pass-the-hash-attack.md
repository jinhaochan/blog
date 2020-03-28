Title: Pass The Hash Attack
Date: 2019-01-06 10:45
Author: Chan Jin Hao
Category: Security
Tags: Pass the hash, Windows
Slug: pass-the-hash-attack
Status: published



Passing the Hash attack is a way of logging on to the machine without knowing the actual password of the user. It uses the hash value for authentication, instead of the plain text passwords.





This attack vector is possible in Windows, due to how they store the passwords in their system 



<!-- wp:heading {"level":3} -->

### How Windows stores your passwords in memory





------------------------------------------------------------------------






The Local Security Authority Subsystem Service, LSASS.exe, is a process that runs in memory, and it is responsible for performing tasks such as:





-   Enforcing Security Policies
-   Handling Login Verification
-   Performing Password Changes
-   Generating Access Tokens
-   Writing to Windows Security Log





LSASS.exe is a crucial component for running Windows, and a forceful termination of LSASS.exe will result in the Welcome screen losing its accounts, requiring a restart of the machine.





After a user logs on to the system, a variety of credentials are generated and stored in LSASS.exe, which functions as a Single-Sign-On (SSO). The SSO is to allow quick and automated user authentication for resources. These credentials includes Kerberos Tickets, NTLM Hashes, LM Hashes and clear text passwords.





Because LSASS.exe is running in memory, it should be no surprise that all these credentials and hashes are stored in memory as well. This makes it a valuable target for attackers to steal credentials.



<!-- wp:quote {"className":"is-style-default"} -->

> *If you discover that LSASS.exe is not in C:\\Windows\\System32, or that it is consuming more resources than necessary, that is a cause for concern.*

<!-- /wp:quote -->

<!-- wp:heading {"level":3} -->

### Extracting Password Hash from Memory





------------------------------------------------------------------------






Since the password hashes are all stored in memory, all we have to do is to find techniques to extract the information. There are already many existing ways to do this, the most famous being the tool [Mimikatz](https://github.com/gentilkiwi/mimikatz/wiki) 





One way of doing this is to dump the LSASS.exe process from memory to disk by using tools such as ProcDump (Which is a Microsoft Signed Binary, so it won't trigger any red flags when executed).





After you have dumped the password hashes, there are two attack scenarios that can happen:



<!-- wp:list {"ordered":true} -->

1.  Decrypt the password hashes to obtain the plaintext password
    -   The hashes are encrypted using the Windows API **LsaProtectMemory**.  We can simply decrypt it by calling **LsaUnprotectMemory**.
2.  Don't decrypt the hash, and simply pass it to the authentication mechanism (Pass the Hash Attack)
    -   Inject the hash to LSASS.exe and open session with the injected hash.
    -   Implement part of the NTLM protocol for the authentication with the hash and send commands over the network with protocols like SMB, WMI, etc.



<!-- wp:heading {"level":3} -->

### Detecting a Pass The Hash Attack using Windows Event Log





------------------------------------------------------------------------






You can detect Pass the Hash attack by reviewing your Windows Event Security Log.





A Pass the Hash attack takes places with the NTLM authentication type, and it can be seen in the Event Log with the following features:



<!-- wp:list {"ordered":true} -->

1.  NTLM connection takes place
2.  Event ID 4624 (“*An account was successfully logged on*”)
3.  Logon Type 3 *(“A user or computer logged on to this computer from the network”*)
4.  Authentication Package NTLM (or by logon process name NtLmSsp)





These features are indicative of an NTLM login process, but it does not mean that a Pass the Hash has taken place. Further analysis, such as user behavior, allowed logon techniques and privileges assigned can tell you more.


