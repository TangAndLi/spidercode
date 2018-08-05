# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from freexs.items import FreexsItem
from scrapy_redis.spiders import RedisCrawlSpider


class FxsspiderSpider(RedisCrawlSpider):
    name = 'fxsspider_redis'
    # allowed_domains = ['www.freexs.org']
    # start_urls = ['https://www.freexs.org/']

    redis_key = 'fxsspider_redis:start_urls'

    get_url = LinkExtractor(allow=r'class|top')
    get_content = LinkExtractor(allow=r'/info/')
    rules = (
            Rule(get_content, callback='parse_item', follow=True),
            Rule(get_url, follow=True),
    )

    def parse_item(self, response):
        item = FreexsItem()
        item['xsname'] = response.xpath('//div[@class="readout"]/h1/text()').extract_first()
        item['author'] = response.xpath('//div[@class="xiangxi"]/ul/li[1]/text()').extract_first().split('：')[-1]
        item['classes'] = response.xpath('//div[@class="xiangxi"]/ul/li[2]/text()').extract_first().split('：')[-1]
        item['last_update'] = response.xpath('//div[@class="xiangxi"]/ul/li[3]/text()').extract_first().split('：')[-1]
        item['status'] = response.xpath('//div[@class="xiangxi"]/ul/li[4]/text()').extract_first().split('：')[-1]
        item['all_click_num'] = response.xpath('//div[@class="xiangxi"]/ul/li[5]/text()').extract_first().split('：')[-1]
        item['week_click_num'] = response.xpath('//div[@class="xiangxi"]/ul/li[6]/text()').extract_first().split('：')[-1]
        item['month_click_num'] = response.xpath('//div[@class="xiangxi"]/ul/li[7]/text()').extract_first().split('：')[-1]
        item['collect_num'] = response.xpath('//div[@class="xiangxi"]/ul/li[8]/text()').extract_first().split('：')[-1]
        item['words'] = response.xpath('//div[@class="xiangxi"]/ul/li[9]/text()').extract_first().split('：')[-1].replace('字', '').strip()
        item['intro'] = response.xpath('//div[@class="xiangxi"]').xpath('string(.)').extract_first().split('书籍简介：')[-1].split('...')[0].strip()
        item['url'] = response.xpath('//div[@class="tu"]//a/@href').extract_first()
        item['image_url'] = response.xpath('//div[@class="tu"]//img/@src').extract_first()
        yield item

