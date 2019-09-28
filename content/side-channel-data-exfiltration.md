Title: Side Channel Data Exfiltration
Date: 2019-05-10 14:39
Author: jinhaochan
Category: Security
Tags: data exfiltration
Slug: side-channel-data-exfiltration
Status: published

<!-- wp:paragraph -->

A typical data exfiltration attack can be quite easy to spot. By monitoring the usage of common protocols such as HTTP, HTTPS, FTP or even DNS, we can deduce if a data exfiltration is taking place.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Most modern DLP (Data Leak Prevention) solutions today that incorporate network analysis can perform such detection across multiple protocols. In fact, a simple data analysis by SIEMs and a competent analyst can point out anomalies in traffic behavior and protocol usage.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The bad guys are well aware of this, and thus are looking for many innovative ways to exfiltrate data that does not leverage on typical protocols, of even the network at all. I came across a few that I found were extremely interesting:

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Data Transfer over Ultrasonic Frequency

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

<https://github.com/jamesonrader/CUE-Ultrasonic-Transmissions-Protocol>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

On the write up, it has ***"No reliance on a data connection, including Wi-Fi, Bluetooth, or cellular service."***

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

As of now, the advertised usage is targeted at various marketing activities during events at a stadium. One example usage was ***"Triggering commands on the smartphone through a television broadcast, online video, radio commercial, film and movies."***

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

If you can send commands, you can send data. If you can send data, it's data exfiltration.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Data Transfer over Screen Interfaces

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

<https://github.com/pentestpartners/PTP-RAT>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<https://www.pentestpartners.com/security-blog/exfiltration-by-encoding-data-in-pixel-colour-values/>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This package is more straightforward as malicious tool.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

You have a sender (Victim) and a receiver (C2). The victim has his machine compromised, and has established an RDP connection back to the C2. To get the RDP connection in the first place can be done by tunneling through SSH: <https://serverfault.com/questions/200249/how-to-tunnel-windows-remote-desktop-through-ssh-using-a-linux-box>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Once the RDP connection is established, this tool shows that data exfiltration can be performed by encoding data into pixels, which on the receiver end, can read the screen decode them.

<!-- /wp:paragraph -->

<!-- wp:core-embed/youtube {"url":"https://www.youtube.com/watch?time_continue=1\u0026v=hpw8Lz5Fg9I","type":"rich","providerNameSlug":"","className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->

<figure class="wp-block-embed-youtube wp-block-embed is-type-rich wp-embed-aspect-16-9 wp-has-aspect-ratio">
<div class="wp-block-embed__wrapper">

https://www.youtube.com/watch?time\_continue=1&v=hpw8Lz5Fg9I

</div>


<!-- /wp:core-embed/youtube -->

<!-- wp:heading {"level":3} -->

### Data Transfer over Hardware Manipulation

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Perhaps the most interesting of all is hijacking and manipulating the physical machine itself. In the event of an air-gapped machine where no network connection is present, getting data out can be very challenging. (Getting into an air-gapped machine is even more challenging, and can involve really complex scenarios such as supply-chain attacks)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This paper explain how it's possible to control the blinking of LED lights and, using a recording device, capture the blinking sequences to reconstruct data: <https://arxiv.org/abs/1706.01140>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Even more innovative ones take control of the PC fans, and control the RPM to produce sound based data encoding: <https://www.technologyreview.com/s/601816/how-fansmitter-malware-steals-data-from-air-gapped-computers/>

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### End Notes

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The techniques are endless, and as attackers continue to get more innovative, the list will continue to grow. That being said, all these attacks are considerably hard to pull off, and what we as defenders can do is the bare minimum of preventing easy ways of data exfiltration over the network.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Once we raise the difficulty threshold of data exfiltration to a certain level, then should we start worrying about such innovative and out of the box methods. Get the basics right first!

<!-- /wp:paragraph -->
