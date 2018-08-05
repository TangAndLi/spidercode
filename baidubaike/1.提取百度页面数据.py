#coding:utf-8
import requests
import urllib.request
def download(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' #模拟浏览器
    #headers = {'User-Agent': user_agent}
    response=requests.get(url)
    if response.status_code==200:
        response.encoding="utf-8" #设置编码
        return response.text
    else:
        return  None

#print (download("https://baike.baidu.com/item/Python/407313"))
print(urllib.request.urlopen("http://baike.baidu.com/item/Python/407313").read().decode("utf-8"))


