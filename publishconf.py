#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://co3k.org'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/blog.atom'
CATEGORY_FEED_ATOM = None
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
