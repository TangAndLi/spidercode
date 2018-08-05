

import urllib.request
import urllib.parse
import re
import threading
import queue
import time

def  geteveryurl(data):
    alllist=[]
    mylist1=[]
    mylist2=[]

    mylist1=getallhttp(data)
    if len(mylist1) >0:
        mylist2=getabsurl(  mylist1[0],data)

    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return  alllist


def getabsurl(url,data):
    try:
        regex=re.compile("href=\"(.*?)\"",re.IGNORECASE)
        httplist=regex.findall(data)
        newhttplist=httplist.copy()#深拷贝
        for data  in  newhttplist:
            if  data.find("http://")!=-1:
                httplist.remove(data)
            if  data.find("javascript")!=-1:
                httplist.remove(data)
        hostname=gethostname(url)
        if hostname!=None:
            for  i  in range(len(httplist)):
                httplist[i]=hostname+httplist[i]

        return httplist
    except:
        return []


#http://bbs.tianya.cn/post-140-393974-1.shtml'
#http://bbs.tianya.cn
def  gethostname(httpstr):
    try:
        mailregex = re.compile(r"(http://\S*?)/", re.IGNORECASE)
        mylist = mailregex.findall(httpstr)
        if  len(mylist)==0:
            return None
        else:
            return mylist[0]
    except:
        return None

def  getallhttp(data):
    try:
        mailregex = re.compile(r"(http://\S*?)[\"|>|)]", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


# 抓取网页
def Getdata(url):
    try:
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except:
        return "."


# 抓取当前网页邮箱
def Getallemail(data):
    try:
        # IGNORECASE 忽然大小写
        mail_regex = re.compile(r'([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})',re.IGNORECASE)
        my_list = mail_regex.findall(data)
        return my_list
    except:
        return []


def BFS(url):
    global emailqueue
    my_queue = queue.Queue() # 队列
    my_queue.put(url)

    #  队列不为空则取
    while not my_queue.empty():
        url = my_queue.get()
        # 抓取页面的数据
        pagedata = Getdata(url)
        print('抓取',url)

        # 抓取页面邮箱
        emaillist = Getallemail(pagedata)
        if len(emaillist) != 0:
            for email in emaillist:
                print(email)
                emailqueue.put(email)


        # 提取页面链接 压如队列
        urllist = geteveryurl(pagedata)
        if len(urllist) != 0:
            for myurl in urllist:
                my_queue.put(myurl)

def savemail():
    global  emailqueue
    mailfile = open('./mail.txt','ab')

    while True:
        time.sleep(3)
        # print('hello word')
        while not emailqueue.empty():
            data = emailqueue.get()
            mailfile.write((data+'\r\n').encode('utf-8','ignore'))
            mailfile.flush()
    mailfile.close()
# 邮箱队列
emailqueue = queue.Queue()
# url队列
url_queue = queue.Queue()

# 控制最大线程为100个
sem = threading.Semaphore(100)

#  5秒开启一个线程 savemail
timethread = threading.Timer(5,savemail)
timethread.start()

BFS('http://bbs.tianya.cn/m/post-140-393974-1.shtml')



# print(Getallemail(Getdata('http://bbs.tianya.cn/m/post-140-393974-1.shtml')))
# print(geteveryurl(Getdata('http://bbs.tianya.cn/m/post-140-393974-1.shtml')))








