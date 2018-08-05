import time
import urllib.request
import requests
import urllib.parse


def handler_url(page):
    time.sleep(2)
    sum = str(int(time.time()*1000)) + '_' + str(73+((page-1) * 14))
    back = 'jsonp'+str(74+((page-1) * 14))
    # url = 'https://v.taobao.com/micromission/req/selectCreatorV3.do?cateType=704&currentPage%d&_ksTS=%s&callback=%s&&_output_charset=UTF-8&_input_charset=UTF-8'%(page,sum,back)
    url = 'https://v.taobao.com/v/content/live?'
    # url = 'https://v.taobao.com/micromission/req/selectCreatorV3.do?'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    }
    # print(sum,back)
    data = {
        'cateType': '704',
        'currentPage': page,
        '_ksTS': sum,
        'callback': back,
        '_output_charset': 'UTF-8',
        '_input_charset':'UTF-8',
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    print(url)
    request = urllib.request.Request(url = url, headers = headers)
    response = urllib.request.urlopen(request)
    # print(response.read().decode('utf-8'))
    # request = requests.get(url,data = data, headers = headers)
    # print(request.text)
    with open('./taonvlang.html','w', encoding = 'utf-8')as fp:
        fp.write(response.read().decode('utf-8'))


def main():
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    for page in range(start_page,end_page+1):
         handler_url(page)
        # print(request)


if __name__ == '__main__':
    main()














