import time

import numpy as np
from threading import Thread
import multiprocessing
from multiprocessing import Queue
from multiprocessing import shared_memory, Process


class Write:

    def __init__(self, q: Queue):
        self._q = q
        one_point = [0, 1, 1, 0.5, 2, 0.3, 1]
        points = [one_point for x in range(100)]
        self._points_bytes = np.array(points).tobytes()
        # self._shm = shared_memory.SharedMemory(name='2', create=True, size=len(self._points_bytes))
        self._process = Process(target=self._working, daemon=True)

    def _working(self):
        for i in range(20000):
            one_point = [0.1, 1, 1, 0.5, 2, 0.3, 1]
            points = [one_point for x in range(100)]
            self._points_bytes = np.array(points).tobytes()
            self._q.put(self._points_bytes)
            if i == 0:
                self._q.put((1, time.time()))
            if i == 9999:
                self._q.put((2, ))

    def start(self):
        self._process.start()


class Read:

    def __init__(self, q: Queue, t):
        self._q = q
        self._t = t
        # self._shm = shared_memory.SharedMemory(name='2')
        self._thread = Thread(target=self._working, daemon=True)
        self._thread.start()

    def _working(self):
        all_p = list()
        while 1:
            data = self._q.get()
            if data[0] == 1:
                t = data[1]
            elif data[0] == 2:
                print(time.time() - self._t, len(all_p))


if __name__ == '__main__':
    import time
    # 1.74s
    q = Queue()
    ts = time.time()
    write = Write(q=q)
    read = Read(q=q, t=ts)
    write.start()
    while 1:
        time.sleep(1)
