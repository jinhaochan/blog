Title: What is a CGI?
Date: 2019-04-08 17:11
Author: jinhaochan
Category: Security
Tags: cgi
Slug: what-is-a-cgi
Status: published

<!-- wp:paragraph -->

Not Computer Generated Imagery, but `cgi` pages you see when you visit webpages.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

CGI stands for Common Gateway Interface, and it acts as the Controller in the MVC framework. To give a complete picture, in a web application, the Model is the database, the View is the front-end HTML/CSS, and the Controller is the logic that processes user interaction

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The CGI program takes in input from the user via the webpage, does the processing, and outputs information back to the front-end.

<!-- /wp:paragraph -->

<!-- wp:image {"id":392,"align":"center"} -->

<div class="wp-block-image">

<figure class="aligncenter">
![]({attach}media/2019/04/cgi.gif){.wp-image-392}
</figure>

</div>

<!-- /wp:image -->

<!-- wp:paragraph -->

CGI is a generic name for any program, or script that runs at the back end to process the user input. This program can be written in languages such as Python, C or C++. An example of a Python CGI is:

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

`http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2`

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Programming vs CGI Programming

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Most of us are familiar and have experience with the languages mentioned above, but there is a difference between conventional programming with those languages, and programming to conform to CGI standard.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Below shows a code snippet of CGI programming in Python:

<!-- /wp:paragraph -->

<!-- wp:code -->

``` {.wp-block-code}
#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '</body>'
print '</html>'
```

<!-- /wp:code -->

<!-- wp:paragraph -->

There are two main differences here:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  The CGI program must start with a MIME-type header.
    -   MIME, which stands for **Multipurpose Internet Mail Extensions** is a HTTP header which tells the client what sort of content it's receiving.
    -   `print "Content-type:text/html\r\n\r\n"`
2.  The content of the output must be in HTML format, or other formats that the browser is able to display

<!-- /wp:list -->

<!-- wp:heading {"level":3} -->

### CGI Environment Variables  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

When programming a CGI program, there are some environment variables that are standard across all CGI, regardless of languages used.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Some examples of these are:

<!-- /wp:paragraph -->

<!-- wp:table -->

  ------------------- ----------------------------------------------
  HTTP\_COOKIE        The visitor's cookie, if one is set
  HTTP\_HOST          The hostname of the page being attempted
  HTTP\_REFERER       The URL of the page that called your program
  HTTP\_USER\_AGENT   The browser type of the visitor
  ------------------- ----------------------------------------------

<!-- /wp:table -->

<!-- wp:paragraph -->

You can see the full list of CGI environment variables by searching it online.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### CGI Vulnerabilities

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Most CGI vulnerabilities lie in the fast that the inputs from the users are not properly checked and parsed. As a result, the user can perform unintended actions on your server such as directory traversal or RCE.

<!-- /wp:paragraph -->
