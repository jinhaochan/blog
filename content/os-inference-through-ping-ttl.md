Title: OS Inference through Ping TTL
Date: 2019-04-18 14:00
Author: jinhaochan
Category: Security
Slug: os-inference-through-ping-ttl
Status: published

<!-- wp:heading {"level":3} -->

### Terminologies

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:list -->

-   Ping: An command to discover the availability of a target machine. It sends an ICMP Echo Request, and waits for an Echo Reply
-   TTL: Time-To-Live, which tells the network routers how long the packet should live. For each router that passes the packet on, the TTL reduces by 1. Once TTL reaches 0, the packet is discarded, and an ICMP message is sent to the original sender to resend the packet.

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Infering OSes From TTLs

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Each OS has a different TTL for their Echo Reply packet, and based on that, we can infer what OS is sending us the reply.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Lets look at what happens when we ping `google.com`

<!-- /wp:paragraph -->

<!-- wp:image {"id":415} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/04/untitled.png){.wp-image-415}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

The TTL that is show there is the Echo Reply that Google has sent us, and when it has reached our machine, it was "left" with 42 TTL. So how do we find out how long the Echo Reply travelled? `tracert`!

<!-- /wp:paragraph -->

<!-- wp:image {"id":416} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/04/untitled-1.png){.wp-image-416}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

How `tracert` works is that it first sends out a packet with TTL 1 and incrementally bumps up that amount so that at each router, it collect the IP address information about it. When a packet reaches a router with TTL=0, it is sent back to the originating machine, along with it's (the router) IP address.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Request time out happens when the network router has specifically blocked ICMP ping request, so when a packet reaches there with TTL=0, nothing is sent back.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We can see that for traffic that travel from `google.com` to our machine takes 23 hops, and when it reached out machine, it was left with 42 TTL. With that, we can conclude that when it was sent out, it had an initial TTL of `23+42=65`.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We can look at the table below to find out that Linux servers using ICMP protocol has a TTL of 64, which has the closest value to ours.  

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Table of TTLs for each OS

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:table -->

  ---------------- ----------------------- -------------- -----
  Device /\        Version                 Protocol       TTL
  OS                                                      

  AIX              -                       TCP            60

  AIX              -                       UDP            30

  AIX              3.2, 4.1                ICMP           255

  BSDI             BSD/OS 3.1 and 4.0      ICMP           255

  Compa            Tru64 v5.0              ICMP           64

  Cisco            -                       ICMP           254

  DEC\             V5                      TCP and UDP    30
  Pathworks                                               

  Foundry          -                       ICMP           64

  FreeBSD          2.1R                    TCP and UDP    64

  FreeBSD          3.4, 4.0                ICMP           255

  FreeBSD          5                       ICMP           64

  HP-UX            9.0x                    TCP and UDP    30

  HP-UX            10.01                   TCP and UDP    64

  HP-UX            10.2                    ICMP           255

  HP-UX            11                      ICMP           255

  HP-UX            11                      TCP            64

  Irix             5.3                     TCP and UDP    60

  Irix             6.x                     TCP and UDP    60

  Irix             6.5.3, 6.5.8            ICMP           255

  juniper          -                       ICMP           64

  MPE/IX\          -                       ICMP           200
  (HP)                                                    

  Linux            2.0.x kernel            ICMP           64

  Linux            2.2.14 kernel           ICMP           255

  Linux            2.4 kernel              ICMP           255

  Linux            Red Hat 9               ICMP and TCP   64

  MacOS/MacTCP     2.0.x                   TCP and UDP    60

  MacOS/MacTCP     X (10.5.6)              ICMP/TCP/UDP   64

  NetBSD           -                       ICMP           255

  Netgear\         -                       ICMP and UDP   64
  FVG318                                                  

  OpenBSD          2.6 & 2.7               ICMP           255

  OpenVMS          07.01.2002              ICMP           255

  OS/2             TCP/IP 3.0              -              64

  OSF/1            V3.2A                   TCP            60

  OSF/1            V3.2A                   UDP            30

  Solaris          2.5.1, 2.6, 2.7, 2.8    ICMP           255

  Solaris          2.8                     TCP            64

  Stratus          TCP\_OS                 ICMP           255

  Stratus          TCP\_OS (14.2-)         TCP and UDP    30

  Stratus          TCP\_OS (14.3+)         TCP and UDP    64

  Stratus          STCP                    ICMP/TCP/UDP   60

  SunOS            4.1.3/4.1.4             TCP and UDP    60

  SunOS            5.7                     ICMP and TCP   255

  Ultrix           V4.1/V4.2A              TCP            60

  Ultrix           V4.1/V4.2A              UDP            30

  Ultrix           V4.2 – 4.5              ICMP           255

  VMS/Multinet     -                       TCP and UDP    64

  VMS/TCPware      -                       TCP            60

  VMS/TCPware      -                       UDP            64

  VMS/Wollongong   1.1.1.1                 TCP            128

  VMS/Wollongong   1.1.1.1                 UDP            30

  VMS/UCX          -                       TCP and UDP    128

  Windows          for Workgroups          TCP and UDP    32

  Windows          95                      TCP and UDP    32

  Windows          98                      ICMP           32

  Windows          98, 98 SE               ICMP           128

  Windows          98                      TCP            128

  Windows          NT 3.51                 TCP and UDP    32

  Windows          NT 4.0                  TCP and UDP    128

  Windows          NT 4.0 SP5-             -              32

  Windows          NT 4.0 SP6+             -              128

  Windows          NT 4 WRKS SP 3, SP 6a   ICMP           128

  Windows          NT 4 Server SP4         ICMP           128

  Windows          ME                      ICMP           128

  Windows          2000 pro                ICMP/TCP/UDP   128

  Windows          2000 family             ICMP           128

  Windows          Server 2003             -              128

  Windows          XP                      ICMP/TCP/UDP   128

  Windows          Vista                   ICMP/TCP/UDP   128

  Windows          7                       ICMP/TCP/UDP   128

  Windows          Server 2008             ICMP/TCP/UDP   128

  Windows          10                      ICMP/TCP/UDP   128
  ---------------- ----------------------- -------------- -----

<!-- /wp:table -->
