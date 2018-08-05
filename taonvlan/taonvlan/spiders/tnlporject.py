# -*- coding: utf-8 -*-
import scrapy


class TnlporjectSpider(scrapy.Spider):
    name = 'tnlporject'
    allowed_domains = ['v.taobao.com/v/content/video']
    start_urls = ['http://v.taobao.com/v/content/video/']

    def parse(self, response):
        table_list = response.xpath('//div[@class="anchor-card-content"]/div')
        print(table_list)

