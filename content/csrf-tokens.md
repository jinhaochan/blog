Title: CSRF Tokens
Date: 2019-04-24 16:13
Author: jinhaochan
Category: Security
Tags: CSRF
Slug: csrf-tokens
Status: published



If we look at source codes of HTML forms, we typically can spot this field being rendered on the webpage



<!-- wp:image {"id":420} -->


![placeholder]({attach}media/2019/04/token.png){.wp-image-420}  

<figcaption>
  

</figcaption>





Sometimes it doesn't have the name called CSRF Token, and it just appears as a random gibberish value being loaded.





This post breaks down the purpose of the token, and what happens behind the scenes with the token



<!-- wp:heading {"level":3} -->

### Understanding CSRF  





------------------------------------------------------------------------






CSRF stands for Cross-Site Request Forgery, and understanding how it works is a prerequisite to understanding CSRF tokens. Below shows a picture of what a CSRF attack looks like



<!-- wp:image {"id":421} -->


![placeholder]({attach}media/2019/04/csrf-cross-site-request-forgery.png){.wp-image-421}




<!-- wp:list {"ordered":true} -->

1.  The attacker crafts a GET requests that triggers a fund transfer to his account
    -   `GET http://bank.com/transfer.php?account=Attacker&amount=100`
2.  The attacker embeds this request as a hyperlink
    -   `<a href="http://bank.com transfer.php?account=Attacker&amount=100"> READ MORE... </a>`</code>
3.  When the user clicks on the link, it triggers the `GET` request on behalf of the victim
4.  The `GET` request is triggered by the victim, and funds are transferred to the Attacker





This attack hinges on the fact that the Victim must be logged in to the service, and is already authenticated with an open session with the service.





If the Victim is not logged in, when he clicks on the malicious link, instead of triggering the bad `GET` request, it will redirect him to the login page instead, thus rendering the attack useless.



<!-- wp:heading {"level":3} -->

### CSRF Tokens





------------------------------------------------------------------------






CSRF token is a simple concept where include one more argument of a token, that is sort of like a secret password.





`http://bank.com/transfer.php?account=User&amount=100&token=32Sa2dsa10gB88vcx9cz08f331j=Da`





This token value is a high-entropy value which is hard to guess by the attacker. If on the server side, it receives a wrong or missing CSRF token value, the `GET` request is rejected and does not execute





The CSRF token works this way:



<!-- wp:list {"ordered":true} -->

1.  Client requests for a HTML page that contains a form
2.  Server generates two distinct tokens, and sends one as a cookie to the client, and embeds the other as a hidden field in the form
3.  When the client submits the form, both CSRF tokens must be sent back to the server. The one embedded in the form, and the one in the cookie.
4.  If the request does not contain both tokens, it's rejected





The CSRF token value should be regularly invalidated at a time interval, per request, or when the user logs out.



<!-- wp:heading {"level":3} -->

### CSRF Token Vulnerabilities





------------------------------------------------------------------------






If traffic carrying the token is not encrypted over HTTPS, the Attacker can sniff the traffic and obtain the CSRF token value and the Cookie, and perform a CSRF token replay attack.





The solution to this is obvious: Always use encryption for communication. Aside from that, per-request-tokens can also be implemented.


