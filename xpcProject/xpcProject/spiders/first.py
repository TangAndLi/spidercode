# -*- coding: utf-8 -*-
import scrapy
from ..items import XpcprojectItem

class FirstPySpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0']

    def parse(self, response):
        # table_list = response.xpath('//div[@class="channel-con"]/ul/li')
        table_list = response.xpath('//div[@class="channel-con"]/ul/li')
        print(len(table_list))
        for table in table_list:
            items = XpcprojectItem()
            items['image_url'] = table.xpath('.//a[@class="video-cover"]/img/@_src').extract_first()
            # 视频名称
            # items['image_url'] = table.xpath('.//a[@class="video-cover"]/img/@src').extract_first()
            items['video_name'] = table.xpath('.//div[@class="video-con-top"]/a/p/text()').extract_first()
            # items['video_author']= table.xpath('.//div[@class="user-info"]//span[2]/text()').extract_first()
            items['video_author'] = table.xpath('.//div[@class="user-info"]//span[2]/text()').extract_first().strip(
                '\n').strip('\t')
            items['release_date']= table.xpath('//div[@class="video-hover-con"]/p/text()').extract_first()
            yield items


