import threading
import time
from multiprocessing import Process, Queue


one_point = [1, 2, 3, 0.4, 0.6, 0.7, 10]
all_points = [one_point for x in range(200)]


class PutPoints:

    def __init__(self, q: Queue):
        self._q = q
        self._process = Process(target=self._working, daemon=True)

    def _working(self):
        for i in range(1000):
            self._q.put((i, all_points))

    def start(self):
        self._process.start()


class GetPoints:

    def __init__(self, q: Queue):
        self._q = q
        self._thread = threading.Thread(target=self._recv, daemon=True)
        self._t = 0

    def _recv(self):
        while 1:
            data = self._q.get()
            if data[0] == 999:
                print(time.time() - self._t, len(data))

    def start(self):
        self._t = time.time()
        # self._put.start()
        self._thread.start()


if __name__ == '__main__':
    q = Queue()  # 7ms, 用for也是7ms
    get = GetPoints(q=q)
    put = PutPoints(q=q)
    put.start()
    get.start()
    while 1:
        time.sleep(1)
