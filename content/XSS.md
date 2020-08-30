Title: XSS - Revisited
Date: 2020-08-30 13:50
Author: Chan Jin Hao
Category: Security
Tags: XSS
Slug: XSS
Status: published


I've been doing this lessons by  [Pentesterlabs](www.pentesterlab.com), and i've learnt a few new things there, which is always great! To be honestly, i've never had any proper training or course in terms of offensive cyber security, especially the web. My experiences have mostly been centered around the Linux kernel, which is pretty niche and narrow. In this post, i'd like to talk very briefly about XSS, and the different ways to do it.

## Kinds of XSS

Very briefly, XSS can be done in 3 ways: Stored, Reflected, or DOM attacks.

In Stored XSS, a script is injected to the server, and it resides permanently on the server. The malicious script thus triggers everytime someone visits the server.

In Reflected XSS, the script is part of the URL, and is sent to other users to click on it. Once the victim clicks on the URL with the payload appended to it, the script is executed.

In DOM based attacks, we're injecting HTML DOMs, or Document Object Models to the server, and this is the attack that I have learnt a great deal from Pentesterlabs.

## DOM based attacks

I won't cover much on Stored and Reflected XSS, and those are pretty common. In Stored, you have to upload the script to the server, and in Reflected, you will see the payload in the URL.

For DOM based attacks, instead of seeing the script tags `<script></script>` that traditionally encapsulates the JS payload to be executed, we see DOMs being injected.

For example, we could inject an image which loads from an invalid path, and place an onerror function to trigger the payload.

DOMs can even use mouse events and links to trigger the scripts

```
<img src='zzzz' onerror='alert(1)' />
<div onmouseover='alert(1)'/> ; onmouseout; onmousemove; onclick
<a onmouseover='alert(1)'/> ; onmouseout; onmousemove; onclick
<a href='javascript:alert(1)' />
```

## Detection on the network

This is really new to me (I'm not a red teamer), and we could utilize these infomation to form detection rules in whatever engine we're using.

Things like XSS or SQLi are usually caught with some signature mapping, for example, a regex to detect an SQL statement in the URL. For XSS, instead of just detecting `<script></script>`, we must also include these DOMs. In any case, it's suspicious and unlikely that there would be DOMs existing in the URL.
