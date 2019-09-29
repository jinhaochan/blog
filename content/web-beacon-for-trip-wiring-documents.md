Title: Web Beacon for Trip wiring documents
Date: 2019-03-03 14:25
Author: Chan Jin Hao
Category: Security
Tags: Web Beacons
Slug: web-beacon-for-trip-wiring-documents
Status: published



During my course of security research work, I came across this concept of web beacons, which is a clever way of knowing who has opened up a document.





A Web Beacon is an element inside the document, that is not a saved resource. Rather, the element sends a request out to a server to retrieve the resource. An example of this would be an image tag, that requests the image resource from a server.





For example, writing this piece of code fetches the image resource from www.w3schools.com server:





`img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com" style="width:104px;height:142px;"`



<!-- wp:image {"align":"center"} -->




![W3Schools.com](https://www.w3schools.com/images/w3schools_green.jpg)  
<figcaption>
Image retrieved from w3 schools
</figcaption>








It's a very simple concept, and we can make use of this functionality and twist it to be a defensive tool



<!-- wp:heading {"level":3} -->

### Web Server Request Tracking





------------------------------------------------------------------------






If we can setup our own server that hosts resources, we can secretly embed invisible images, or elements that makes requests to our servers to retrieve those resources.





This way, when the document is opened, the tries to render itself by making a request to our server for the resource. It acts as a tripwire that immediately triggers the moment the document is opened. And as the image is is not obvious to the threat actor, he would not be aware of this callback.



<!-- wp:heading {"level":3} -->

### Improvements?





------------------------------------------------------------------------






The obvious drawback to this is that, once the document is taken to an offline premise, the image can no longer make a request to our server. This means that we will not be notified when the tripwire is activated.





The second drawback is: So what?





So what if I know if the document has been opened by some unauthorized person, or in another location? What can I do to prevent him from opening it? Some simple solutions that I came up with are:





If the requesting IP address is not in the whitelist, we return an extremely huge image, hopefully to make the document hang and not be usable.





Another improvement is, aside from image resources, what other resources can be requested, and hopefully such resources can be "executed". Of course, such a solution is considered intrusive, because then it can be used in malicious ways for remote code execution.


