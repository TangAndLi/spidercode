import csv
import os
import time
from multiprocessing import Pool, Queue
from threading import Thread, Lock, BoundedSemaphore
from lxml import etree
import urllib.request

# 线程锁
lock = Lock()
# 线控制程并发数为8
sema =BoundedSemaphore(8)

# 保存信息
def save_info(li):
    # 控制线程并发数
    global sema
    with sema:
        info_list =[]
        info_list.append(li.xpath('.//@lazy_src')[0].strip())   # img_url
        info_list.append(li.xpath('.//h2/a')[0].text.strip())   # title
        info_list.append(li.xpath('.//div[@class ="money"]/b')[0].text.strip())  # money
        info_list.append(li.xpath('.//p[@class="room"]')[0].text.strip())   # size
        info_list.append(li.xpath('.//div[@class="sendTime"]')[0].text.strip()) # 发布时间
        # 地址
        addr1 = li.xpath('.//p[@class="add"]/a[1]')[0].text
        addr2 = li.xpath('.//p[@class="add"]/a[last()]')[0].text
        addr3 = li.xpath('.//p[@class="add"]')[0].text
        info_list.append((addr1 + addr2 + addr3).strip())

        # 写入文件加线程锁
        global lock
        with lock:
            # 保存单条信息
            with open('58.csv', 'a+', newline= '', encoding='utf-8') as fp:
                write = csv.writer(fp)
                write.writerow(info_list)


# xpath处理页面，获取信息
def do_xpath(response,page):
    html_etree = etree.HTML(response)
    # xpath获取所有目标信息所在的li标签
    li_list = html_etree.xpath('//ul[@class="listUl"]/li')
    # 去除分页的li标签
    li_list.pop()
    # 为每一条信息的处理开一个线程
    for li in li_list:
        Thread(target=save_info,args=(li,)).start()
    return {'len':len(li_list), 'page':page, 'pid':os.getpid()}


# 构建请求，获得响应的页面
def request_url(page,header):
    print('<进程%s>开始处理第%s页'%(os.getpid(),page))
    url = 'http://sz.58.com/chuzu/pn' + str(page) +'/'
    request = urllib.request.Request(url=url,headers=header)
    # handler = urllib.request.HTTPHandler()
    # opener = urllib.request.build_opener(handler)
    # response = opener.open(request).read().decode('utf-8')
    response = urllib.request.urlopen(request).read().decode('utf-8')
    # xpath处理获取目标信息
    return do_xpath(response,page)


# 回调函数
def back_func(res):
    print('<进程%s>处理第%s页完成，获取%d条信息'%(res['pid'],res['page'],res['len']))

def main():
    star_page = int(input('开始页：'))
    end_page = int(input('结束页：'))
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'f=n; userid360_xml=D41C39E975D64CEE7BEF8B52A1F231E2; time_create=1530524791261; 58home=sz; f=n; id58=c5/njVsSZ1o+vnUJA/6+Ag==; city=sz; 58tj_uuid=95b24bfd-aaf9-4fe5-8838-5eba416f4477; new_uv=1; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DMbUGewaJanwTs_PeoasMBgcUzuHzMWALHm2wUlvKGSi%2526wd%253D%2526eqid%253Deb5bbf6a0001ba73000000065b126756; als=0; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; commontopbar_ipcity=sz%7C%E6%B7%B1%E5%9C%B3%7C0; commontopbar_myfeet_tooltip=end; xxzl_deviceid=CnaAW3ctNgv9kXJYL8azWMoXe%2FlbxBrqC7GC7sGXF1CSGsdi9bHvG%2FjH2rac5gD5; wmda_uuid=276210f3320c9b7349412e991946590d; wmda_new_uuid=1; wmda_session_id_2385390625025=1527932774706-6f03b5f8-7edd-74d7; wmda_visited_projects=%3B2385390625025; new_session=0',
        'Host': 'sz.58.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    # 多进程处理响应页面
    pp = Pool(8)
    # res_list接受每个进程处理的信息数
    res_list,num =[],0
    # 为每个页面的处理操作开一个进程
    for page in range(star_page, end_page+1):
        time.sleep(5)
        res = pp.apply_async(request_url, args=(page,header,), callback=back_func)
        res_list.append(res)
    pp.close()
    pp.join()
    for i in res_list:
        try:
            num += i.get()['len']
        except:
           pass
    print('共获取信息%s条'% num)


if __name__ == '__main__':
    time1 = time.clock()
    main()
    print('耗时%.2f秒'%time.clock())
