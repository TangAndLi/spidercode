import os
from threading import Thread
from multiprocessing import Pool
import time
for i in range(1,6):
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)),'files'+str(i))
    dest = os.path.join(os.path.abspath(os.path.dirname(__file__)),'to_files'+str(i))
    # print(source,dest)
def copy_file(source,dest):
    old_file = open(source, 'rb')
    new_file = open(dest, 'wb')
    while True:
        content = old_file.read(1024)
        if len(content) == 0:
            break
        new_file.write(content)
        old_file.close()
        new_file.close()

if __name__ == '__main__':
    print('主进程启动')
    pp = Pool(4)
    # pp.apply_async()











