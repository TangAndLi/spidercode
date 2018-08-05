# -*- coding: utf-8 -*-
import json
import scrapy
from douyin.items import DouyinVideoItem, DouyinUserItem
from scrapy_redis.spiders import RedisCrawlSpider


class DySpider(RedisCrawlSpider):
    name = 'dy_redis'
    redis_key = 'dy_redis:start_urls'
    allowed_domains = ['aweme.snssdk.com']
    # start_urls = ['https://aweme.snssdk.com/aweme/v1/aweme/favorite/?aid=1128&count=1000&user_id=95077716507']

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(DySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # video_info = response.meta.get('video_item')
        # user_item = response.meta.get('user_item')
        video_json = json.loads(response.text)
        for video_info in video_json['aweme_list']:
            video_ite = self.get_video(video_info)
            user_ite = self.get_user(video_info['author'])
            user_ite['author_user_id'] = video_info["author_user_id"]
            url = 'https://aweme.snssdk.com/aweme/v1/aweme/favorite/?aid=1128&count=10000&user_id=%s'% (user_ite['author_user_id'])
            # print(url)
            # yield scrapy.Request(url, callback=self.parse, dont_filter=True)
            yield scrapy.Request(url, callback=self.parse)
            yield video_ite
            yield user_ite

    def get_video(self, video_info):
        video_item = DouyinVideoItem()
        video_item["author_user_id"] = str(video_info["author_user_id"])             # 作者id
        video_item["video_desc"] = video_info["desc"]              # 视频描述
        video_item["aweme_id"] = str(video_info["statistics"]["aweme_id"])            # 视频aweme_id
        video_item["digg_count"] = str(video_info["statistics"]["digg_count"])            # 点赞数
        video_item["share_count"] = str(video_info["statistics"]["share_count"])            # 分享数
        video_item["comment_count"] = str(video_info["statistics"]["comment_count"])            # 评论数
        video_item["share_url"] = video_info["share_url"]                            # 分享链接
        video_item["origin_cover"] = video_info["video"]["origin_cover"]["url_list"][0]            # 封面图链接列表，这里只取一个
        video_item["play_addr"] = video_info["video"]["play_addr"]["url_list"][0].split("&line")[0]            # 视频播放地址列表,这里只取一个并去掉多余参数
        download_addr = video_info["video"]["download_addr"]["url_list"][0].split("&line")[0]            # 视频下载地址列表，这里只取一个并去掉多余参数
        video_item["download_addr"] = download_addr
        return video_item

    def get_user(self, author):
            user_item = DouyinUserItem()
            user_item['uid'] = author['uid']
            user_item['bind_phone'] = author['bind_phone']
            user_item['create_time'] = author['create_time']
            user_item['constellation'] = author['constellation']       # 星座
            user_item['avatar_medium'] = author['avatar_medium']['url_list'][0]     # 头像地址之一
            user_item['follow_status'] = author['follow_status']    # 粉丝
            user_item['follower_status'] = author['follower_status']
            user_item['school_name'] = author['school_name']    # 学校名
            user_item['school_type'] = author['school_type']    # 学校类型
            user_item['birthday'] = author['birthday']     # 生日
            user_item['nickname'] = author['nickname']      # 用户昵称
            user_item['signature'] = author['signature']    # 签名
            user_item['region'] = author['region']
            user_item['gender'] = author['gender']
            user_item['unique_id'] = author['unique_id']
            return user_item

