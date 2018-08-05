

from urllib import request,parse

url = 'http://fanyi.baidu.com/sug '

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

word = input('请输入查询的单词:')

data = {
    'kw': word
}

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url = url,data = data,headers = headers)

response = request.urlopen(req)
# print(response.read().decode('utf-8'))

json_string = response.read().decode('utf-8')
# print(json_string)
import json

# 转成json字符串转换成json对象
json_obj = json.loads(json_string)
print(json_obj)

# json 对象转换成普通字符串
json_string = json.dumps(json_obj,ensure_ascii = False)
print(json_string)

# 二进制下无法修改编码模式  去掉b
with open('ret.json','w',encoding = 'utf-8') as file:
    file.write(json_string)









