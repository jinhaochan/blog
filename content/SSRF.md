Title: Server Side Request Forgery
Date: 2020-09-01 12:19
Author: Chan Jin Hao
Category: Security
Tags: SSRF
Slug: SSRF
Status: published


Server Side Request Forgery, or SSRF, is an attack where the attacker is able to make a request to an internal resource by pivoting through the server. By leveraging on the server to make a request to the internal resource, the request become seen as legitimate, because internal systems usually trust each other.

## SSRF through Forms

If the server and internal resource are hosted on the same machine, the attacker can leverage on internal systems by specifying the resource address to `localhost`, `127.0.0.1` or `0.0.0.0`. This attack vector is exposed if the application allows an input of an address or URL, and makes calls to them. For example, if we have an application that accepts a URL of a webpage, and sends a `GET` request to it to get certain resources, we can put in `localhost` for it to send a `GET` request to other internal services running on the same server

```
Legitimate call

www.vulnweb.com/?site=www.shop.com


SSRF to send requests to services running on the same server

www.vulnweb.com/?site=0.0.0.0
```


We can acheive the same effect if the other services are hosted not on the same machine, but on other internal IP addresses. In this cases, instead of injecting `0.0.0.0`, we could put `192.168.0.1`, or perform an enumeration of private IP address to discover the services.

Defences against these involve input sanitization, and prevent calls to `localhost`, `0.0.0.0` and `127.0.0.1` inputs. From a software engineering perspective, we can move towards a Zero Trust Artchitecture, which basically means we remove the explicit assumption that calls to internal systems from other internal systems are trusted, and every request must be authenticated.

There are ways to circumvent input sanitizations and removing strings, and that is through DNS replies that always return a localhost

## SSRF through DNS

If there are input sanitization rules to remove `localhost`, `0.0.0.0` or `127.0.0.1`, we can setup our own malicious domain name or DNS server to always return localhost.

```
badsite.com returns 0.0.0.0, which has the same effect as SSRF

www.vulnweb.com/?site=www.badsite.com

```

## Possible Detections

Looking for localhost variants in the URL, or DNS replies with localhost values. One possible false positive is when malicious domains are sinkholed, they are also resolved to localhost
