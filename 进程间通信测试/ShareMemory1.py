import array
import os
import time

import numpy as np
from typing import Optional
import multiprocessing
from multiprocessing import shared_memory, Process
from multiprocessing import cpu_count, current_process


one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(200)]

np_points = np.array(all_points).tobytes()  # list to bytes

# 制作一个空memory, 可以在一个进程共享，也可以在两个进程共享
# 进程间通信：15w个点，1个点数据是8位列表，内存共享要25ms，pipenv要28ms，queue只要7ms


def make_memory():
    shm = shared_memory.SharedMemory(create=True, size=len(np_points), name=str(0))
    for i in range(10000):
        shm.buf[:len(np_points)] = np_points


def get_memory_data(ts):
    i = 0
    _data = list()
    ex_shm = shared_memory.SharedMemory(name=str(0))
    while 1:
        i += 1
        points = ex_shm.buf.tolist()[:len(np_points)]
        _data.append(points)
        if i == 10000:
            print(2222, time.time() - ts, len(_data))


if __name__ == '__main__':
    import time

    # 1.9s
    ts = time.time()
    process1 = Process(target=make_memory)
    process = Process(target=get_memory_data, args=(ts, ))
    # 2种方式，发送开始，然后子进程开始无脑放数据，主进程开始无脑取
    # 另一种就是也用队列，把名字发过去，然后这边开始按名字取
    process1.start()

    process.start()
