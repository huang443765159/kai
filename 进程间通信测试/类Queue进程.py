import threading
import time
from multiprocessing import Process, Queue


one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(200000)]


class PutPoints:

    def __init__(self, q: Queue):
        self._q = q
        self._process = Process(target=self._working, daemon=True)

    def _working(self):
        self._q.put(all_points)

    def start(self):
        self._process.start()


class GetPoints:

    def __init__(self):
        self._q = Queue()
        self._put = PutPoints(q=self._q)
        self._thread = threading.Thread(target=self._recv, daemon=True)
        self._t = 0

    def _recv(self):
        while 1:
            data = self._q.get()
            print(time.time() - self._t, len(data))

    def start(self):
        self._t = time.time()
        self._put.start()
        self._thread.start()


if __name__ == '__main__':
    get = GetPoints()
    get.start()
    while 1:
        time.sleep(1)
