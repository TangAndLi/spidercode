
import urllib.request
import queue
import threading

spider_queue  = queue.Queue()
parse_queue = queue.Queue()


def request_spider(url,headers):
    # return url
    header = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(header)
    #get 请求
    request = urllib.request.Request(url = url, headers = headers)
    response = opener.open(request)
    html = response.read().decode('utf-8')
    return html

# print(request_spider(5))


if __name__ == '__main__':
    header = {
        'authority':' s.taobao.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 't=10589bb513e965a18aaea60fb746b92f; cna=LmZ3Ex4aNGcCARsmLBCepJdN; miid=801110790606853099; tracknick=summer%5Cu4E00%5Cu62B9%5Cu9633%5Cu5149; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; thw=cn; enc=cSzITUtJALCxUKqCZ%2F8sCvR056oaSwxqoInzYXYV8tUb0lkds8MrcWOkvh5j4sV6eoWLFmFkD2bluYROkmXWLQ%3D%3D; UM_distinctid=163d372d4c7471-0dc6d172f9fc6b-5b163f13-100200-163d372d4c89c4; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; v=0; cookie2=3bbbaae843a7c7d594bb9d831d1c3c0a; _tb_token_=e93e3663b1a1e; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=BB29836A117B98783A7770EE678209F1; isg=BJmZtFWCJmxiuPqW7Y1ZLKkCqIWzjpLkgTnjr7tOFUA_wrlUA3adqAfzwMYR-iUQ',
        'upgrade-insecure-requests':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    for i in range(1,101):
        url = 'https://s.taobao.com/list?' \
             'spm=a21bo.2017.201867-links-0.3.5af911d9rRNGOl&q=%E5%A4%8F%E4%B8%8A%E6%96%B0&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao' \
            '&bcoffset=12&s=' + str((i * 60) - 60)
        spider_queue.put(url)


    print(request_spider(10,header))










