Title: What are Proxies?
Date: 2019-06-21 09:57
Author: jinhaochan
Category: Security
Tags: Proxy
Slug: what-are-proxies
Status: published

<!-- wp:paragraph -->

A Proxy, or a Proxy Server / Web Proxy, is something that sits between the source of the network traffic, and the desired destination of the traffic. What the proxy will do is relay the network traffic across to the other side.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Typically, it would sit between a client and a server, where the client is usually a web browser, and the server being the web server that hosts its resources.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Forward Proxies

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:image {"id":457} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/06/1-1.png){.wp-image-457}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

Forward proxies are setup such that the clients are behind a proxy server that passes all the network traffic from the clients to the server.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Such a setup is viable for several security reasons, such as centralized scanning of traffic, identify protection and blocking of content.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The downsides of this is that all the clients share the same bandwidth on the proxy server, thus potentially slowing the network speed for everyone.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Reverse Proxy

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:image {"id":458} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/06/2-1.png){.wp-image-458}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

A reverse proxy is the same as the forward proxy, but it's implemented on the server side instead. Multiple servers sit behind the reverse proxy, and the proxy routes the network traffic to the correct servers based on packet information.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The reasons for a reverse proxy also pertain to security such as DDoS protection, but also includes load balancing, where the reverse proxy can detect which server is being overloaded, and redirect the traffic to other servers.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Types of Proxies

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### HTTP Proxies

<!-- /wp:heading -->

<!-- wp:paragraph -->

HTTP proxies are designed specifically for proxying HTTP information. HTTP proxies cannot proxy for other types of protocols.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

There is also an encrypted version of a HTTPS proxy to prevent the proxy (or anyone along the pipeline) from seeing any data being transferred.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Because HTTP or HTTPS runs on TCP, this means that the HTTP proxy only supports TCP protocols

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### SOCKS Proxies

<!-- /wp:heading -->

<!-- wp:paragraph -->

While HTTP proxies are only meant for HTTP traffic, SOCKS operate on a lower level, and thus can support almost all protocols including both TCP and UDP types, as well as HTTP traffic.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The SOCKS proxy server establishes the TCP connection on behalf of the client with an external server, and then uses that connection to route traffic between the client and server.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

SOCKS does not touch the data stream at all, only setting up the connection and routing the traffic.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Comparison between the Proxies

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### Security

<!-- /wp:heading -->

<!-- wp:paragraph -->

In both proxies (HTTPS and SOCKS, not HTTP), encryption is present, thus your data flowing through is secure.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Speed

<!-- /wp:heading -->

<!-- wp:paragraph -->

As SOCKS proxies only route data traffic and never touches the data inside, they can route the data much faster. However, most of the time the speed differences are negligible.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Features

<!-- /wp:heading -->

<!-- wp:paragraph -->

Since SOCKS proxies supports multiple protocols including HTTP, why still do we need a HTTP proxy?

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Because HTTP proxies understand the HTTP traffic that is flowing through, the client and the external server can both talk to the proxy server over HTTP. This can allow the HTTP proxy to do things like caching to improve performance.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The SOCKS proxy on the other hand, does not understand HTTP traffic, and only routes the data that is flowing through. You cannot talk directly to the SOCKS server in HTTP.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Also, SOCKS proxies support both TCP and UDP connections, which can be used by more programs.

<!-- /wp:paragraph -->
