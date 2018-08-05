import scrapy
from scrapy import cmdline

# pycharm执行风格
cmdline.execute(["scrapy", "crawl", "douyins", "-o", "data.json"])
