#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chan Jin Hao'
SITENAME = u'glob'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('All', '/'),
         ('Data Science', '/category/data-science.html'),
         ('Cyber Security', '/category/security.html'),
         ('Software Engineering', '/category/software-engineering.html'),
         ('Book Reviews', '/category/review.html'),
         ('Ramblings', '/category/ramblings.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/jinhao-hao-chan-162630120/'),
        ('github', 'https://www.github.com/jinhaochan'),)

DEFAULT_PAGINATION = 10

THEME = "Flex"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
