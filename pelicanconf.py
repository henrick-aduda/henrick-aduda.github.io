#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Henrick'
SITENAME = 'The Healing Poet'
SITEURL = 'thehealingpoet.org'
THEME ='./attila/' 
PATH = 'content'
LOAD_CONTENT_CACHE = False
TIMEZONE = 'Africa/Nairobi'
HEADER_COVER = 'static/cover_photo.jpg'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISQUS_SITENAME = "attilademo"
GOOGLE_ANALYTICS = "UA-149301960-1"
CSS_OVERRIDE = ['css/darkly.css']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extras']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'}
}
