Title: How to harden a Linux Kernel
Date: 2019-04-17 11:21
Author: Chan Jin Hao
Category: Security
Tags: ASLR, SMAP, SMEP
Slug: how-to-harden-a-linux-kernel
Status: published



Hardening means to make the something more secure and resilient to attacks. When people talk about hardening, they usually talk about server hardening, which includes things like





-   IP / MAC address white listing
-   Closing unused ports
-   Uninstalling unused systems
-   Disabling `root` login (no one can login as root, only a normal user who can `sudo`)





These are legitimate areas of hardening, but another area of hardening involves securing the kernel itself at compile time. This deals with much lower level of security such as Address Space Layout Randomization (ASLR) or Read/Write permissions at different memory regions (SMEP/SMAP). In this post, I'll be writing about these 2 technologies.



<!-- wp:heading {"level":3} -->

### Kernel Level Hardening





------------------------------------------------------------------------




<!-- wp:heading {"level":4} -->

#### Kernel Address Space Layout Randomization (KASLR)





ASLR is a memory protection technique that randomizes the address layout of the executables that are loaded in memory. How this prevent an attack is to disallow memory space predictability.





An attacker, if he knows your target OS (example Ubuntu 14.04), he can spin up the exact same OS in his testing environment. If there is no ASLR, the executables such as `glibc` will be loaded in the same address space every time, allowing him to make an exploit targeting predictable addresses.





With ASLR, the executable will always be in a different address space, and it will cause the kernel to crash (Memory access violation) if an exploit runs.





ASLR can be configured at `/proc/sys/kernel/randomize_va_space` with the following values:





-   0 - No Randomization: All addresses are static
-   1 - Conserved Randomization:
    -   Stack ASLR: Each execution of a program results in different stack memory layout
    -   LIBS/MMAP ASLR: Each execution of a program results in different `mmap` memory space layout
    -   EXEC ASLR: Each program that was complied with `-fPIE -pie`, which stands for Position Independent Executables, will get loaded into different memory locations
-   2 - Full Randomization: `brk` ASLR
    -   All of the above, including `brk` ASLR
    -   Previously, `brk` memory areas were always allocated after the EXEC memory area
    -   `brk` ASLR randomizes the `brk` memory area relative to the EXEC memory area





Possible Exploits: One of the weakness of ASLR is that even though the libraries and executables are randomly located within the memory space, within the library, the functions are still at a fixed offset. This means that if the attack want to leverage on a `glibc` function, all he has to do is find the starting point of `glibc`, and the function will always be at the same offset



<!-- wp:heading {"level":4} -->

#### SMEP/SMAP  





Supervisor Mode Execution Protection (SMEP) and Supervisor Mode Access Prevention (SMAP) are techniques to prevent unauthorized memory access.





SMAP prevents supervisor mode from accessing (rw) user-space memory space.





SMEP prevents user mode from executing (x) in kernel memory space





SMAP is important because while you're in kernel space, you have full privileges to perform any actions. If we allow this privilege to "escape" and return to user-space memory, he can perform even more unauthorized actions and get user data.





SMEP is important for similar reasons, where the user cannot execute in kernel space to perform unprivileged actions affecting the kernel.





Possible Exploits: Linux kernel has a function `native_write_cr4` which can overwrite bits in the CR4 control register. One of the bit controls if SMEP/SMAP is on or off. If the attack can call the function to overwrite the bits in the control register, he can turn of SMEP/SMAP





  


