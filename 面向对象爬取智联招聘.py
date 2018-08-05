
import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request


class ZhiLian(object):
    def __init__(self,url,start_page,end_page,area,gangwei):

        self.url = url
        self.start_page = start_page
        self.end_page = end_page
        self.area = area
        self.gangwei = gangwei
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
        }

    def download(self,request):
        html = request.text.encode('utf-8')
        soup = BeautifulSoup(html,'lxml')
        # print(soup)
        table_list = soup.select('#newlist_list_content_table > table')[1:]
        for table in table_list:
            # 获取职位名称：
            zwmc = table.select('.zwmc')[0].select('a')[0].get_text()
            zwmc.strip() # 去除空格
            gsmc = table.select('.gsmc > a')[0].get_text().strip()
            salary = table.select('.zwyx')[0].get_text()
            print(gsmc)

    def handler_url(self,page):
        data = {
            'ji': self.area,
            'kw': self.gangwei,
            'p': page,
        }
        data = urllib.parse.urlencode(data)
        url = self.url + data
        request = requests.get(url = url, headers =self.headers)
        return request

    def start(self):
        for page in range(self.start_page,self.end_page+1):
            requests = self.handler_url(page)
            self.download(requests)

def main():
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
    start_page = int(input('请输入:'))
    end_page = int(input('请输入:'))
    area = input('请输入地区:')
    gangwei = input('请输入岗位:')

    obj = ZhiLian(url, start_page, end_page, area, gangwei)
    obj.start()


if __name__ == '__main__':
    main()



    

























