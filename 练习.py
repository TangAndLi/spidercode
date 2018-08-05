
import threading
import random
import time
import queue
import requests
from lxml import etree
import json
from urllib.error import URLError

# 创建队列
spider_queue = queue.Queue()

# 创建解析队列
parse_queue = queue.Queue()

# 解析退出标志
parse_exit_flag = False

# 锁
lock = threading.Lock()

UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
]


# 创建队列线程
class SpiderThread(threading.Thread):
    def __init__(self,s_id, s_queue, p_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = s_id
        self.spider_queue = s_queue
        self.parse_queue = p_queue

    def run(self):
        while True:
            time.sleep(3)
            # 如果队列为空 结束循环
            if self.spider_queue.empty():
                break
            url = self.spider_queue.get(block = False)
            try:
                response = requests.get(url=url, headers={'User-Agent': random.choice(UserAgent_List)} )

                # 加入解析队列
                self.parse_queue.put(response.text)

                print('%d 当前程序爬取数据%s'%(self.id, url))

            except URLError as e:
                print(e,'xxxxx')
            finally:
                self.spider_queue.task_done()


class ParseThread(threading.Thread):
    def __init__(self, p_id, p_queue, fp, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.id = p_id
        self.parse_queue = p_queue
        self.fp = fp

    def run(self):
        while True:
            global parse_exit_flag
            if parse_exit_flag:
                break
            try:
                data = self.parse_queue.get(block =False)
                print('1111')
                self.parse(data)
                print('11')
                print('%d 数据解析成功'% self.id)

                self.parse_queue.task_done()
            except Exception:
                pass

    # def parse(self,data):
    #     html = etree.HTML(data)
    #     div_list = html.xpath('//div[contains(@id, "qiushi_tag_')
    #     items = []
    #     for div in div_list:
    #         head_shot = div.xpath('.//img/@src')[0]
    #         name = div.xpath('.//h2/text()')[0].strip('\n')
    #         content = div.xpath('.//span/text()')[0].strip('\n')
    #         item = {
    #             'head_shot': head_shot,
    #             'name': name,
    #             'content': content
    #         }
    #         items.append(item)
    #
    #     with lock:
    #         self.fp.write(json.dumps(items,ensure_ascii = False) + '\n')
    def parse ( self,data ):
        # 解析页面
        # 创建etree
        html = etree.HTML(data)
        # 获取页面内容列表
        div_list = html.xpath('//div[contains(@id, "qiushi_tag_")]')
        # print(div_list)
        items = []
        for div in div_list:
            head_shot = div.xpath('.//img/@src')[0]
            name = div.xpath('.//h2/text()')[0].strip('\n')
            content = div.xpath('.//span/text()')[0].strip('\n')
            item = {
                'head_shot':head_shot,
                'name':name,
                'content':content
            }
            items.append(item)
        with lock:
            self.fp.write(json.dumps(items,ensure_ascii = False) + '\n')


def main():
    base_url = 'https://www.qiushibaike.com/8hr/page/%d/'

    for i in range(1, 11):
        url = base_url % i
        spider_queue.put(url)
        # print(url)

    # 创建Spider线程
    for i in range(4):
        SpiderThread(i, spider_queue, parse_queue,).start()

    fp = open('./spider.txt' ,'w', encoding = 'utf-8')

    for i in range(4):
        ParseThread(i, parse_queue, fp).start()

    spider_queue.join()
    parse_queue.join()
    print('1111111')
    global parse_exit_flag
    parse_exit_flag = True

    fp.close()


if __name__ == '__main__':
    main()







