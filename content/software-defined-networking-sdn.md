Title: Software Defined Networking (SDN)
Date: 2018-12-23 10:29
Author: jinhaochan
Category: Networking
Tags: SDN
Slug: software-defined-networking-sdn
Status: published

What is an SDN
==============

------------------------------------------------------------------------

Software Defined Networking is a way of abstracting away the control logic of networking and packet switching away from the physical switches, and passing that control to a SDN Controller.

The main idea of this is to allow the control to perform decision making on what to do with the packets on the switches behalf.

Components and Architecture of a SDN
====================================

------------------------------------------------------------------------

![Untitled Diagram (1)](https://chanjinhao.files.wordpress.com/2018/11/untitled-diagram-1.png){.alignnone .size-full .wp-image-105 width="686" height="406"}

It'll make more sense when the flow is explained bottom up, from the infrastructure layer.

**[Infrastructure layer (Data Plane)]{style="text-decoration:underline;"}**

This is where your physical switches are. The packets from the network, be it intranet or internet, flows through these switches. Conventionally, a dedicated software will be running on each of the switches, deciding what do with the each packet that passes through them.

Now, instead of the switches making the decision, the control is passed to the Control layer. This means that the switches will have to query the SDN Controller about what action to take for each packet.

But it's not that dumb to query the controller for every single packet. The SDN Switch has a table which stores a set of rules as to what action to perform for which packet. Only when a packet does not match any rows on the table, does the SDN Switch query the controller.

The SDN Switch gets the information from the SDN Controller via Southbound protocols, such as Openflow. (We'll cover that later)

**[Control layer (Control Plane)]{style="text-decoration:underline;"}**

The SDN Controller acts as the brains of the system. You can think of it as the CPU, where it brokers requests from the hardware to the application, vice-versa.

The applications are able to push their desired changes down to the controller, where the controller disseminates the changes down to the SDN Switches via Openflow.

One scenario might be a change in firewall rules done on a firewall application. This change is then push down to the SDN Controller, and down to the SDN Switches.

An example of an SDN Controller is [Floodlight ](https://github.com/floodlight/floodlight)

[**Application layer**]{style="text-decoration:underline;"}

The application layer where all your applications sit. Before SDN, they used to sit on the physical switch itself. That made it tedious to execute updates or changes to the software on the switch when you have multiple switches.

With SDN, these applications are taken out of the switch, and resides elsewhere. These applications can also be virtualized via a concept known as Network Functions Virtualization (NFV). NFV is just another way of describing virtualizing Networking Software, such as firewalls and IDS systems.

 

North-Bound API (OpenDayLight)

South-Bound API (Openflow)

Benefits of a SDN
=================

------------------------------------------------------------------------

In the past, your network topology was defined by your physical switches. Now that the applications have been extracted out the switches, your network topology is effectively defined by your software (hence the name Software Defined Network).

This gives you more control the of switches, and the ease of configuring them.

One draw back of SDN is the introduction of a single point of failure. Although it does give you more granular security by controlling each SDN Switch, the bottle neck lies in the SDN Controller.
