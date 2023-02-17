import numpy as np
from multiprocessing import Process
from multiprocessing import Pipe
import os, time, random


one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(150000)]


# 写数据进程执行的代码
def proc_send(pipe, p):
    # print 'Process is write....'
    # print('Process is send :%s' % p)
    pipe.send(p)
    time.sleep(random.random())


# 读数据进程的代码
def proc_recv(pipe, ts):
    while True:
        # print('Process rev:%s' % pipe.recv())
        data = pipe.recv()
        print(time.time() - ts, len(data))
        time.sleep(random.random())


if __name__ == '__main__':
    # 父进程创建pipe，并传给各个子进程
    pipe = Pipe()
    ts = time.time()
    p1 = Process(target=proc_send, args=(pipe[0], all_points))
    p2 = Process(target=proc_recv, args=(pipe[1], ts))
    # 启动子进程，写入
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
    print("mian")

