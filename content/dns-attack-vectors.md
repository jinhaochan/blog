Title: DNS Attack Vectors
Date: 2019-07-07 14:50
Author: Chan Jin Hao
Category: Security
Slug: dns-attack-vectors
Status: published



Before looking at DNS Attack Vectors, let's do a quick recap of what a DNS is, and what are it's functions.



<!-- wp:heading {"level":3} -->

### What is a DNS?





------------------------------------------------------------------------






DNS, or Domain Name System, is a server that provides Name to IP Address resolution. When people visit websites, it's much easier for them to remember words, such as Facebook or Hotmail, and the DNS server translates these URLs to IP address such as 73.22.512.31.





Machines in a network, and groups of networks references a DNS server which manages a huge database of domain names to IP addresses. The act of mapping a domain name to an IP is called `DNS Name Resolution`.





When you connect to a home or business network, the service providers that assign your IP address also sends network configurations that includes 1 or more DNS servers that the device should use to perform DNS Name Resolution.





DNS traffic takes place on port 53, and has both TCP and UDP protocols



<!-- wp:heading {"level":3} -->

### DNS Attacks  





------------------------------------------------------------------------






Now that we have a rough idea of what a DNS does, lets look at the attack vectors that can target DNS servers



<!-- wp:heading {"level":4} -->

#### 1. DNS Tunneling





DNS tunneling is a method of attack that encodes data of programs into DNS queries and responses





The malicious actor must first own a domain name, and his own local DNS server. In this example, we have the domain `server1.test.com`





The typical steps of a DNS tunneling attack is as follows:



<!-- wp:list {"ordered":true} -->

1.  Client sends out a DNS Name Resolution request to the DNS server, but the domain is modified to contain pieces of data: `MYDATA.server1.test.com`
2.  The DNS server does the IP address resolution of `server1.test.com`, and sends the modified request to that server
3.  The information of `MYDATA.server1.test.com` is forwarded to the malicious server
4.  The bad actor can inspect the packets to view information from the DNS queries, thus achieving data exfiltration





DNS tunneling takes advantage of the fact that domain names are allowed up to 255 characters, but most domain names typically do not go that long. The additional data can thus be appended into the unused character space



<!-- wp:heading {"level":4} -->

#### 2. DNS Cache Poisoning





DNS cache poisoning is an attack that corrupts the DNS cache so that when DNS Name Resolution is done, it points to a malicious IP address instead of the legitimate one.





The internet has more than one DNS servers for name resolution, and DNS servers would cache information from other DNS servers for efficiency in querying. Your machine also has a local DNS cache which performs a quick lookup, instead of performing DNS Name Resolution again.



<!-- wp:heading {"level":4} -->

#### 3. DNS Zone Transfer Attack





A legitimate DNS Zone Transfer occurs when a slave DNS server requests for information from the master DNS server to update it's DNS records





DNS Zone Transfers are performed by TCP protocols to ensure lossless data transfer.





Bad actors can leverage on this to pose as a slave DNS server, and download all information from the master DNS server, thus revealing information about the network.



<!-- wp:heading {"level":4} -->

#### 4. DNS Domain Lock-Up





Domains are setup by attackers. When the target DNS server sends a request to one of the malicious Domains, the domains don't send the proper reply to end the connection, but instead send random junk to keep the TCP connection to the DNS alive.





When enough connections are kept alive, this exhausts the DNS resources to perform further Name Resolutions.



<!-- wp:heading {"level":4} -->

#### 5. DNS Water Torture Attack and NXDomain (Non-Existent Domain)





When requests with invalid domain names are sent to the DNS server, the DNS server replies with NXDomain, which indicates that the domain names are not valid.





The DNS stores all these queries and NXDomain responses in the cache, and if these requests happens on a large scale, it can flood the cache, thus preventing further Name Resolutions from happening. This essentially is a DDoS on DNS servers.





This attack is analogous to a MAC flooding attack, which fills up the cache with bogus MAC addresses.  


