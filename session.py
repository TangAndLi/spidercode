
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

post_url = 'https://passport.weibo.cn/sso/login'
data = {
    'username': '18676689715',
    'password': 'xuke666',
    'savestate': '1',
    'r': 'http://weibo.cn/',
    'ec': '0',
    'pagerefer': '',
    'entry': 'mweibo',
    'wentry': '',
    'loginfrom': '',
    'client_id': '',
    'code': '',
    'qq': '',
    'mainpageflag': '1',
    'hff': '',
    'hfp': '',
}
headers = {
    # 'Host': 'passport.weibo.cn',
    'Connection': 'keep-alive',
    'Origin': 'https://passport.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

session = requests.Session()

r = session.post(url = post_url ,data =data,headers=headers )
# print(r.json())



url = 'https://weibo.cn/2952685222/info'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

req = session.get(url=url, headers=headers)
with open('./session.html', 'w', encoding = 'utf-8') as fp:
    fp.write(req.text)







