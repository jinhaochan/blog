Title: UEFI and Secure Boot
Date: 2019-04-09 16:12
Author: Chan Jin Hao
Category: Security
Tags: Secure Boot, UEFI
Slug: uefi-and-secure-boot
Status: published



Secure Boot is a verification mechanism to ensure that code launched by the firmware is trusted. It ensures that all system level drivers are signed and trusted.





Before we talk about secure boot and how it works, we need to have some understand of UEFI (Unified Extensible Firmware Interface)



<!-- wp:heading {"level":3} -->

### Overview of BIOS and UEFI





------------------------------------------------------------------------






Both UEFI and BIOS are firmwares, and are programs that run upon booting your system.





UEFI provides faster boot time, more security features (such as Secure Boot), and a more usable graphical interface. Below shows the visual difference between BIOS and UEFI:



<!-- wp:image {"id":398} -->


![placeholder]({attach}media/2019/04/ximg_5913814ed5e9f.png.pagespeed.gpjpjwpjwsjsrjrprwricpmd.ic_.9qc4wyodnr.png){.wp-image-398}  

<figcaption>
Side by side visual comparison of BIOS and UEFI

</figcaption>





The typical sequence for the BIOS when booting up is:



<!-- wp:list {"ordered":true} -->

1.  Perform POST (Power-On Self Test), which checks that the hardware configuration is proper
2.  Look for the MBR (Master Boot Record) on the boot device to launch the boot loader
3.  Boot loader then launches the Operating System





On the other hand, UEFI boots the system by launching EFI's (Extensible Firmware Interfaces) executables, as opposed to running the MBR.



<!-- wp:heading {"level":3} -->

### Drawbacks of BIOS





------------------------------------------------------------------------






Some major drawbacks of BIOS booting are it can only boot from an MBR-partitioned disk, and the MBR-partitioned disk can only support up to 2TB of partitions. What this means is that if you use a disk bigger than 2TB as your boot loader, it will only show that it has 2TB of space.





GPT partitioning can support partitions more than 2TB, but BIOS cannot boot from GPT-partitioned disk, only MBR-partitioned disk





Also, BIOS runs in 16-bit processor mode, and only has 1MB of memory space to execute in. As such due to its limited space, it cannot initialize multiple hardware at once, which leads to a slower boot time.





These drawbacks are solved by UEFI



<!-- wp:heading {"level":3} -->

### UEFI





------------------------------------------------------------------------






One of the biggest change is that the UEFI can run in 32-bit or 64-bit mode, which has way more address space, and is able to boot a lot faster. It also has other features such as



<!-- wp:list {"ordered":true} -->

1.  Being able to boot from a GPT-partitioned disk, hence being able to support disks more than 2TB
2.  Giving a nice GUI
3.  Secure Boot feature (more on this later)
4.  Network boot
5.  Firmware specification





Just like the BIOS which targets the MBR to boot up the OS, UEFI marks one of the GPT-partition with a boot flag, and that partition becomes an EFI partition with its own EFI filesystem in FAT32 format.





The layout of the EFI filesystem is such that every OS has its own directory, which stores all the necessary files for loading the OS



<!-- wp:code -->

``` {.wp-block-code}
/EFI
    /Boot
    /Microsoft
    /Ubuntu
```

<!-- /wp:code -->

<!-- wp:heading {"level":3} -->

### UEFI Legacy Mode  





------------------------------------------------------------------------






Operating Systems that are installed in BIOS mode cannot be booted using UEFI, vice-versa. To boot a BIOS install OS in UEFI mode, you have to reinstall the entire system. To get around this hassle, UEFI supports legacy mode





UEFI Legacy will make the UEFI act just like a BIOS, and this throws away many of the features such as Fast Boot and Secure Boot. UEFI Legacy allows the system to boot from MBR-partitioned disks, and allows booting to be not from EFI partitions.



<!-- wp:heading {"level":3} -->

### Secure Boot





------------------------------------------------------------------------






Advanced malwares target the bootloader as a vector of attack, which launches their malicious process before the OS is launched.





Secure Boot is a feature in UEFI which aims to make the booting process more secure by disallowing unsigned code to run in the pre-boot phase. Secure Boot only allows signed bootloaders and drivers that are trusted by the Original Equipment Manufacturer (OEM) to run.





When the PC first runs, it checks the signature of each piece of booting software. If the signatures are valid, then the firmware passes control to the OS.





The OEMs creates Secure Boot keys and store them on the firmware, which are used for the verification process of Secure Boot.





Secure Boot is also customizable, and you can control which signing certificates are present for checking. You can install or remove certificates that Secure Boot uses for checking. For example, if an organization uses Linux, they can remove all of Microsoft's certificates, and install their own organization's certificate in place. Secure Boot then uses those certificates for verification.





This customization is also available to any individual user, where you can sign your own bootloader and device drivers.



<!-- wp:heading {"level":3} -->

### Secure Boot and Linux





------------------------------------------------------------------------






The whole concept of Secure Boot was built around Microsoft systems, and Linux distros were not made in mind for this. As such, there were a few hurdles to overcome when applying Secure Boot to Linux distros.





The first money grabbing move by Microsoft was to let Linux distros pay a one-time fee of \$99 on Microsoft Sysdev Portal to apply for their bootloaders to be signed and recognized by Secure Boot. This way, these Linux distros work with Secure Boot out-of-the-box in the machines.





In Linux, it's common for developers to develop their own third party modules, which are all unsigned, and will be rejected by the system when trying to `insmod` them. Linux therefore provides a way to sign their custom binaries or modules using the command `sbsign` and `kmodsign` respectively.






