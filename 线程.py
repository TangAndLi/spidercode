

# 进程
from  multiprocessing import Process
from time import sleep

import threading
sem = threading.Semaphore(100)

class myProcess(Process):
    def __init__(self,id,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.id = id

    def run(self):
        print('子进程%d 开始运行'% self.id)
        sleep(2)
        print(self)
        print('子进程%d 结束运行'% self.id)

if  __name__ == '__main__':
   print('父进程开始运行')
   for i in range(4):
        p = myProcess(name = '子进程'+str(i),id = i)
        p.start()
   print('over')












