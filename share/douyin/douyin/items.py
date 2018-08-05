# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_user_id = scrapy.Field()
    video_desc = scrapy.Field()
    aweme_id = scrapy.Field()
    play_addr = scrapy.Field()
    download_addr = scrapy.Field()
    origin_cover = scrapy.Field()
    comment_info = scrapy.Field()
    comment_list = scrapy.Field()
    digg_count = scrapy.Field()
    comment_count = scrapy.Field()
    share_count = scrapy.Field()
    share_url = scrapy.Field()
