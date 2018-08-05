# -*- coding: utf-8 -*-
import scrapy
from ..items import XpcprojectItem

class SecondSpider(scrapy.Spider):
    name = 'second'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0']

    def parse ( self,response ):
        video_li = response.xpath('//div[@class="channel-con"]/ul//li')
        # print(len(video_li))
        for video_li in video_li:
            # 视频id
            data_articleid = video_li.xpath('./@data-articleid').extract_first()
            # 视频
            data_videourl = video_li.xpath('./@data-videourl').extract_first()
            url = 'http://www.xinpianchang.com/a{}?from={}'.format(data_articleid,data_videourl)
            # print(url)

            yield scrapy.Request(url,callback = self.video_parse)

    def video_parse ( self,response ):
        # print(response.text)
        items = XpcprojectItem()
        items['title'] = response.xpath('.//video[@id="xpc_video"]/@alt').extract_first()
        items['video'] = 'https:' + response.xpath('.//video[@id="xpc_video"]/@src').extract_first()
        items['video_format'] = response.xpath('.//video[@id="xpc_video"]/source/@type').extract_first()
        categorys = response.xpath(
            './/div[@class="filmplay-intro fs_12 fw_300 c_b_9"]/span[@class="cate v-center"]/a/text()').extract()
        strcategorys = ''
        for i in categorys:
            strcategorys += i.strip('\n').strip('\t') + '-'
        items['category'] = strcategorys
        # 创建时间
        items['created_at'] = response.xpath(
            './/div[@class="filmplay-intro fs_12 fw_300 c_b_9"]/span[@class="update-time v-center"]/i/text()').extract_first()
        yield items


