# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ""
RELATIVE_URLS = False

FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
AUTHOR_FEED_ATOM = ""
AUTHOR_FEED_RSS = ""
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
