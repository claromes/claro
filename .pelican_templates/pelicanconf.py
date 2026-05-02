AUTHOR = ""
SITENAME = ""
SITEURL = ""
SITEIMAGE = ""
SITEDESCRIPTION = ""
KEYWORDS = ""
DEFAULT_DATE_FORMAT = "%d %b %Y"

FAVICON = ""
FIRST_NAME = ""

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

PATH = "content"
THEME = "claro/theme/claro"

STATIC_PATHS = ["images", "extras/_redirects"]
EXTRA_PATH_METADATA = {"extras/_redirects": {"path": "_redirects"}}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["gzip_cache", "share_post", "sitemap"]

DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = False
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# SITEMAP PLUGIN
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.99, "pages": 0.75, "indexes": 0.5},
    "changefreqs": {"articles": "daily", "pages": "daily", "indexes": "daily"},
    "exclude": ["author/", "category/"],
}

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
