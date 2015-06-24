#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Damián Nohales'
SITENAME = u'nohales.org blog'
SITEURL = ''
GITHUB_REPO_URL = 'https://github.com/eagleoneraptor/blog.nohales.org'

PATH = 'content'

TIMEZONE = 'America/Buenos_Aires'

DEFAULT_LANG = u'en'

# THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SUMMARY_MAX_LENGTH = 40

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/eagleoneraptor'),
          ('google-plus', 'https://plus.google.com/+DamiánNohales'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

FILENAME_METADATA = '\d{4}-(?P<slug>.*)'

DELETE_OUTPUT_DIRECTORY = True
