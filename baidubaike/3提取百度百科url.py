#coding:utf-8
import requests
import re
import urlparse
from bs4 import BeautifulSoup

def download(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' #模拟浏览器
    headers = {'User-Agent': user_agent}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        response.encoding="utf-8" #设置编码
        return response.text
    else:
        return  None

def  gettitle(pagedata):
    soup=BeautifulSoup(pagedata,"html.parser") #解析
    list1= soup.find_all("h1")
    list2=soup.find_all("h2")
    if len(list1)!=0  and  len(list2)!=0:
        return (list1[0].text,list2[0].text)
    elif  len(list1)!=0 and  len(list2)==0:
        return  list1[0].text
    else:
        return None

def  getcontent(pagedata):
    soup=BeautifulSoup(pagedata,"html.parser") #解析
    summary= soup.find_all("div",class_="lemma-summary")
    if  len(summary)!=0:
        return  summary[0].get_text()
    else:
        return None

def  geturllist(pagedata):
    urllist=set() #集合
    soup = BeautifulSoup(pagedata, "html.parser")  # 解析
    links=soup.find_all("a",href=re.compile(r"/item/.*"))
    for  link  in links:
        url="https://baike.baidu.com"
        url+=link["href"]
        urllist.add(url) #加入集合

    return urllist


pagedata= download("https://baike.baidu.com/item/Python/407313")
print  (geturllist(pagedata))
#print gettitle(pagedata)[0],gettitle(pagedata)[1]
