#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lizherui'
SITENAME = u"lizherui的程序世界"
SITEURL = 'http://www.lizherui.com'
GITHUB_URL = 'https://github.com/lizherui'
ARCHIVES_URL = 'archives.html'

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

DEFAULT_LANG = u'zh'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

GOOGLE_ANALYTICS = 'UA-42648273-1'

GOOGLE_CUSTOM_SEARCH_SIDEBAR = '012191777864628038963:sjrtj5zxtec'

DISQUS_SITENAME = 'lizheruisworld'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Blogroll
LINKS =  (('Google', 'https://www.google.com/ncr'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/lizherui'),
          ('Twitter', 'https://twitter.com/lzrak47'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100004875786021'),
          ('Linkedin', 'http://www.linkedin.com/profile/view?id=232391796'),
          ('Weibo', 'http://weibo.com/lzrm4a1'),
          ('Zhihu', 'http://www.zhihu.com/people/li-zhe-rui'),
         )

