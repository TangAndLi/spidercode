
#coding:utf-8
import requests

url = 'https://www.baidu.com'

r = requests.get(url= url)

# 转换编码
r.encoding = 'utf-8'

# print(r.text) # 查看网页内容

# 查看编码
# print(r.encoding) #utf-8

# print(r.content)  # 查看内容 一堆乱码

# 状态码
print(r.status_code)  #200

with open('./58.html' ,'w',encoding='utf-8') as fp:
    fp.write(r.text)


