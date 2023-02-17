from multiprocessing import Process
from multiprocessing import Queue
import time, random

one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(200)]


# 写数据进程执行的代码
def proc_write(q):
    # print('Process is write....')
    for i in range(1000):
        q.put(all_points)
        # print('put data ', len(all_points))
        # time.sleep(random.random())


# 读数据进程的代码
def proc_read(q, s):
    # print('Process is reading...')
    i = 0
    _data = list()
    while True:
        i += 1
        data = q.get()
        _data.append(data)
        # print('Get data', len(url))
        if i == 1000:
            print(time.time() - s, len(_data))


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程, 7ms
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
