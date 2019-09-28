Title: How HTTPS Works
Date: 2018-11-18 22:36
Author: jinhaochan
Category: Security
Tags: HTTPS
Slug: how-https-works
Status: published

How does HTTPS work?
--------------------

We all know to use a HTTPS site instead of a HTTP, because it is more secure. We roughly know that the messages sent to and fro the client and server are encrypted, so any snooping person wouldn't know the contents, but how does it all work?

This post is motivated by Google's announcement that it is going to label all HTTP sites as insecure. HTTP sites are those that do not implement any encryption, and all your passwords and traffic are in plain text. The question should be, why do HTTP sites even exist anymore...

The HTTP in HTTPS
-----------------

HTTP traffic is how the client talks to the server. Its the language that is spoken when transferring information over the internet.

Below is an example of a HTTP traffic of a `GET` request sent to the server. It is sent when a user keys in his credentials, and clicks onto the login button.

\[code lang=text\]  
GET /bin/login?user=dumb+user&pw=12345&action=login HTTP/1.1  
Accept: image/gif, image/jpeg, \*/\*  
Referer: http://127.0.0.1:8000/login.html  
Accept-Language: en-us  
Accept-Encoding: gzip, deflate  
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)  
Host: 127.0.0.1:8000  
Connection: Keep-Alive  
\[/code\]

Because there is no encryption, all the contents are in plain text, including the username and password. By using a traffic inspection tool like WireShark, it takes little to no effort to analyze and pick out information like this.

The S in HTTPS
--------------

So we want to encrypt the traffic so that it is not in plain text, including all our passwords and contents we sent and recieve.

HTTPS (HTTP Secure) is simply HTTP wrapped up in SSL/TLS.

SSL is the predecessor of TLS, and both SSL 2.0 and 3.0 have been deprecated by the IETF (Internet Engineering Task Force, which is a community that develops and promotes protocols and standards pertaining to TCP/IP). As such, it is safer to disable SSL, and leave TLS and the default option for your browsers.

The being said, SSL/TLS does not does the actual encryption. It is only a handshake protocol that happens between the client and the server.

During the handshake, the following steps are taken:

1\) Hello

-   The client initiates the request by sending a `ClientHello`, which contains the information needed by the server to connect to the client via SSL, such as the cipher suites the client supports, and the SSL versions it supports.
    
-   The server then responds with a `ServerHello`, which contains similar information, and with the decision to use which cipher suite and SSL version to use

2\) Certificate Verification

-   The server now has to prove it's identity to the client, and it does so by an SSL certificate
    
-   An SSL certificate is a file that contains information about the server. This includes domain name, server name or hostname, organization name, location, the server's public key and certificate validity.

-   The client either verifies the certificate with a CA, or implicitly trusts the certificate (Clicking on the button "Trust Anyway")

3\) Key Exchange

-   Once the client trusts the server, and the cipher suites have been chosen, the client generates a symmetric key to be used for encryption and decryption.
    
-   The symmetric key is then encrypted using the server's public key, an sent over to the server. (Asymmetric encryption is used to encrypt the symmetric key to be used. Encrypt-ception!)

-   The following messages sent and recieved by the client and the server are thus encrypted/decrypted by this symmetric key

Conclusion
----------

HTTP sends everything in plain text. We then use SSL/TLS to encrypt the plain text traffic, to prevent people from snooping in on our information.

We briefly described the processes involved in setting up the SSL/TLS connection, which includes the initiation, certificate verification, and key exchange.

Happy surfing!
