

# def fn(n):
#     return n-1
#
# list1 = [1,2,3,4]
# list2 = map(fn,list1)
# print(list(list2))

# list3 = list(map(str,list1))
# print(list3)


# list = [8,9,7,6,5,3,4]
# for i in range(0,len(list)-1):
#     for j in range(0,len(list)-i-1):
#         if list[j] > list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
# print(list)

# for i in range(len(list)-1):
#     for j in range(len(list)-1-i):
#         if list[j] < list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
#
# print(list)

#选择排序
# for i in range(len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i] > list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)

# for i in range(len(list)-1):
#     index = i
#     for j in range(i+1,len(list)):
#         if list[j] < list[index]:
#             index = j
#     list[i],list[index] = list[i],list[index]
# print(list)


# def quickSort(list):
#     if len(list) <=1:
#         return list
#
#     centerIndex = len(list)//2
#     center = list.pop(centerIndex) # 删除并返回
#
#     listLeft = []
#     listRight = []
#     for i in list:
#         if i < center:
#             listLeft.append(i)
#     for j in list:
#         if j > center:
#             listRight.append(j)
#     # print(quickSort(listLeft) + [center] + quickSort(listRight))
#     return quickSort(listLeft) + [center] + quickSort(listRight)
#
# list1 = quickSort(list)
# print(list1)




# def deco(n):
#     def warp1(func):
#         def warp2(*args,**kwargs):
#             print(n)
#             return func(*args,**kwargs)
#         return warp2
#     return warp1
#
#
# @deco(2)
# def girl(n):
#     print('hello  my'"\'s girlfriends",'xx')
#     return n
# print(girl(1))

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 3:
#         if j == 3:
#             break
#         print(i,j)
#         j += 1
#     i += 1

"""
list.append()
list.extend([x,y]) # 加入多个元素
list.insert(index,cls) #下标 参数
list.count() #统计列表中指定的元素出现次数
list.clear() #清除列表 
list.index() #查询指定元素在列表中对应的下标 没有就报错
max(list) # 列表中的最大值
min(list) # 列表中的最小值
list1 = sorted(list)  # 默认升序排序
list1 = sorted(list,reverse = True) # 降序
list.sort() # 升序
list.sort(reserve = True) # 降序 改变原列表
list.reverse() # 反转

fp = open('./xx,'r',encoding='utf-8')
fp.read(12) 
fp.readline() 读取一行
fp.readlines() 读取所有行

fp = open('./xx','rb') # 把二进制转换成字符串
content = fp.read()
# 把二进制转换成字符串  
str = content.decode(encoding='utf-8')
# 字符串转换成二进制
str.encode(encoding='utf-8')
fp.close()

将字典转换成集合 会保存字典的key
dict = {}
set = set(dict)
"""
import os
# print(os.path.splitext('情书.txt'))
# # 默认以点拆分
# print(os.path.split(r"C:\wamp\www\day08\code\情书.txt"))
"""
os.path.isfile() #是否是文件
os.path.isdir() #是否是目录
os.path.exists() #判断目录是否存在
open("文件路径", "r", encoding="utf-8", error="ignore")
pickle #模块
os.mkdir() 创建目录
os.rmdir() 删除目录
os.remove() 删除文件
os.rname() 修改目录名称
os.getcwd() 获取当前文件所在目录
os.listdir() 获取目录下的所有文件名和目录名
os.curdir() 当前相当目录
os.system() 执行shell命令
os.path.abspath() 获取绝对路径
os.path.dirname(__file__) #获取当前文件名
os.path.split() 将目录和文件拆分开
os.path.splitext() 将文件名和拓展名拆分
os.path.join() 拼接
os.path.isfile() 是否是文件
os.path.isdir() 是否是目录
os.path.exists() 是否存在

# 字符串操作
str.upper() 小写字母大写
   .lower() 大写字母小写
   .title() 首字母大写 其他小写
   .swapcase() 大小写翻转
   .capitalize() 字符串首字母大写
   .isupper() 判断是否所有字母都是大写
   .islower() 判断是否所有字母都小写
   .strip() 

# 字符串查找
find()
#查找字符串中指定子字符串第一次出现的位置(下标/索引)
如果找不到就反回-1
str.find() 
   .rfind() 右边查找
   .index() /rindex 找到反回下标 没有就报错
   .splitlines() 按行拆分
   .replace(x,y,z) 替换 x旧字符串 y新换字符 z数量/默认全部替换
   .startswith('x') 判断是否已x开头
   .endswith('x') 判断是否以x结尾
   .count() 统计指定字符串出现的次数
   
   str = 'a'
   ord(str) 将字符串转换成ascll码
   chr(97) 将ascll码转换成字符
   
"""
path = r'c:\www\day\www\\'
file = '04-kkkk'
str = path.rstrip('\\') + '\\'+file
print(str)

