import random
import time
import uuid
from multiprocessing import Pipe,Process,current_process


def task(conn,url):
    while True:
        time.sleep(3)
        conn.send('完成了'+url+'网络请求')
        msg = conn.recv()
        if msg ==  66:
            time.sleep(0.05)
            conn.send('bye')
            break
        print(current_process().name,'子进程开始新的任务：',msg)
        conn.send(str(uuid.uuid4()).replace('-',''))
    print(current_process().name,'子进程结束')


if __name__ == '__main__':
    conn1,conn2 = Pipe() #默认全双工
    taskProcess = Process(target=task,args = (conn1,'http://www.jd.com'))
    taskProcess.start()
    while True:
        msg = conn2.recv() # 等待管道发来的消息
        if msg == 'bye':
            break

    # 获取当前进程名
        print( current_process().name ,'进程-收到-',msg)

        num = random.randint(50,100)
        time.sleep(0.05)
        conn2.send(num)
    print('---over----')














