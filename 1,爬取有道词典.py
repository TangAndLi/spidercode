# import urllib.request
# import urllib.parse
import random
import time
import hashlib
from urllib import request,parse
import urllib.error

def send_response(req):
    try:
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)


# def post_request(url,data,header):
    # data = urllib.parse.urlencode(data).encode('utf-8')
    # handler = urllib.request.HTTPHandler()
    # opener = urllib.request.build_opener(handler)
    # req = urllib.request.Request(url = url,headers = header,data = data)
    # # send_response(req)
    # response = opener.open(req).read().decode('utf-8')
    # # print(response.read().decode('utf-8'))
    # return response


def main():
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    header = {
        'Host':'fanyi.youdao.com',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Origin':'http://fanyi.youdao.com',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer':'http://fanyi.youdao.com/',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':' OUTFOX_SEARCH_USER_ID=-305723138@10.169.0.84; JSESSIONID=aaaLlyOIHJNx1fcAGP6ow; OUTFOX_SEARCH_USER_ID_NCOO=2003795746.2558346; ___rl__test__cookies=1527851295588',
    }

    word = input('请输入查询的单词:')
    salt = str(int(time.time() * 1000) + random.randint(1,10))
    # sign = hashlib.md5()
    # words = "fanyideskweb" + word + salt + "ebSeFb%=XZ%T[KZ)c(sy!"
    # sign.update(words.encode('utf-8'))
    # sign.hexdigest()
    sign = hashlib.md5(("fanyideskweb" + word + salt + "ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8')).hexdigest()

    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false',
    }

    # return post_request(url,data,header)
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url = url,headers = header,data=data)
    send_response(req)


if __name__ == '__main__':
    # req = main()
    main()
    # print(req)







