Title: Domain Generating Algorithm (Used by C2 Communication)
Date: 2019-04-07 16:46
Author: jinhaochan
Category: Security
Tags: Domain Generation Algorithm
Slug: domain-generating-algorithm-used-by-c2-communication
Status: published

<!-- wp:heading {"level":3} -->

### C2 Communication and Disruption





------------------------------------------------------------------------



</p>


When a machine gets infected by a malware, it can start receiving command from it's C2 server to perform unwanted activities. Examples of this are a machines infected with botnets or ransomware, where the C2 server will send commands down to the victim machine, and the machines can send replies back.





The easiest way to tackle this problem is to disrupt the communication between the C2 and the victim machine, and one of this is to either take down the C2 server, or block all traffic that is going to that specific IP address.



<!-- wp:heading {"level":3} -->

### How Malwares Overcome Communication Disruption





------------------------------------------------------------------------



</p>


Bad actors are well aware of this problem of having a single static IP or server for their C2, and they know that if this single IP is block or the server is taken down, their infected machines have no where to receive commands from.





How they overcome this is by having their malware communicate with different domains instead of a single static one. This act is called **"Domain Fluxing**", or **"Fast Fluxing"**, where the malware communicates with different C2 servers.





The process of generating multiple domains for their malware to connect to is called **"Domain Generation Algorithm" (DGA)**.



<!-- wp:heading {"level":3} -->

### DGA in Action





------------------------------------------------------------------------



</p>


DGAs automatically generate multiple domains that the malware can communicate to. These DGA's have to be random enough, so that defenders cannot predict what list of domains to block. For example, if a malware is dumb enough to change their list of domains to "badserver1", "badserver2" ... Defenders just have to block "badserver\*", and that will cover all the list of C2 servers.





Dumb DGAs will also generate jibberish domains, which can be spotted easily by analyst, or smart NLP models. Domains such as "dsawkkl.com" generated randomly is obviously a malicious domain.





Smarter DGAs will pluck and piece together words that make sense, such as "Birds.com", "Elephant.com" or "Tiger.com". But this also has a downside, as its obvious that their seed for generating the names are animals. Really advanced DGAs will use and NLP text generator model, and a random seed generator to produce really legitimate looking domains that can fool both the analyst, and models.





Below is an example code to generate random domains



<!-- wp:code -->

``` {.wp-block-code}
def generate_domain(year, month, day):
    """Generates a domain name for the given date."""

    domain = ""

    for i in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)

    domain += chr(((year ^ month ^ day) % 25) + 97)
```

<!-- /wp:code -->

<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------



</p>


Malwares need to communicate with C2's for commands. It's easy to block a single domain, or list of correlated domains.





Malwares therefore need sophisticated DGAs to come up with unpredictable domains for their C2 server.