"""

"""
# stack = []
# stack.append('k')
# print(stack)
# stack.append('B')
# print(stack)
# stack.append('c')
# print(stack)
#
# 出栈 在列表的末尾取出数据
# res = stack.pop()
# print(stack)
# print(res)
#
# res = stack.pop()
# print(stack)
# print(res)

# import time
# t = time.time()
# print(t)
#
# t1 = time.gmtime(t)
# print(t1[0],t1[1])
import pickle
# list1 = ('xx','zz','ss','qq','bb')
# fp = open('./data.txt','wb')
# pickle.dump(list1,fp)
# fp.close()
#  序列化

# 反序列化
# fp = open('./data.txt','rb')
# res = pickle.load(fp)
# print(res)
# print(type(res))

# @deco(4)
# def my(n,m):
#     return  m + n
#
# print(my(2,3))
# list = [(b'2', 5.0), (b'16', 2.0), (b'9', 1.0), (b'7', 1.0), (b'3', 1.0)]
# l =[id for id,_ in list]
# print(l)

# import collections
#
# queue = collections.deque()
# print(queue)
#
# queue.append('B')
# print(queue)
#
# queue.append('C')
# print(queue)
#
# queue.appendleft('D')
# print(queue)
#
# res = queue.pop()
# print(queue)
# print(res)
#
# res = queue.popleft()
# print(queue)
# print(res)


import os
"""
def getAllDirAndFile(sourcePath):
    if not os.path.exists(sourcePath):
        return '目录不存在'

    fileNameList = os.listdir(sourcePath)
    print(fileNameList)
    for fileName in fileNameList:
        absPath = os.path.join(sourcePath,fileName)
        # print(absPath)
        if os.path.isfile(absPath):
            print('fileName:',fileName)
        elif os.path.isdir(absPath):
            print('dirName',fileName)
            getAllDirAndFile(absPath)

if __name__ == '__main__':

    # dirPath = os.path.abspath(os.path.dirname(__file__))
    # print(dirPath)
    dirPath = r'D:\s-爬虫\作业'
    getAllDirAndFile(dirPath)                                 


# dirPath = os.path.dirname(__file__)
# dirPath = os.path.join(os.path.abspath(__file__),'lll')
# print(dirPath)
"""

# import os
#
# def copyDir(sourcePath,targetPath):
#
#     if not os.path.exists(sourcePath):
#         return '目录不存在，无法复制'
#     if not os.path.exists(targetPath):
#         os.mkdir(targetPath)
#
#     fileNamelist = os.listdir(sourcePath)
#     # print(fileNamelist)
#     for filename in fileNamelist:
#         newsourcePath = os.path.join(sourcePath,filename)
#         newtargetPath = os.path.join(targetPath,filename)
#         # print(newtargetPath)
#         # print(newsourcePath)
#
#     #     # 如果是文件则复制
#         if os.path.isfile(newsourcePath):
#             copyFile(newsourcePath,newtargetPath)
#     #
#          # 如果是目录则递归创建
#         if os.path.isdir(newsourcePath):
#             os.mkdir(newtargetPath)
#             copyDir(newsourcePath,newtargetPath)
#
# def copyFile(newsourcePath,newtargetPath):
#     source = open(newsourcePath,'rb')
#     target = open(newtargetPath,'ab')
#
#     while True:
#         content = source.read(1024)
#         if len(content) == 0:
#               break
#         target.write(content)
#
#     source.close()
#     target.close()
#
#
# if __name__ == '__main__':
#     sourcePath = os.path.abspath(os.path.dirname(__file__))
#     targetPath = os.path.abspath(os.path.dirname(__file__))+'-副本'
#     copyDir(sourcePath,targetPath)

# print(os.path.abspath(os.path.dirname(__file__)))
#
#
# def quickSort(list):
#     if len(list) <=1:
#         return list
#     centerIndex = len(list)//2
#     center = list.pop(centerIndex)
#
#     leftList = []
#     rightList = []
#
#     for i in list:
#         if i > center:
#             rightList.append(i)
#         else:
#             leftList.append(i)
#         return quickSort(leftList) + [center] + quickSort(rightList)
#

"""
def d2(a,b):
    def wanner(func):
        print('[output]')
        print('before test',a,b)
        def wanner1(*args,**kwargs):
             func(*args,**kwargs)
             print('[\output]')
        return wanner1
    return wanner


@d2("a","b")
def test(arg1,arg2):
    print('test',arg1,arg2)
    
test('c','d')
"""
"""
re.match() 匹配字符开头
re.search() 匹配指定的字符串 返回匹配的
re.findall() 匹配字符串中和某个模式匹配的 以列表的形式返回
[] 表示单个字符串允许出现的范围
{} 表示匹配次数
() 分组 
. + r.S 表示匹配任意字符 可以匹配到换行

x | y   x或y

* 表示0个 或 多个 
？ 表示0个 或一个
+  表示一个 或多个

[a-zA-Z0-9_]
[^0-9] 非数字
\d   [0-9]
\w   [a-zA-Z0-9_]
\W   [^a-zA-Z0-9_]
\s   表示换行符\n 空格 换页符\f \t \r [\n\r]
\S   表示非换行符 ......




"""
# import re
# res = re.search('www','wwz.baiduwWwc.com',re.I)
# print(res.group())
# import random
# import string
# nonce = ''.join(random.sample(string.ascii_letters + string.digits, 20))
# print(nonce)
#

