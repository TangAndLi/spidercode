

#试题请做下。 pathon部分：

#  1、元组和列表的区别。 

#列表是可变的数据类型，即这种类型是可以被改变的，并且列表是可以嵌套的
#元祖和列表十分相似，不过元组是不可变的

#2、给定列表cloudran=["1","4","3","4","5","2"]。请输出排序后的新列表cloudranA
cloudran=["1","4","3","4","5","2"]
cloudranA = sorted(cloudran)
print(cloudranA)

#3、给定列表cloudran=["1","4","3","4","5","2"]。请输出去重后的新列表cloudranA 
CloudranA = sorted(set(cloudranA))
print(CloudranA)

#4、实现一个队列(先进先出) 
import collections
queue = collections.deque()

for i in 'ABCD':
    queue.append(i)
    print(queue)

for i in queue:
    print(i)


#shell部分： 
#1、sh和source执行区别 

# sh在执行的时候 新建一个shell执行文件 有2个新进程在运行 一个bash 一个sleep
# source 是在当前shell 执行命令


#2、在shell中定义一个名叫cloudran的全局变量；


#在shell中定义一个名叫cloudran的局部变量 


#3、用命令查找cloudran.txt文件位置；
# whereis cloudran.txt


#用命令查找包含“cloudran”字符串的文件。


#4、用命令把cloudran1.txt、cloudran2.txt、cloudran3.txt文件中的“cloudran”字符串替换为“CloudRan” 



#编程题： 1、阶乘 1+1*2+1*2*3...+1*2*3..*N(语言不限)

# x = int(input('请输入：'))
# n = 1
# y = 1
# z = 0
# while n <= x:
#     y *= n
#     z += y
#     n += 1
# print(z)

li = '22'

print(eval(li))







