# !usr/bin/env python
# -*- coding:utf-8 _*-
import threading
from multiprocessing import Process
from multiprocessing import Queue
import time, random

one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(200000)]


# 写数据进程执行的代码
def proc_write(q):
    print('Process is write....')
    q.put(all_points)
    print('put data ', len(all_points))
    time.sleep(random.random())


# 读数据进程的代码
def proc_read(q, s):
    print('Process is reading...')
    while True:
        url = q.get()
        print('Get data', len(url))
        print(time.time() - s)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程, 7ms
    q = Queue()
    ts = time.time()
    proc_write1 = Process(target=proc_write, args=(q, ))
    thread = threading.Thread(target=proc_read, args=(q, ts))
    # proc_reader = Process(target=proc_read, args=(q, ts))
    # 启动子进程，写入
    proc_write1.start()

    thread.start()
    # 等待proc_write1结束
    proc_write1.join()
    # proc_raader进程是死循环，强制结束
    # proc_reader.terminate()
    print("mian")
