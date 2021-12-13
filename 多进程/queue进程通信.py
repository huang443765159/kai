import time
from multiprocessing import Process, current_process, Queue


class A:

    def __init__(self, q: Queue):
        self._process = Process(target=self._working, daemon=True, args=(q, ))
        self._process.start()

    def _working(self, q: Queue):
        print(1, current_process())
        q.put([1, 2, 3])
        q.put([3, 2, 1])


class B:

    def __init__(self, q: Queue):
        self._process = Process(target=self._working, daemon=True, args=(q, ))
        self._process.start()

    def _working(self, q: Queue):
        print(2, current_process())
        data = q.get()
        print(data)


class C:

    def __init__(self, q: Queue):
        self._process = Process(target=self._working, daemon=True, args=(q, ))
        self._process.start()

    def _working(self, q: Queue):
        print(3, current_process())
        data = q.get()
        print(data)


if __name__ == '__main__':
    q = Queue()
    a = A(q=q)
    b = B(q=q)
    c = C(q=q)
    print(4, current_process())
    while 1:
        time.sleep(1)
