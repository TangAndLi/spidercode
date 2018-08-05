# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinVideoItem(scrapy.Item):
    # define the fields for your item here like:
    author_user_id = scrapy.Field()
    video_desc = scrapy.Field()
    aweme_id = scrapy.Field()
    play_addr = scrapy.Field()
    download_addr = scrapy.Field()
    origin_cover = scrapy.Field()
    digg_count = scrapy.Field()
    comment_count = scrapy.Field()
    share_count = scrapy.Field()
    share_url = scrapy.Field()


class DouyinUserItem(scrapy.Item):
    author_user_id = scrapy.Field()
    uid = scrapy.Field()
    bind_phone = scrapy.Field()
    create_time = scrapy.Field()
    constellation = scrapy.Field()
    avatar_medium = scrapy.Field()   # 头像地址之一
    follow_status = scrapy.Field()  # 粉丝
    follower_status = scrapy.Field()
    school_name = scrapy.Field()    # 学校名
    school_type = scrapy.Field()  # 学校类型
    birthday = scrapy.Field()  # 生日
    nickname = scrapy.Field()  # 用户昵称
    signature = scrapy.Field()  # 签名
    region = scrapy.Field()
    gender = scrapy.Field()
    unique_id = scrapy.Field()
