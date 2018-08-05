


import multiprocessing # 分布式进程
import multiprocessing.managers # 管理器
import random,time
import queue
import os

task_queue = queue.Queue()  #任务
result_queue = queue.Queue() # 结果


# 任务队列
def return_task():
    return task_queue


# 结果队列
def return_result():
    return result_queue


# 继承 进程管理共享数据
class QueueManger(multiprocessing.managers.BaseManager):
    pass


if __name__ == '__main__':
    #  开启分布式支持
    multiprocessing.freeze_support()
    # 注册函数 给客户调用
    QueueManger.register('get_task', callable =return_task)
    QueueManger.register('get_result', callable= return_result)
    # 创建一个管理器
    manager = QueueManger(address = ('10,36,137,11',8848), authkey =123456)
    manager.start()
    task,result = manager.get_task(),manager.get_result()  # 任务，结果
    # task = manager.get_task()
    # result = manager.get_result()

    for i in range(100):
        print('task add data',i)
        task.put(i)
    print('waiting for ------------------------')
    for i in range(100):
        res = result.get()
        print('get data',res)

    # 服务器关闭
    manager.shutdown()

































