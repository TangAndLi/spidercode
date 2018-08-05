# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DyprojectsItem

class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']
    rules = (
        Rule(LinkExtractor(allow=r'list_23_\d+\.html'), callback='parse_item', follow=True),
    )

    def info(self,response):
        print(2222)
        # 获取到传递过来的参数
        item = response.meta['item']
        # 接着解析网页，获取item的其它信息
        item['image_url'] = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
        # item['story_info'] = response.xpath('')
        item['download_url'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()
        yield item

    def parse_item(self, response):
        table_list = response.xpath('//div[@class="co_content8"]/ul//table')
        for table in table_list:
            item = DyprojectsItem()
            item['name'] = table.xpath('.//a[@class="ulink"]/text()').extract_first()
            item['movie_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
            movie_url = 'http://www.dytt8.net'+ table.xpath('.//a[@class="ulink"]/@href').extract_first()
            item['movie_url'] = movie_url
            # yield item
            print(movie_url)
            yield scrapy.Request(url = movie_url, callback=self.info, meta = {'item': item})


