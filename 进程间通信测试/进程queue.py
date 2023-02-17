# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:何以解忧
@Blog(个人博客地址): https://www.codersrc.com/

@File:python_process_queue.py
@Time:2019/12/21 21:25

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""

from multiprocessing import Process
from multiprocessing import Queue
import time, random

one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(150000)]


# 写数据进程执行的代码
def proc_write(q):
    print('Process is write....')
    q.put(all_points)
    print('put %s to queue... ', len(all_points))
    time.sleep(random.random())


# 读数据进程的代码
def proc_read(q, s):
    print('Process is reading...')
    while True:
        url = q.get()
        print('Get %s from queue', len(url))
        print(time.time() - s)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    ts = time.time()
    proc_write1 = Process(target=proc_write, args=(q, ))
    proc_reader = Process(target=proc_read, args=(q, ts))
    # 启动子进程，写入
    proc_write1.start()

    proc_reader.start()
    # 等待proc_write1结束
    proc_write1.join()
    # proc_raader进程是死循环，强制结束
    proc_reader.terminate()
    print("mian")
