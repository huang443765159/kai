import time

import numpy as np
from threading import Thread
from multiprocessing import Queue
from multiprocessing import shared_memory, Process


class Write:

    def __init__(self, q: Queue):
        self._q = q
        one_point = [0, 1, 1, 0.5, 2, 0.3, 1]
        points = [one_point for x in range(100)]
        self._points_bytes = np.array(points).tobytes()
        self._shm = shared_memory.SharedMemory(name='6', create=True, size=len(self._points_bytes))
        self._process = Process(target=self._working, daemon=True)

    def _working(self):
        for i in range(1, 20001):
            one_point = [i / 100, 1, 1, 0.5, 2, 0.3, 1]
            points = [one_point for x in range(100)]
            self._points_bytes = np.array(points).tobytes()
            self._shm.buf[:len(self._points_bytes)] = self._points_bytes[:]

    def start(self):
        self._process.start()


class Read:

    def __init__(self, q: Queue, t):
        self._q = q
        self._ts = t
        self._shm = shared_memory.SharedMemory(name='6')
        self._thread = Thread(target=self._working, daemon=True)
        self._thread.start()

    def _working(self):
        all_p = list()
        while True:
            # data = self._q.get()
            points = np.ndarray((100, 7), dtype=np.float64, buffer=self._shm.buf).tolist()
            if points[0][0] == 200:
                print(time.time() - self._ts, points)
                break


if __name__ == '__main__':
    import time
    q = Queue()
    ts = time.time()  # 1.6s
    write = Write(q=q)
    read = Read(q=q, t=ts)
    write.start()
    while 1:
        time.sleep(1)

