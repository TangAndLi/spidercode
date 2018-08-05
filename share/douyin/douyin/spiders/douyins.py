# -*- coding: utf-8 -*-
import scrapy
import json
import jsonpath  # jsonpath是用来方便解析大点的json文件的，用法大家百度下，挺简单的

from douyin.items import DouyinItem


class DouyinsSpider(scrapy.Spider):
    name = 'douyins'
    # allowed_domains = ['a']
    # start_urls = ['http://a/']

    # start_urls列表实际是调用start_requests函数来处理每个url的，这里我们重写下自己的start_requests
    def start_requests(self):

        # 这是抖音的一个接口，每次请求这个url将会随机返回20条左右的抖音视频信息，count控制返回信息的多少，貌似25就是最大了。我们循环访问这个接口抓取数据
        
        url = "https://aweme.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=25&aid=1128&app_name=aweme"
        # 这里循环爬取10次，dont_filter设置为True，表示不过滤重复url。因为我们每次都是请求同一个url，不设置dont_filter默认位False，只能爬取一次
        for i in range(1, 10):
            yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())

        # 找出返回文件中所有aweme_list下的文件，也就是抖音的视频信息列表，然后循环解析每一个视频信息，video_info就是1个抖音视频的所有信息
        aweme_list = jsonpath.jsonpath(json_response, "$..aweme_list")
        for aweme in aweme_list:
            for video_info in aweme:

                # digg_count是点赞数，筛选出点赞数大于10w的视频进行解析
                digg_count = video_info["statistics"]["digg_count"]
                if int(digg_count) > 10 * 10000:

                    # 先找出aweme_id，aweme_id好像就是每个视频的唯一标识，我们这里要把aweme_id传入下面的comment_url这个接口爬取评论信息，
                    aweme_id = jsonpath.jsonpath(video_info, "$.statistics.aweme_id")
                    comment_url = "https://aweme.snssdk.com/aweme/v1/comment/list/?aweme_id={}&cursor=0&count=15&aid=1128".format(
                        aweme_id[0])

                    # 访问comment_url这个接口爬取每个视频的评论信息，调用parse_info函数解析，meta表示将video_info中的信息传递给parse_info函数
                    yield scrapy.Request(comment_url, callback=self.parse_info, meta={"video_info": video_info})
                else:
                    continue

    def parse_info(self, response):
        video_info = response.meta["video_info"]  # 接收上面parse函数传过来的video_info信息

        # 这里只找出评论内容和评论点赞数，以列表形式返回
        comment_json = json.loads(response.body_as_unicode())
        comments = comment_json["comments"]
        comment_list = []
        for comment in comments:
            text = jsonpath.jsonpath(comment, '$..text')  # 评论内容
            digg_count = jsonpath.jsonpath(comment, '$..digg_count')  # 评论点赞数
            comment_list.append(text + digg_count)  # text+digg_count是个列表，形如["小姐姐好漂亮",1888]

        # 将每个抖音视频所有的信息传给init_item
        item = self.init_item(video_info, comment_list)
        yield item

    def init_item(self, video_info, comment_list):
        item = DouyinItem()

        # 作者id
        item["author_user_id"] = video_info["author_user_id"]

        # 视频aweme_id
        item["aweme_id"] = video_info["statistics"]["aweme_id"]

        # 视频描述
        item["video_desc"] = video_info["desc"]

        # 点赞数
        item["digg_count"] = video_info["statistics"]["digg_count"]

        # 分享数
        item["share_count"] = video_info["statistics"]["share_count"]

        # 评论数
        item["comment_count"] = video_info["statistics"]["comment_count"]

        # 评论列表
        item["comment_list"] = comment_list

        # 分享链接
        item["share_url"] = video_info["share_url"]

        # 封面图链接列表，这里只取一个
        item["origin_cover"] = video_info["video"]["origin_cover"]["url_list"][0]

        # 视频播放地址列表,这里只取一个并去掉多余参数
        item["play_addr"] = video_info["video"]["play_addr"]["url_list"][0].split("&line")[0]

        # 视频下载地址列表，这里只取一个并去掉多余参数
        download_addr = video_info["video"]["download_addr"]["url_list"][0].split("&line")[0]
        item["download_addr"] = download_addr

        return item
