# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FreexsItem(scrapy.Item):
    # define the fields for your item here like:
    xsname = scrapy.Field()
    author = scrapy.Field()
    classes = scrapy.Field()
    last_update = scrapy.Field()
    status = scrapy.Field()
    all_click_num = scrapy.Field()
    week_click_num = scrapy.Field()
    month_click_num = scrapy.Field()
    collect_num = scrapy.Field()
    words = scrapy.Field()
    intro = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()

