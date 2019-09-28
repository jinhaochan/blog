Title: Process Injection
Date: 2019-04-05 14:44
Author: jinhaochan
Category: Hacking, Security
Tags: Process Injection
Slug: process-injection
Status: published

<!-- wp:paragraph -->

I decided to revisit some fundamental security concepts again, and one of which I used in my previous employment was Process Injection.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Process Injection is a technique of running your own code within the address space of another process. The hard part is getting your code in that address space, but there are numerous ways to achieve this

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### DLL Injection  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The malware write the address pointing to its own DLL into the virtual address space of another process. The DLL is then executed by creating a remote thread within the process.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The steps performed to achieve this are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Finding a process to hijack using `Process32First` and `Process32Next`
2.  Getting a handle of the target process with `OpenProcess`
3.  Allocating memory and writing the path to malicious DLL using `VirtualAllocEx` and `WriteProcessMemory`
4.  Code execution in the process by calling `CreateRemoteThread`, `NtCreateThreadEx` or `RtlCreateUserThread`

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### PE Injection

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Instead of passing the address of the DLL, the malware can directly copy malicious the code into the process. The code is then executed via `CreateRemoteThread`

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The steps performed to achieve this are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Finding a process to hijack using `Process32First` and `Process32Next`
2.  Getting a handle of the target process with `OpenProcess`
3.  Allocating memory and writing the malicious code using `VirtualAllocEx` and `WriteProcessMemory`
4.  Code execution in the process by calling `CreateRemoteThread`, `NtCreateThreadEx` or `RtlCreateUserThread`

<!-- /wp:list -->

<!-- wp:paragraph -->

The difference here is in step 3, where the code is copied, instead of the reference to the code. This method does not require dropping a DLL onto the machine.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Process Hollowing

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Instead of injecting the address of the DLL, or copying the malicious code into the target process, malware can also overwrite the original code in the memory space of the process. This is called Process Hollowing.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The steps performed to achieve this are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Create a new process in suspended mode to host the malicious code
2.  Done by calling `CreateProcess` with the flag `CREATE_SUSPEND`
3.  Unmap memory of target process by calling `ZwUnmapViewOfSection` or `NtUnmapViewOfSection`
4.  Allocate new memory for malware using `VirtualAllocEx` and write the code using `WriteProcessMemory`
5.  Point the entry point of the suspended process to the code in the target process using `SetThreadContext`
6.  Resume suspended process by calling `ResumeThread` which executes the code in the target process

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Thread Execution Hijacking (Suspend, Inject, Resume)

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Instead of creating a new process that is suspended like Process Hollowing, Thread Execution Hijacking avoids creating a new process.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The steps performed to achieve this are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Get a handle to the target process
2.  Suspend the target process by calling `SuspendThread`
3.  Write malicious code in the target process by calling `VirtualAllocEx` and `WriteProcessMemory`
4.  Resume the running of the process by calling `ResumeThread`

<!-- /wp:list -->

<!-- wp:paragraph -->

SIR are problematic because suspending a process mid-execution may cause the system to crash.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Hook Injection via `SetWindowsHookEx`  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Hooking is a technique to intercept function calls, and load their malicious DLL upon a certain event getting triggered within a specific thread.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

`SetWindowsHookEx` is called to install a hook routine into the hook chain. One of the arguments that `SetWindowsHookEx` takes is a `threadID` with which this hook procedure is associated with. If this value is set to `0`, all threads within the process perform the action when the event is triggered. To generate less noise, 1 thread is usually targeted.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Once the DLL is injected, the malware executes the malicious code on behalf of the process of the `threadID` that was passed into the `SetWindowsHookEx` function.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Injection and Persistence via Registry Modification  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Malwares can insert their malicious libraries under `Appinit_Dlls` to have other processes load their libraries. Every library under this registry key is loaded into any process that calls `User32.dll`.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Malwares can also put their libraries under `AppCertDlls`, which affects any process that calls Win32 API functions such as `CreateProcess`, `CreateProcessAsUser` and `WinExec`  

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Image File Execution Options (IFEO) is usually used for debugging purposes. The `Debugger Value` under this registry key can be set to attach a program to another executable for debugging, and whenever that executable is launched, the attached program is also launched. Malwares can make use of this to attach themselves to a target executable.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Asynchronous Procedure Calls (APC)

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Malwares can leverage on APC to force another thread to execute their malicious code by intercepting the APC queue of the target thread.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Each thread has a queue of APC which are waiting for execution upon the thread entering an alterable state.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The steps performed to achieve this are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Finding a thread that is in an alterable state
2.  Call `OpenThread` and `QueueUserAPC` to queue an APC to the thread
3.  `QueueUserAPC` takes in 3 arguments
    -   Handle to a target thread
    -   Pointer to the function that the malware wants to run
    -   Parameters to the function

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Injection using Shims

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Shims are provided by Microsoft to provide backward compatibility by allowing developers to apply fixes to their program without rewriting code. Malwares can leverage on Shims to target an executable for persistence and injection.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

When Windows runs the Shim engine, it loads a binary to check shimming databases to check for appropriate fixes. Malwares can create and install their own shimming database (sdb). They can do so by calling `sdbinst.exe` (shim database installer), and install their own malicious sdb file.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Import Address Table (IAT) and Inline Hooking

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

IAT hooking involves modifying the Import Address Table to redirect the address of the functions there to their own malicious functions.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Inline hooking modified the API function itself, by rewriting the first few bytes of code in the function to jump to their malicious function.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

In the past, I've only worked in the Linux space when doing process injection. One of the techniques I used was modifying the IAT, and here I've learnt a lot more other techniques that are related to the Windows OS.

<!-- /wp:paragraph -->