# import os
# def path(filePath):
#     for root,dirs,files,in os.walk(filePath):
#         for file in files:
#             print(root + file)
#         for dir in dirs:
#             path(dir)
#
# a = r'D:\s-爬虫\作业'
# path(a)


# def m(list):
#     v  =list[0]
#     for e in list:
#         if v < e : v =e
#     return v
#
# values = [[3,4,5,1],[33,6,1,2]]
#
# for row in values:
#     print(m(row),end=' ')

import socket
"""
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1',8080))

while True:
    sendData = input('客户端:')
    clientSocket.send(sendData.encode('utf-8'))
    
    recvDate = clientSocket.recv(1024)
    print('服务端说',recvDate.decode('utf-8'))
"""
"""
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1',8888))
serverSocket.listen(5)

# 等待客户端来连接 阻塞线程
clientSocket,address = serverSocket.accept()

while True:
    recvData = clientSocket.recv(1024)
    print(recvData.decode('utf-8'))

    sendData = input('服务端说:')
    clientSocket.send(sendData.encode('utf-8'))

    clientSocket.close()
"""
"""
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    sendDate = input('1:')
    clientSocket.sendto(sendDate.encode('utf-8'),(("127.0.0.1",8088)))

    data,address = clientSocket.recvfrom(1024)
    print('2:',data.decode('utf-8'))
    print('2:',address)
"""
"""
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind(('127.0.0.1',8000))

while True:
    print('等待客户端发送消息')
    data,address= serverSocket.recvfrom(1024)
    print('1:',data.decode('utf-8'))
    print('1:',address)

    sendData = input('2:')
    serverSocket.sendto(sendData.encode('utf-8'),address)
"""

# 冒泡排序：
"""
list1 = [1,2,3]

for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]


# 选择排序
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)-1):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

for i in range(len(list1)-1):
    index = i
    for j in range(i+1,len(list1)-1):
        if list1[j] < list1[index]:
            index = j
        list1[index],list1[i] = list1[j],list1[index]


def quicklySort(list1):

    index=len(list1)//2
    center = list1.pop(index)

    leftList = []
    rightList = []
    for i in list1:
        if i > center:
            rightList.append(i)
        else:
            leftList.append(i)

    return quicklySort(leftList) + [center] +quicklySort(rightList)
"""

# class singleton(object):
#     _instance = None
#     def __new__(cls,*args,**kwargs):
#         if not cls._instance:
#             cls._instance = super(singleton,cls).__new__(cls,*args,**kwargs)
#         return cls._instance
#
# class myClass(singleton):
#     a =1
# one = myClass()
# two = myClass()
#
# print(id(one)==id(two))


# import random
# import numpy as np

# list1 =[i for i in range(1,9)]
# # print(list1)
# offices = [[],[],[]]
#
# for list2 in list1:
#     index = random.randint(0,2)
#     offices[index].append(list2)
#     if index == 0:
#         for i in [2,3,3]:
#             offices[index].append(i)
#     elif index == 1:
#         for i in [3,2,3]:
#             offices[index].append(i)
#     elif index == 2:
#         for i in [3,3,2]:
#             offices[index].append(i)


    # for i in off:
    #     print(i,end ='')










# import re
# res = '45032419960819371X'
#
# str = re.search(r'^\d{17}[A-Z0-9]',res)
# print(str.group())



# import random
# office =[[],[],[]]
#
# names = ['t1','t2','t3','t4','t5','t6','t7','t8']
# for t in names:
#     of = random.randint(0,2)
#     while True:
#         if len(office[of])>=3:
#             of = random.randint(0,2)
#         elif len(office[of])<=2:
#             break
#     office[of].append(t)
# for i in office:
#  print(i)
#

from multiprocessing import Process, Pool
import os, time, random

def run(name):
    print('子进程%d启动--%s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print('子进程%d结束--%s--耗时%.2f' % (name, os.getpid(), end-start))



if __name__ == '__main__':
    print('父进程启动')
    # 创建进程池
    # 4表示同时可以执行的进程数量，不写默认是电脑的cpu内核数
    pp = Pool(4)

    for i in range(100):
        pp.apply_async(run, args=(i,))

    # 关闭进程池，调用close之后不能再继续添加新的进程。
    pp.close()
    # 等进程池中的进程都完成再结束进程池, 注意必须在调用close之后调用join
    pp.join()

    print('父进程结束')











































































































































































