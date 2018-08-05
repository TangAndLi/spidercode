# -*- coding: utf-8 -*-
import urllib
import scrapy
from ..items import XpcprojectItem

class ThirdSpider(scrapy.Spider):
    name = 'third'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0']

    def parse( self,response ):
        # table_list = response.xpath('//div[@class="channel-con"]/ul/li')
        table_list = response.xpath('//div[@class="channel-con"]/ul/li')
        print(len(table_list))
        for table in table_list:
            items = XpcprojectItem()

            image_url1 = table.xpath('.//a[@class="video-cover"]/img/@_src').extract_first()
            items['image_url1'] = image_url1

            # items['image_url'] = table.xpath('.//a[@class="video-cover"]/img/@src').extract_first()
            video_name1 = table.xpath('.//div[@class="video-con-top"]/a/p/text()').extract_first()
            items['video_name1'] = video_name1
            # items['video_author']= table.xpath('.//div[@class="user-info"]//span[2]/text()').extract_first()
            items['video_author1'] = table.xpath('.//div[@class="user-info"]//span[2]/text()').extract_first().strip(
                '\n').strip('\t')
            items['release_date1'] = table.xpath('//div[@class="video-hover-con"]/p/text()').extract_first()
            try:
                urllib.request.urlretrieve(image_url1,filename ='./img' + video_name1+".jpg")
            except:
                pass
            yield items

        for i in range(1,5):
            new_url =  'http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-%d'% i
            yield scrapy.Request(new_url,callback = self.parse)



