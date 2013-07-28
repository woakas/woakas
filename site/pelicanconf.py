#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Woakas'
SITENAME = u'woakas'
SITEURL = 'http://woakas.pehik.co'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Blogroll

GITHUB_URL = 'http://github.com/woakas/'
DISQUS_SITENAME = "woakas"
SOCIAL = (('twitter', 'http://twitter.com/woakas'),
          ('github', 'http://github.com/woakas'),
          )
DEFAULT_PAGINATION = 3


FEED_DOMAIN = SITEURL

DISPLAY_PAGES_ON_MENU = True


# Plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Static files
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
STATIC_PATHS = ["static", ]

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# fotter colophon
COLOPHON = True
COLOPHON_TITLE = 'Colophon'
COLOPHON_CONTENT = 'El d&iacute;a es largo y la vida corta'

# Theme
THEME = "../theme-built-texts"

# Author
AUTHOR_SAVE_AS = False

# Analytics
MIXPANEL_ANALYTICS = "66043383c2f73a32095329de656bc0fc"
GOOGLE_ANALYTICS = "UA-42789249-1"
