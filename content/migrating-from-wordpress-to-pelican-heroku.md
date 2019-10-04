Title: Migrating from Wordpress to Pelican + Heroku
Date: 2019-09-28 17:54
Author: Chan Jin Hao
Category: Software Engineering
Tags: Heroku
Slug: migrating-from-word-press
Status: published

I used to write my blog posts on Wordpress, and it was doing a good job. I had a few blogs on WP, one was my technical blog, and another was just me rambling about life. But I realized that Wordpress was not very friendly to `coding blog posts`. Sure, they had a code block segment, but the horrible switching from blockmode to classic mode was a pain

Also, I found out that I really wanted control of the things that I am building. Building my own site (Well... with the help of Pelican) gave me the granularity of control I want. While I'm not building everything from ground up, at least I have the power to control the things around my blog. 

And writing in markdown is fun!

In this post, I'm going to run through the thing I did to make this happen. It took literally one day for me to migrate all my posts over to Pelican.

---

### Exporting Your Wordpress Posts

---
This part is fairly simple. Thankfully, the things you create on Wordpress are yours to keep. That was one of my biggest initial fear at first, where my content was not kept by me. And if the unlikely case of Wordpress going under, all my posts are lost.

In this step, you simply go to your Wordpress site, hit on Tools, and export both your posts and your media (images, videos etc)

![export your image]({attach}media/images/export.png)

### Setting up Pelican

---
Once you got your back up ready, we're now going to setup Pelican on your local machine, before pushing it up to Heroku

Its pretty straight forward, and you can follow the guide here: [Pelican Quickstart](http://doc.getpelican.com/en/latest/quickstart.html)

Basically you

1. Install Pelican
2. Start a placeholder project
3. Move on to the next step

### Setting up Heroku

---
Of course, if everything was so simple, why the hell would I want to write this post? It's always the system integration where the troubles pop up.

Assuming that you already have a Heroku account and downloaded Heroku toolbelt on your local machine, then getting the contents of `requirements.txt` and `Procfile` are the trickiest

- `requirements.txt`

```
pelican
Markdown
typogrify
gunicorn
static
```

- `Procfile`

`web: pelican content --listen --port $PORT`

The reason for doing `$PORT` is that you can't choose which port Heroku listens on, so you set it to pull from the Heroku environment with `$PORT`

### Importing your Wordpress contents over

---
With that done, you can start to import your Wordpress content over.

Your Wordpress files downloaded earlier would be in XML format, and thankfully, Pelican has a module that does all the heavy lifting for you.

`pelican-import --wpfile <filename> -m markdown`

If you don't specify `-m markdown`, it will default to `.rst`, which causes a whole lot of rendering problems

But wait! You're not done yet.

All the pictures and media within your posts are linked to the Wordpress format, which would look something like this

`![](chanjinhao.files.wordpress.com/2019/01/img.png)`

This would not work, as proper rendering would look something like this

`![placeholder]({attach}media/img.png)`

To make your life easier, here's a command to replace all strings, in all files

`find . -name '*.md' -exec sed -i -e 's/<old>/<new>/g' {} \;`

What this does is to find all files ending with `.md`, and execute a `sed` replacement call. In this case, our command would look like this:

`find . -name '*.md' -exec sed -i -e 's/chanjinhao.files.wordpress.com\{attach\}media//g' {} \;`

We also need to remove all the wordpress, and html stuff. I'll leave you to figure out how to do it given the command above.

### GOGOGO

---
Once you're done with that, run the command 

`pelican`

to see if there's any issues with your build. Once you fixed all the errors, you can proceed to 

```
git add .
git commit -m "first push to heroku"
git push heroku master
```

And your new website should be live!

I've aliased those 3 commands to `GOGOGO` (since they all start with G, and it saves a lot of keystrokes)

### Others

---
If you wanna play around with the whole setup, you can look at things like Pelican themes, and Pelican plugins

[Themes](https://github.com/getpelican/pelican-themes)

[Plugins](https://github.com/getpelican/pelican-plugins)

