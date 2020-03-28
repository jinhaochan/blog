Title: What are Proxies?
Date: 2019-06-21 09:57
Author: Chan Jin Hao
Category: Security
Tags: Proxy
Slug: what-are-proxies
Status: published



A Proxy, or a Proxy Server / Web Proxy, is something that sits between the source of the network traffic, and the desired destination of the traffic. What the proxy will do is relay the network traffic across to the other side.





Typically, it would sit between a client and a server, where the client is usually a web browser, and the server being the web server that hosts its resources.



<!-- wp:heading {"level":3} -->

### Forward Proxies





------------------------------------------------------------------------




<!-- wp:image {"id":457} -->


![placeholder]({attach}media/2019/06/1-1.png){.wp-image-457}






Forward proxies are setup such that the clients are behind a proxy server that passes all the network traffic from the clients to the server.





Such a setup is viable for several security reasons, such as centralized scanning of traffic, identify protection and blocking of content.





The downsides of this is that all the clients share the same bandwidth on the proxy server, thus potentially slowing the network speed for everyone.



<!-- wp:heading {"level":3} -->

### Reverse Proxy





------------------------------------------------------------------------




<!-- wp:image {"id":458} -->


![placeholder]({attach}media/2019/06/2-1.png){.wp-image-458}






A reverse proxy is the same as the forward proxy, but it's implemented on the server side instead. Multiple servers sit behind the reverse proxy, and the proxy routes the network traffic to the correct servers based on packet information.





The reasons for a reverse proxy also pertain to security such as DDoS protection, but also includes load balancing, where the reverse proxy can detect which server is being overloaded, and redirect the traffic to other servers.



<!-- wp:heading {"level":3} -->

### Types of Proxies





------------------------------------------------------------------------




<!-- wp:heading {"level":4} -->

#### HTTP Proxies





HTTP proxies are designed specifically for proxying HTTP information. HTTP proxies cannot proxy for other types of protocols.





There is also an encrypted version of a HTTPS proxy to prevent the proxy (or anyone along the pipeline) from seeing any data being transferred.





Because HTTP or HTTPS runs on TCP, this means that the HTTP proxy only supports TCP protocols



<!-- wp:heading {"level":4} -->

#### SOCKS Proxies





While HTTP proxies are only meant for HTTP traffic, SOCKS operate on a lower level, and thus can support almost all protocols including both TCP and UDP types, as well as HTTP traffic.





The SOCKS proxy server establishes the TCP connection on behalf of the client with an external server, and then uses that connection to route traffic between the client and server.





SOCKS does not touch the data stream at all, only setting up the connection and routing the traffic.



<!-- wp:heading {"level":3} -->

### Comparison between the Proxies





------------------------------------------------------------------------




<!-- wp:heading {"level":4} -->

#### Security





In both proxies (HTTPS and SOCKS, not HTTP), encryption is present, thus your data flowing through is secure.



<!-- wp:heading {"level":4} -->

#### Speed





As SOCKS proxies only route data traffic and never touches the data inside, they can route the data much faster. However, most of the time the speed differences are negligible.



<!-- wp:heading {"level":4} -->

#### Features





Since SOCKS proxies supports multiple protocols including HTTP, why still do we need a HTTP proxy?





Because HTTP proxies understand the HTTP traffic that is flowing through, the client and the external server can both talk to the proxy server over HTTP. This can allow the HTTP proxy to do things like caching to improve performance.





The SOCKS proxy on the other hand, does not understand HTTP traffic, and only routes the data that is flowing through. You cannot talk directly to the SOCKS server in HTTP.





Also, SOCKS proxies support both TCP and UDP connections, which can be used by more programs.


