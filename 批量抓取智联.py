
import json

import requests
from bs4 import BeautifulSoup


def handler_url(base_url,page):
    url = base_url % page
    return url

def main():
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&sg=492ea9f658fc4b148522d926e6717ce9&p=%d'
    start_page = int(input('请输入起始页面:'))
    end_page = int(input('请输入结束页:'))
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    }

    for page in range(start_page,end_page+1):
        # 拼接url
        url = handler_url(base_url,page)
        # 发送http请求
        r = requests.get(url = url,headers = headers)
        # 创建bs4 对象
        soup = BeautifulSoup(r.text,'lxml')
        # 找到所有的table
        table_list = soup.select('#newlist_list_content_table > table')[1:]
        # print(table_list)


if __name__ == '__main__':
    main()


























