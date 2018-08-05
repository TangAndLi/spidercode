# -*- coding: utf-8 -*-
import scrapy



class NameSpider(scrapy.Spider):
    name = 'name' # 爬虫名字
    allowed_domains = ['www.dytt8.net']  # 允许的域名
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html'] # 起始url

    def parse(self, response):
        pass
