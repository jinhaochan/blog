Title: inotify on Shared Servers
Date: 2019-10-04 16:51
Author: Chan Jin Hao
Category: Software Engineering
Slug: inotify-shared-server
Status: published

We all have faced an issue at one point in our engineering adventures that we need to create a form of watchdog. We have to watch for a certain activity on a certain file or folder, before we perform a set of actions.

Thankfully in Linux, there is a function called `inotify`, which allows you to monitor the Linux filesystem for any specific events.

There's also a python package for it, but please DON'T USE `PYINOTIFY`. USE THE VANILLA `INOTIFY`. `PYINOTIFY` is defunct, inefficient, and is no longer supported.

`pip install inotify` will do.

### inotify

---

`inotify` is an system call in the Linux kernel that allows processes to register themselves to be notified when events have occured to a specified filesystem.

This is opposed to a user land implementation, which typically, and very inefficiently does a `while True` to check for any changes. A typical setup would be to run a process that writes a flag file to the folder when it has completed, and start a `while` loop to see if a flag file is present in that folder.

`inotify` can watch for several events such as: `open`, `close`, `read`, `write`, `delete`, `move`, or any other action that can be taken on a filesystem.

More importantly, it can know when a file finishes writing by looking out for the event `IN_CLOSE_WRITE`. I would think this scenario is pretty common, as we would need to wait until a file is fully written before performing any action. If we do the naive approach of just looking if the file exists, we could process the file before it has finished writing, causing major errors.

I won't go through the entire details of how `inotify` is implemented, you can read it here: [inotify implementation](https://www.linuxjournal.com/article/8478)

But basically, instead of constantly polling for changes which induces huge CPU cycles, inotify does a block and waits for notification events. Cool!

### Implementing inotify on shared servers

---

Say now you have 2 virtual machines, Machine A does the file processing, and Machine B queries the internet for enrichment information. What we want is for Machine A to pass the file over to Machine B, Machine B to do the enrichment, and pass the enriched file back to Machine A.

Because inotify is a kernel function, it needs the file pointer of the folder it's watching.

The image below shows the setup that can make it work.

![placeholder]({attach}media/images/inotify.png)

Machine A mounts the folder called Unenriched, that is physically on Machine B.

Machine B mounts the folder called Enriched, that is physically on Machine A.

Machine B runs `inotify` to monitor the Unenriched folder, and takes in any unenriched files that is passed over from Machine A.

Machine A runs `inotify` to monitor the Enriched folder, and takes in any enriched files that is passed from Machine B.

And because `inotify` is done in a block-wait manner, the program flow on Machine A simply pauses and waits for the `IN_CLOSE_WRITE` event on the Enriched folder.

This is a simple post to show you how you can implement a watchdog with `inotify`, and how to set it up on shared folders. Hope it helps!
