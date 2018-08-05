# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XpcprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url = scrapy.Field()
    video_name = scrapy.Field()
    video_author =scrapy.Field()
    release_date = scrapy.Field()

  # 第二题
    title = scrapy.Field()
    video = scrapy.Field()
    video_format = scrapy.Field()
    category = scrapy.Field()
    created_at = scrapy.Field()
    #
    image_url1 = scrapy.Field()
    video_name1 = scrapy.Field()
    video_author1 =scrapy.Field()
    release_date1= scrapy.Field()
