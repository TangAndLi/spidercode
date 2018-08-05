from scrapy import cmdline

# cmdline.execute('scrapy startproject freexs'.split())     # 普通类
# cmdline.execute('cd freexs'.split())
# cmdline.execute('scrapy genspider freexs https://www.freexs.org/'.split()     # spider类
# cmdline.execute('scrapy genspider -t crawl fxsspider https://www.freexs.org/'.split())  # crawspider类
cmdline.execute('scrapy crawl fxsspider'.split())  # 运行爬虫
# cmdline.execute('scrapy crawl fxsspider -s JOBDIR=crawls/somespider-1'.split())  # 运行爬虫
