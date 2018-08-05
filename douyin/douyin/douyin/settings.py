# -*- coding: utf-8 -*-

# Scrapy settings for douyin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douyin'

SPIDER_MODULES = ['douyin.spiders']
NEWSPIDER_MODULE = 'douyin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douyin.middlewares.DouyinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douyin.middlewares.DouyinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'douyin.pipelines.DouyinPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# mysql数据库
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_DB = 'douyin'
DB_CHARSET = 'utf8mb4'

# scrapy_redis 配置
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 使用的是scrapy_redis的去重类
SCHEDULER = "scrapy_redis.scheduler.Scheduler"     # 调度器使用是scrapy_redis的调度器
SCHEDULER_PERSIST = True      # 爬取的过程中是否允许暂停
# 配置存储的redis服务器
# REDIS_HOST = '10.36.137.107'
# REDIS_PORT = 6379
# REDIS_DB = 1
REDIS_URL = 'redis://10.36.137.107/1'
# 配置管道
ITEM_PIPELINES = {
   'douyin.pipelines.DouyinPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 200,  # 在管道中添加这条redis管道
}

# user-agent中间件
DOWNLOADER_MIDDLEWARES = {
   'douyin.middlewares.UserAgentMiddleware': 543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

LOG_LEVEL = 'WARNING'
DOWNLOAD_DELAY = 1
USER_AGENT = 'Aweme/1.8.8 (iPhone; iOS 11.2.6; Scale/3.00)'
FEED_EXPORT_ENCODING = 'utf-8'
AUTOTHROTTLE_START_DELAY = 1

# CLOSESPIDER_TIMEOUT = 3600      # 一小时后停止爬虫
