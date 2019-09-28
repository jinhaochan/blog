Title: Looking out for C2 Traffic
Date: 2019-05-02 16:14
Author: jinhaochan
Category: Security
Tags: C2, Command and Control
Slug: looking-out-for-c2-traffic
Status: published

<!-- wp:heading -->

Types of C2 Communication
-------------------------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

When a host gets infected with a malware, sometimes it will attempt to call back to it's Command and Control (C2) to get, or send information. There are 4 types of C2 communication traffic

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Beacon
    -   After a host has been compromised, the malware will send a message heartbeat to the C2 to inform them of it's status. This traffic is just to tell the C2 that it's alive.
2.  Command
    -   The command is sent from the C2 to the malware residing on the compromised host. It can either be real-time, or non-real-time. Non-real-time commands means that the command is stored and queued somewhere which the malware can retrieve to execute.
3.  Exfiltration
    -   This command is sent from the compromised host to the C2. Exfiltration means sending a payload, and this payload can either be a reply from the malware, or stolen data from the host or network. Exfiltration can be done either immediately on request, or at regular (or deliberately irregular) intervals
4.  Connectivity Check
    -   This check is done by the malware to check if it has internet connectivity out. This connection may not talk directly to the C2, but may try to connect to something as benign as Google. If it doesn't have any internet connection, it can either defer talking to the C2, or remove itself entirely from the system.

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Capturing C2 traffic

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

There are some strategies to capture C2 traffic, such as leveraging on CTI to learn about IOCs, patterns and log entries that may indicate a compromise.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Because C2 traffic is a networking phenomenon, most approaches towards network analysis, such as:

<!-- /wp:paragraph -->

<!-- wp:list -->

-   Netflow Analysis for inflow and outflow
-   IRC and P2P traffic
-   DNS query logs (to look out for DNS tunneling or DGA)
-   Unusual port numbers and services
-   Unusual timing of connections
-   Requests to Social Media at unusual hours
-   Packet size

<!-- /wp:list -->

<!-- wp:paragraph -->

Below shows an image of the packet sizes versus time, and we can see the start difference between a normal Google search and a Malware

<!-- /wp:paragraph -->

<!-- wp:image {"id":435,"align":"center"} -->

>


![placeholder]({attach}media/2019/05/eta-blake-fig-2.png){.wp-image-435}




<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### Machine Learning to capture C2 traffic

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Machine learning techniques can be employed to detect C2 traffic. In an extremely noisy environment like network traffic, ML perform anomaly detection by sieving out traffic that stands out.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I did a small sample project which can be seen here:<https://github.com/jinhaochan/BotnetDetection>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The model trained took features only from network behavior, and had quite a good performance. Although I must say that more advanced malwares these days come up with creative techniques, and in this case, machine learning might fail to detect them due to the lack to training data. Furthermore, the malware can cleverly disguise themselves to look like normal traffic, and the model we train miss those entries

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Analyzing C2 traffic

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Assuming that you know a malware has infected a host and is talking to a C2 server, you can either setup a honeypot, or try to reverse engineer the malware sample on the host.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Setting up the honeypot is essentially performing an MITM between the malware and the C2 server. We allow the malware to connect to the C2 and internet, while isolating it from other machines on the network to prevent it from spreading. This way, we can capture all the traffic that's flowing to and from the C2, and we can find out what the motive of the malware is.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The second method is getting the sample of the malware on the infected host, and perform reverse engineering to find out what functions and capabilities it has.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### MITRE ATT&CK TTP for C2

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

There is a branch Tactics in the MITRE ATT&CK Framework dedicated to C2, and there is a collection of Techniques they use to identify C2 communication.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

If you are coming up with a system or model to detect C2 traffic, the matrix can be highly beneficial. But take caution to not fit a round peg into a square hole, the list is not comprehensive. Attackers are aware of MITRE and their TTPs, and will actively build ways around them.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Software to use for detection C2

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Bro (now renamed to Zeek) <https://www.zeek.org/>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

There are many write ups out there on how to use Zeek to capture and analyze traffic. Zeek is not specific to capturing just C2, but a wide array of network activities

<!-- /wp:paragraph -->
