import array
import os
import time

import numpy as np
from typing import Optional
import multiprocessing
from multiprocessing import shared_memory, Process
from multiprocessing import cpu_count, current_process


one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(150000)]

np_points = np.array(all_points)  # list to array

# print(np_points.shape, np_points.dtype)  # (192, 8), np.float64

# print(np_points.tolist())  array to list

# 制作一个空memory, 可以在一个进程共享，也可以在两个进程共享
# 进程间通信：15w个点，1个点数据是8位列表，内存共享要25ms，pipenv要28ms，queue只要7ms


class MakeProcess:

    def __init__(self):
        self._shm = None
        self._name = 0

    def make_memory(self):
        self._name += 1
        self._shm = shared_memory.SharedMemory(create=True, size=np_points.nbytes, name=str(self._name))
        array_data = np.ndarray(np_points.shape, dtype=np_points.dtype, buffer=self._shm.buf)  # 把数据填充进去
        array_data[:] = np_points[:]
        # print(1111, os.getpid())
        return self._shm

    def unlink(self):
        self._shm.unlink()


class GetProcess:

    def __init__(self):
        self._shm = None

    def get_memory_data(self, ts):
        self._shm = shared_memory.SharedMemory(name=str(1))
        points = np.ndarray(np_points.shape, dtype=np.float64, buffer=self._shm.buf)
        print(time.time() - ts)

    def close(self):
        self._shm.close()


if __name__ == '__main__':
    import time

    make = MakeProcess()
    get = GetProcess()

    ts = time.time()
    process1 = Process(target=make.make_memory)
    process = Process(target=get.get_memory_data, args=(ts, ))

    # 2种方式，发送开始，然后子进程开始无脑放数据，主进程开始无脑取
    # 另一种就是也用队列，把名字发过去，然后这边开始按名字取
    process1.start()
    process.start()
