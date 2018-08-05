
import re

# str = 'abcd123456.jk0222'
# pattern = re.compile(r'\w+\.')
# # match 从头开始匹配
# m = pattern.match(str)
# print(m)
# # 取出匹配到的字符串
# print(m.group())
#
# pattern = re.compile(r'\d+\.\w+')
# s = pattern.search(str)
# print(s.group())

# ft= pattern.findall(str)
# print(ft)
#
# ft = pattern.finditer(str)
# for i in ft:
#     print(i.start(),i.end(),i.group(),i.span())
#

# str = 'aa, ,22, hh   :  :: 33 ,word'
#
# p = re.compile(r'[\s\:\,]+')
# list = p.split(str)
# print(list)

#['aa', ' ', '22', ' hh   :  : 33 ', 'word']
#['aa', ' ', '22', ' hh   :  : 33 ', 'word']
# for i in list:
#     print(i)
"""
import re

str ='113.22.222.233'

pattern = re.compile(r'(25[0-5]\.|2[0-4]\d\.|1\d{2}\.|[1-9]\d\.|\d\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)')
# m = pattern.findall(str)
# print(m)
ip = re.compile(r'(25[0-5]\.|2[0-4]\d\.|1\d{2}\.|[1-9]\d\.|\d\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)',re.S)
m = ip.search(str)
print(m.group())


reg = "^\d{1,3}[\-\./]\d{1,2}[\-\./]\d{1,2}$"
str2 = "201.11.11"
print(re.search(reg, str2).group())


# res = re.search("www", "www.baiduwww.com")
res = re.search("www", "ww.baiduwww.com")
print(res.group())

str = '0775-987654'
reg = '((\d{3,4})-(\d{6}))'
# res = re.search(reg,str)
res = re.findall(reg,str)
res1 = re.search(reg,str)
print(res1.groups())
print(res)
# print(res.group(2))

# state = (('0','x'),(1,'y'),('2','z'))
#
# print(state[1][0])
"""
"""
class A():
    def __init__ ( self,n ):
        self.n = n

    # ge 大于等于
    def __gt__ ( self,value ): # 相当于把 a2 传给了value
        if isinstance(value,A):  # 判断  a2  是否是函数A的对象
            print('xxx')
            print(self.n,'----------',value.n)
            return self.n > value.n  # 是就返回调用的值  给下面的if函数做判断
        else:
            return self.n > value

a1 = A(10)
a2 = A(20)

if a1 > a2:
    print('1')
else:
    print('2')

if a1 > 5:
    print('a')

"""
"""
from collections import Iterator # 迭代器
from collections import Iterable #迭代器对象
print(isinstance([1,2],Iterator))
print(isinstance((1,2),Iterable))
"""
"""
 可以被for in 就是迭代器对象
 可以被for in 和 next() 就是迭代器
 iter() 函数可以得到一个迭代器
 
"""
"""
res = iter([1,2,3,4]) # 得到迭代器
# print(next(res)) 
# print(next(res))

list1 = list(res) #将迭代器转换成迭代器对象
print(list1)

"""
"""
generator = (i for i in range(1,4))
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
# 没有下标时报StopIteration 
"""
#
# def fn(n):
#     data = ''
#     print('A',data)
#     yield n+1
#
"""  生成器 生成斐波那数
def fn1(max):
    n,b,c = 0,0,1
    while n < max:
        yield b
        b,c = c,b+c
        n += 1
    return '空'

f = fn1(10)
while True:
    try:
        x = next(f)
        print('f:',x)
    except StopIteration as e:  
        print(e.value) # 打印接收的错误值
        break    # 跳出这次循环

"""
"""
class fn(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 10:
            raise StopIteration() #退出条件
        return self.a


for i in fn():
    print(i)

"""

# a = [('a',3),('b',7),('c',6)]
# # print(sorted(a,key = lambda item:item[1] ,reverse=True))
# b = [7,4,6,8]
# print(sorted(a))


# a = int(input())
#
# if a > 10:
#     print('z')
# elif a >20:
#     print('b')
# elif  a > 30:
#     print('c')

# import re
# a = 'Tang_and@qq.com.com.ocm.com'
# c = '[a-zA-Z0-9._-]+@\w+[a-zA-Z0-9\.]+'
# b = re.search(c,a)
# print(b.group())


# str = 'MRS Studios短袖不规则2018新款夏 ja*c设计款侧飘带一字领上衣女'
# p = re.compile('[a-zA-Z0-9\u4e00-\u9fa5 +*!]+')
# list = p.findall(str)
# print(list)
# # print("".join(list))
#
# str = '你好everyone，你好我好 大家好，good'
# p = re.compile(u'[\u4e00-\u9fa5]+')
# print(p.findall(str))

# import pymysql
#
# db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='sq')
# # cursor = db.cursor()
# print(db)


# list = [1,2,3,4,5]
# i = 10
# try:
#     if i in list:
#         print('%d在里面'%(i))
#     else:
#         list.append(i)
# except Exception as e:
#     print('不在里面',e)
# print(list)


# try:
#     print(5/1)
# except ZeroDivisionError as e:
#     print("捕获到异常：除数为0")
# except NameError as e:
#     print("捕获到异常：未定义")
#
# finally:
#     print("finally")
# print("end")
#
#
str1 = 'USD 49.00'
str2 = str1.split(' ')[1]
print(str2)

