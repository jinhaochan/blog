Title: What is UPnP? (And how it can be malicious)
Date: 2019-04-29 20:09
Author: jinhaochan
Category: Security
Tags: UPnP
Slug: what-is-upnp-and-how-it-can-be-malicious
Status: published

<!-- wp:paragraph -->

UPnP, which stands for Universal Plug n Play, is a set of networking protocols used to facilitate adding of new devices to the network. It comes enabled default on most new routers.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For example, when you connect a new printer to the network, it automatically becomes discoverable by all other devices without you having to configure the IP address, or opening ports on the firewall. It does so through the concept of zero-configuration networking, which at it's core consists of

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Automatic assignment of network address
2.  Automatic distribution and resolution of hostnames
3.  Automatic location of network services such as printers (through Service Discovery Protocol)

<!-- /wp:list -->

<!-- wp:paragraph -->

Device search and advertising is done over HTTP over UDP on port 1900

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This means that any UPnP compatible device can join the network and automatically get an IP address, broadcast it's name, advertise it's capabilities /services on request, and learn about capabilities / services on the network.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### UPnP Setup Steps

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### Addressing

<!-- /wp:heading -->

<!-- wp:paragraph -->

The device implements a DHCP client, and must search for a DHCP server on the network. If no DHCP server exists on the network, it then assigns itself an IP through AutoIP

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Discovery

<!-- /wp:heading -->

<!-- wp:paragraph -->

The device then uses Simple Service Discovery Protocol (SSDP) to advertise it's own service to Control Points (CP) on the network by sending SSDP Alive Messages, which provides very basic information about the device

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Description

<!-- /wp:heading -->

<!-- wp:paragraph -->

To learn more about the device, the Control Point must retrieve the device description from the URL provided from the SSDP. The Device Description comes in an XML format, and has information such as model number, serial number and manufacturer name.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Control

<!-- /wp:heading -->

<!-- wp:paragraph -->

After getting the description, the Control Point can send actions to the device via Simple Object Access Protocol (SOAP)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Notifications

<!-- /wp:heading -->

<!-- wp:paragraph -->

The UPnP device can send events or notifications to the Control Points on any changes that happen to it. This uses the General Event Notification Architecture (GENA)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Presentation

<!-- /wp:heading -->

<!-- wp:paragraph -->

If the device has any pages for presentation, the Control Point can receive it and load it on the web browser

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### How It Is Abused

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

UPnP does not perform any sort of authentication, and assumes that any devices that is connected is trusted.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Also, UPnP can automatically configure port forwarding on the router without having any user intervention, or authentication.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Flash UPnP attack was one of the attack that abused the UPnP protocol, and how it works was by sending a UPnP request to the router to forward ports, thus exposing it to the internet. The attack could also change your primary DNS server with a UPnP request.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The best defense therefore is to **disable UPnP on your routers**

<!-- /wp:paragraph -->
