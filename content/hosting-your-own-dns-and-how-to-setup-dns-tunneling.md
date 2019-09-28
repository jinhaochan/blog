Title: Hosting your own DNS (and how to setup DNS tunneling)
Date: 2019-04-11 11:23
Author: jinhaochan
Category: Security
Tags: DNS
Slug: hosting-your-own-dns-and-how-to-setup-dns-tunneling
Status: published

<!-- wp:paragraph -->

Earlier this week, I wrote a post on DNS tunneling, and how to pass information over the web through the DNS protocol by stuffing information in the DNS Name Resolution process.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this post, we're going to look at how to setup and host your own DNS server. And because you're hosting it, you can essentially choose to reply whatever you want to the subject querying you.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Components

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:list {"ordered":true} -->

1.  VM with a static IP address, and allowed ingress/egress connections for port 53.
    -   For this, I spun up a VM on GCP with minimal settings to reduce the cost
    -   I used a Linux based image because I planned to use bind9 for my DNS (https://wiki.debian.org/Bind9)
2.  A Domain name
    -   Head over to `my.freenom.com` for a free domain name with a `.tk` TLD

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Concepts

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:list -->

-   DNS Resolution
    -   When you send a query for a domain name, it queries your DNS for the corresponding IP address tied to the domain name
    -   Your DNS server then queries the Root Servers, which are DNS servers who hold information about the TLDs such as `.com` or `.tk`, and redirects your query to the TLD Server
    -   The TLD Server stores information about your second level domains. The `.com` server will store information such as `facebook.com` or `google.com`. In our case, we're using the `.tk` domain, so the `.tk` server will hold our website information `dnsserver.tk`. The TLD server defers the query to `dnsserver.tk`
    -   `dnsserver.tk` is known as the Authoritative Server, which gives the authoritative response of the IP address
-   DNS Glue Record
    -   A DNS glue record is used for preventing circular dependencies
    -   This is important when your DNS server is a subdomain of your domain name itself. e.g. `ns1.dnsserver.tk` is a subdomain of `dnsserver.tk`
    -   The circular dependency happens when we ask for the IP address of `dnsserver.tk`, and it tells you to ask it's DNS server `ns1.dnsserver.tk`. But in order to query `ns1.dnsserver.tk`, you need the IP address of `dnsserver.tk`
    -   To solve this issue, we "glue" the IP address of `ns1.dnsserver.tk`
    -   Now, instead of asking you to query `ns1.dnsserver.tk`, it'll give you the IP address of `ns1.dnsserver.tk` directly, breaking the circular dependency

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### Execution

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### GCP

<!-- /wp:heading -->

<!-- wp:paragraph -->

We will need to spin up the VM, get it's static IP, and host a DNS server on it. this VM will be our `ns1.dnsserver.tk`

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

You can follow this guide on how to setup bind9 on your VM https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-an-authoritative-only-dns-server-on-ubuntu-14-04

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

On your GCP console, you have to do 2 things

<!-- /wp:paragraph -->

<!-- wp:list -->

-   Open ports 53 to allow DNS traffic to flow through
-   Set your IP address to static, instead of ephemeral

<!-- /wp:list -->

<!-- wp:heading {"level":4} -->

#### Domain name console

<!-- /wp:heading -->

<!-- wp:paragraph -->

When you register for a new domain name, you can usually configure it. The free domain name we got from `my.freenom.com` allows your to specify your own Nameserver and glue records.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I've attached screen grabs on how to point the Nameservers to your `ns1.dnsserver.tk`, and how to glue your IP address to `ns1.dnsserver.tk` for breaking circular dependency

<!-- /wp:paragraph -->

<!-- wp:image {"id":405} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/04/2.png){.wp-image-405}


<!-- /wp:image -->

<!-- wp:paragraph -->

When setting up your glue records for the Nameservers, you can use the same IP address for both records. You need 2 records because when you specify new Nameserver, you need to input minimally 2 records

<!-- /wp:paragraph -->

<!-- wp:image {"id":406} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/04/1.png){.wp-image-406}


<!-- /wp:image -->

<!-- wp:paragraph -->

Instead of letting Freenom Nameservers to be the authoritative Nameserver, point it to your Nameservers your are hosting.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

When you set a new Nameserver, you need to wait a few hours for it to propagate the information over to other DNS servers.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In your DNS server, you can choose to return whatever you want when a DNS request comes to your server. In this way, it can be possible to craft it as a C2 communication server. I won't go into details on how to set that up, but this is one of the steps.

<!-- /wp:paragraph -->
