import time, random, hashlib
import urllib.request
import urllib.parse



def post_request(url,data,header):
    data = urllib.parse.urlencode(data).encode('utf-8')
    # word = input()
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    request =urllib.request.Request(url=url, data=data, headers=header)
    res = opener.open(request).read().decode("utf-8")
    # print(res)
    return res


def main():
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    header = {
        'Host': 'fanyi.youdao.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://fanyi.youdao.com',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://fanyi.youdao.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': ' OUTFOX_SEARCH_USER_ID=-305723138@10.169.0.84; JSESSIONID=aaaLlyOIHJNx1fcAGP6ow; OUTFOX_SEARCH_USER_ID_NCOO=2003795746.2558346; ___rl__test__cookies=1527851295588',
    }
    word = input('请输入你要翻译的内容：')
    salt = str(int(time.time() * 1000) + random.randint(1, 10))
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
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }

    return post_request(url,data,header)


if __name__ == '__main__':
    content = main()
    print(content)