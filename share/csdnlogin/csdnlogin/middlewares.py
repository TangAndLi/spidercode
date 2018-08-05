# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver  # 代表模拟浏览器
from scrapy.http import HtmlResponse  # 网页信息
import time,os
import requests


class LoginMiddleware(object):
    # 替换掉原来的函数，process_request
    def process_request(self, request, spider):
        if spider.name == "csdn":  # 指定仅仅处理这个名称的爬虫
            if request.url.find("login") != -1:  # 判断是否登陆页面

                spider.browser = webdriver.Chrome()  # 创建一个浏览器
                spider.browser.get(request.url)  # 爬虫访问链接
                time.sleep(5)
                print("login访问", request.url)

                spider.browser.find_element_by_link_text("账号登录").click()
                time.sleep(1)
                username = spider.browser.find_element_by_id("username")
                password = spider.browser.find_element_by_id("password")
                time.sleep(1)
                username.send_keys("15323844594")  # 账户
                time.sleep(2)
                PASSWORD = os.getenv('PASSWORD') or '123456'
                password.send_keys(PASSWORD)  # 密码
                time.sleep(3)
                click = spider.browser.find_element_by_class_name("logging")
                click.click()
                time.sleep(8)
                spider.cookies = spider.browser.get_cookies()  # 抓取全部的cookie
                # spider.browser.close()

                return HtmlResponse(url=spider.browser.current_url,  # 当前连接
                                    body=spider.browser.page_source,  # 源代码
                                    encoding="utf-8")  # 返回页面信息
            else:
                # spider.browser.get(request.url)
                # request.访问，调用selenium cookie
                # request模拟访问。统一selenium，慢，request,不能执行js
                print("request  访问")
                req = requests.session()  # 会话
                for cookie in spider.cookies:
                    req.cookies.set(cookie['name'], cookie["value"])
                req.headers.clear()  # 清空头
                new_page = req.get(request.url)
                # print("---------------------")
                # print(request.url)
                # print("---------------------")
                # print(new_page.text)
                # print("---------------------")
                # 页面
                time.sleep(3)
                return HtmlResponse(url=request.url,  # 当前连接
                                    body=new_page.text,  # 源代码
                                    encoding="utf-8")  # 返回页面信息


class CsdnloginSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
