#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'奇百'
SITENAME = u"奇百的博客"
SITEURL = 'http://cheniqit.github.com'

GITHUB_URL = 'https://cheniqit.github.com'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

DEFAULT_LANG = u'zh'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

GOOGLE_ANALYTICS = ''

GOOGLE_CUSTOM_SEARCH_SIDEBAR = '012191777864628038963:sjrtj5zxtec'

DISQUS_SITENAME = 'cheniqit'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PLUGIN_PATHS = ['C:/Users/Administrator/Git/pelican-plugins']
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
LINKS =  (('Zhihu', 'http://www.zhihu.com/'),
          ('Python', 'http://python.org/'),
          ('Pelican', 'http://docs.getpelican.com/'),
          ('Maxing', 'http://maxiang.info/')          
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/cheniqit'),
          ('Weibo','http://weibo.com/cheniqit'),
         )

