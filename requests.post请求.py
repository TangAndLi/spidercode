


import requests

url = 'http://fanyi.baidu.com/sug'

data = {
    'kw': 'fuck'
}

r = requests.post(url=url ,data=data)
print(r.text)
print(r.json())



