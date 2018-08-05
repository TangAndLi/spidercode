
import requests

url = 'http://www.baidu.com/s'

data = {
    'wd':'ip'
}

proxies = {
    'http': '115.153.173.238:61234'
}

r = requests.get(url = url,params = data)

r.encoding ='utf-8'

with open('./baidup.html','w',encoding = 'utf-8') as fp:
    fp.write(r.text)
































