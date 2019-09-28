Title: Setting Up Your Own IDS
Date: 2018-12-30 19:49
Author: jinhaochan
Category: Security
Tags: Mininet, SDN, Snort
Slug: setting-up-your-own-ids
Status: published

Mininet Floodlight Snort
========================

In this post, we're going to be building our own IDS setup to play around with.

This setup can be used as a POC, or to just see how an IDS works. We're going to be using 3 technologies here.

1.  Mininet, which is a program to create your own virtual network on your host.
2.  Snort, which is an IDS program
3.  Floodlight, which is an SDN controller

\[gallery ids="110,109,108" type="rectangular" link="none"\]

The Setup
---------

We're going to setup an SDN network with 5 hosts, with host 5 sniffing traffic on host 4 using Snort.

This project will have 3 malicious actors (h1, h2, h3), a victim machine (h4) and an IDS using Snort sniffer (h5)

We will configure the network such that the 5 hosts are connected to the a switch, and the switch is connected to Floodlight SDN Controller. h1, h2 and h3 will attack h4 with a DoS attack, and h5 will be able to pick it up using Snort rules.

Setting up floodlight
---------------------

\[code lang=text\]  
git://github.com/floodlight/floodlight.git  
\$ cd floodlight  
\$ git submodule init  
\$ git submodule update  
\$ ant

\$ sudo mkdir /var/lib/floodlight  
\$ sudo chmod 777 /var/lib/floodlight  
\[/code\]

After you've configured Floodlight, run it with:  
`$ java -jar target/floodlight.jar`

Floodlight GUI will be running on http://localhost:8080/ui/pages/index.html

Setting up mininet
------------------

Clone and install:

\[code lang=text\]  
\$ git clone git://github.com/mininet/mininet  
\$ cd mininet  
\$ sudo ./util/install.sh -a  
\[/code\]

Mininet is now installed.

Spawn your network with the command:

`$ sudo mn --topo single,5 --controller=remote,ip=127.0.0.1,port=6653`

Spawns a single layer network, with 5 hosts connected to a switch.

The switch is connected to a remote controller, which is the floodlight service you setup earlier.

*Note: your port specified in this command should be `6653` and not `8080`. `8080` is used for showing the UI, `6653` is used for communicating with your switch.*

If your floodlight service is running on another machine, configure the `ip` and `port` accordingly.

Setting up Snort (In Ubuntu)
----------------------------

Before installing Snort, you have to first install DAQ

Updating your apt

\[code lang=text\]  
\$ apt-get update -y  
\$ apt-get upgrade -y  
\[/code\]

Installing dependencies  
`$ apt-get install openssh-server ethtool build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev liblzma-dev openssl libssl-dev`

Grabbing DAQ source (Change the value of the version to the lastest one)

\[code lang=text\]  
\$ wget https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz  
\$ tar xvf daq-2.0.6.tar.gz  
\$ cd daq-2.0.6  
\[/code\]

Configure and install DAQ

\[code lang=text\]  
\$ ./configure && make && make install  
\[/code\]

Now that you've installed DAQ, you can proceed to install Snort

Grabbing Snort source (Change the value of the version to the lastest one)

\[code lang=text\]  
\$ wget https://www.snort.org/downloads/snort/snort-2.9.8.3.tar.gz  
\$ tar vzf snort-2.9.8.3.tar.gz  
\$ cd snort-2.9.8.3  
\[/code\]

Configure and install Snort

\[code lang=text\]  
\$ ./configure --enable-sourcefire && make && make install  
\[/code\]

Link the libraries

\[code lang=text\]  
\$ ldconfig  
\[/code\]

Creating a symbolic link to Snort binary

\[code lang=text\]  
\$ ln -s /usr/local/bin/snort /usr/sbin/snort  
\[/code\]

Test it out!  
`$ snort -V`

After Snort is up and running, you will need to create directory structures for it

\[code lang=text\]  
\$ mkdir /etc/snort

\$ mkdir /etc/snort/preproc\_rules

\$ mkdir /etc/snort/rules

\$ mkdir /var/log/snort

\$ mkdir /usr/local/lib/snort\_dynamicrules

\$ touch /etc/snort/rules/white\_list.rules

\$ touch /etc/snort/rules/black\_list.rules

\$ touch /etc/snort/rules/local.rules

\$ chmod -R 5775 /etc/snort/

\$ chmod -R 5775 /var/log/snort/

\$ chmod -R 5775 /usr/local/lib/snort

\[/code\]

Configuring Snort Rules
-----------------------

Download Snort rules here https://www.snort.org/downloads

Edit your `snort.conf` accordingly to remove any preprocessors you don't have

If you're having trouble, `$ sudo find / -type f -name snort.conf`

Adding a rule in `snort.conf` to catch DoS by ICMP packets

`alert icmp any any -&gt; any any (threshold: type both, track by_dst, count 70, seconds 10; msg: "DoS by ICMP detected"; sid:1001;)`

Mirroring port h4 to h5 and sniff using Snort
---------------------------------------------

Command to mirror h4 traffic to h5  
`mininet$ s1 ovs-vsctl -- set Bridge "s1" mirrors=@m -- --id=@s1-eth4 get Port s1-eth4 -- --id=@s1-eth5 get Port s1-eth5 -- --id=@m create Mirror name=e4toe5 select-dst-port=@s1-eth4 output-port=@s1-eth5`

Now all traffic that is flowing into h4 will be mirrored onto h5, where Snort is running.

`mininet$ xterm h5`

In the new terminal spawned for h5, run:

`h5$ ifconfig` to get the adapter name

`h5$ snort -i &lt;Adapter name&gt; -c &lt;snort.conf location&gt; &amp;`

h5 is now sniffing traffic on h4

Starting the attack
-------------------

`mininet$ h1 ping -f h4`

This launches a barrage of ICMP packets from h1 to h4, which will subsequently be detected by h5, who is sniffing h4.

h5 will then write an alert which you should see in `/var/log/snort/alert` the message `"DoS by ICMP detected"`
