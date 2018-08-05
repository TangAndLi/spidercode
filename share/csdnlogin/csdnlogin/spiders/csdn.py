# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.http import FormRequest  # 抓取表单，返回表单数据
from selenium import webdriver  # 调用浏览器
from scrapy.xlib.pydispatch import dispatcher  # 观察者
from scrapy import signals  # 信号

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://passport.csdn.net/account/login',
                  "https://blog.csdn.net/hellocsz/article/details/80708996"]

    # 初始化
    def __init__(self):
        self.browser = None
        self.cookies = None
        # 传递给父类
        super(CsdnSpider, self).__init__()
        # dispatcher.connect(self.spider_closed,signals.spider_closed)#爬虫关闭通过信号调用我们自己的函数

    def spider_closed(self, response):  # 爬虫关闭
        print("爬虫关闭")
        self.browser.close()  # 关闭浏览器

    def parse(self, response):
        # 打印链接，打印网页源代码
        path = os.path.join(os.getcwd(), os.path.basename(response.url) + 'login.html')
        response.body.decode("utf-8", "ignore")
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(response.text)
