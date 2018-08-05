
import multiprocessing # 分布式进程
import multiprocessing.managers # 管理器
import random,time
import queue


class QueueManger(multiprocessing.managers.BaseManager):
    pass

if __name__ == '__main__':
    QueueManger.register('get_task')
    QueueManger.register('get_result')
    manager =QueueManger(address = ('10.36.137.11',8848),authkey = '123456')
    # 连接服务器
    manager.connect()
    task = manager.get_task()
    result = manager.get_result()

    for i in range(100):
        try:
            data = task.get()
            print('client get',data)
            result.put('client' + str(data+10))
        except:
            pass

