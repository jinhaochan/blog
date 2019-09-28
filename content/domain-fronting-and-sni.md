Title: Domain Fronting and SNI
Date: 2019-06-13 10:54
Author: jinhaochan
Category: Security
Tags: Domain Fronting, SNI
Slug: domain-fronting-and-sni
Status: published

<!-- wp:paragraph -->

Domain fronting is a malicious act of appearing to request to visit a legitimate site (the front), while in actual fact, the request is going to another website.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Domain fronting relies on the SSL technology to work, where the service provider is unable to see the actual malicious hostname the request is going to, but can only see fronted domain the SNI data.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### SNI

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

SNI, which stands for Server Name Indication, helps solves the issue introduced with TLS on HTTP connections.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A server can be shared by many users to host their own websites. For example: AWS, Google Cloud or Azure all host multiple websites that clients can visit.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In a non-TLS connection, when the request is made from the client to the server, the hostname is visible in clear text. The server then simply serves the requested hostname to the client.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In a TLS connection, it gets slightly complicated. A TLS connection requires the certificate of the website to complete the handshake. Each website hosted on the server has their own certificate. However, the hostname is encrypted in the incoming request from the client. Without the hostname, how will the server know which website the client wants to visit, and which certificate to present to the client?

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A simple solution is presented by SNI, which indicates the hostname in the initial TLS connection (TLS Hello). This way, the server knows which website to get the certificate from to complete the TLS handshake.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### SNI-Hostname Mismatch

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Domain fronting takes advantage of SNI presented to the server. The hostname is the actual destination the packet is going to, and it's encrypted. The only information the servers have is from the SNI, and attackers can simply spoof the SNI value to something legitimate.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

An example scenario:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Hostname : `www.badsite.com`
2.  SNI spoofed to show: `www.goodsite.com`

<!-- /wp:list -->

<!-- wp:paragraph -->

Since the hostname is encrypted, no one knows im going to `www.badsite.com`, and they can only access the SNI data to assume that i'm visiting `www.goodsite.com`

<!-- /wp:paragraph -->

<!-- wp:image {"id":452} -->


![placeholder]({attach}media/2019/06/1.png){.wp-image-452}


<!-- /wp:image -->

<!-- wp:image {"id":453} -->


![placeholder]({attach}media/2019/06/2.png){.wp-image-453}


<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### Detection

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Domain fronting is used in other malicious scenarios, such as C2 communication and data exfiltration

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Detection of domain fronting obviously can't work just by observing the packet, as the contents are encrypted. Detection can thus only be done through behavioral analysis such as regular beaconing intervals, or suspicious packet sizes.

<!-- /wp:paragraph -->
