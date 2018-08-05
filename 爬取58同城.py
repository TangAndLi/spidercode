import csv
import urllib.request
import urllib.parse
from lxml import etree
import os

def get_html(req):
    response = urllib.request.urlopen(req)
    html_data = response.read().decode('utf-8')
    html_tree = etree.HTML(html_data)
    # 获取所有的房源信息
    li_list = html_tree.xpath('.//div[@class="listBox"]/ul/li')
    li_list.pop()

    for li_data in li_list:
        # 标题
        # dict = {}
        home_list = []
        home_list.append(li_data.xpath('.//h2/a')[0].text.strip())
        #房间
        home_list.append(li_data.xpath('.//div/p[1]')[0].text.replace('\xa0',''))
        # 地址
        home_list.append(li_data.xpath('.//p/a')[0].text.strip())
        # 联系人
        if li_data.xpath('.//div[@class="jjr"]/span/span[2]'):
             home_list.append(li_data.xpath('.//div[@class="jjr"]/span/span[2]')[0].text.strip())
        else:
             home_list.append('None')
        # 价格
        home_list.append(li_data.xpath('.//div/b')[0].text)
        # home_list.append(dict)
            # save_homeData(home_list)
        # for list in home_list:
        #     print(list)

    # 列表写入
    # headers = ['title','room','address','person','price']
        with open('./home_data.csv','a+',newline='',encoding = 'utf-8') as fp:
            f_csv = csv.writer(fp)
            f_csv.writerow(home_list)

    # 字典写入
        # for list in home_list:
        #     f_csv.writerow([list['title'],list['room'],list['address'],list['person'],list['price']])

# def save_homeData(home_list):
#     with open('./home_data.csv','a+',newline='',encoding = 'utf-8') as fp:
#         f_csv = csv.writer(fp)
#         f_csv.writerow(headers)
#         f_csv.writerows(home_list)

def main():
    url = 'http://sz.58.com/chuzu/pn'
    headers = {
        'Accept': ' application/json, text/javascript, */*; q=0.01',
        'Accept-Language': ' zh-CN,zh;q=0.9',
        'Content-Type': ' text/plain',
        'Origin': ' http://sz.58.com',
        'Proxy-Connection': ' keep-alive',
        'Referer': ' http://sz.58.com/chuzu/pn2/?PGTID=0d3090a7-0000-46f9-aa8b-1308e899621d&ClickID=2',
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    start_page = int(input('请输入你要爬取的起始页码:'))
    end_page = int(input('请输入结束页码:'))

    for page in range(start_page, end_page+1):

        url = url + str(page)
        print(url)
        req = urllib.request.Request(url = url, headers = headers)
        # handler = urllib.request.ProxyHandler({'http': '180.118.243.89:8123'})

        # 创建opener
        # opener = urllib.request.build_opener(handler)
        get_html(req)
        # print(content)


if __name__ == '__main__':
    main()







