
import requests
from lxml import etree
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re


url = 'https://s.taobao.com/list?%27+%5C+%27spm=a21bo.2017.201867-links-0.3.5af911d9rRNGOl&q=%E5%A4%8F%E4%B8%8A%E6%96%B0&' \
      'cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=0'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response = requests.get(url = url,headers=header)
# response.encoding='utf-8'
# taoBao_json = json.load(response.text)
# print(response.text)
pic_url = re.compile('"pic_url":(.*?),',re.S)
title = re.compile('"raw_title":"([a-zA-Z0-9\u4e00-\u9fa5 +*!]+)"',re.S)
detail_url = re.compile('"detail_url":(.*?),',re.S)
price =re.compile('"view_price":(.*?),',re.S)
fee = re.compile('"view_fee":(.*?),',re.S)
loc = re.compile('"item_loc":(.*?),',re.S)
sales = re.compile('"view_sales":(.*?),',re.S)
count = re.compile('"comment_count":(.*?),',re.S)
url_list = re.findall(pic_url,response.text)
title_list = re.findall(title,response.text)
detail_list= re.findall(detail_url,response.text)
price_list = re.findall(price,response.text)
fee_list = re.findall(fee,response.text)

print(len(url_list),len(title_list),len(detail_list),len(price_list),len(fee_list))
for i in range(50):
    print(url_list[i],title_list[i],detail_list[i],price_list[i],fee_list[i])
# print(url_list,title_list,detail_list,price_list,fee_list)


# "pic_url":"//g-search2.alicdn.com/img/bao/uploaded/i4/i1/907361441/TB2IhE6siOYBuNjSsD4XXbSkFXa_!!907361441.jpg",


# html_etree = etree.tostring(html).decode('utf-8')
# print(taoBao_json)
# img = html.xpath('//div[@class="items"]/div//div[@class="pic"]/a/img/@src')
# print(img)























# fp = open('./taobao.html','w',encoding ='utf-8')
# fp.write(response.text)
# fp.close()

# print(response.text)














