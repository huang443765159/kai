import time

import numpy as np
from multiprocessing import shared_memory, Process


class Write:

    def __init__(self):
        one_point = [0, 1, 1, 0.5, 2, 0.3, 1]
        points = [one_point for x in range(150000)]
        self._points_bytes = np.array(points).tobytes()
        self._shm = shared_memory.SharedMemory(name='6', create=True, size=len(self._points_bytes))

    def working(self):
        self._shm.buf[:len(self._points_bytes)] = self._points_bytes[:]


class Read:

    def __init__(self):
        self._shm = shared_memory.SharedMemory(name='6')

    def working(self, t):
        points = np.ndarray((150000, 7), dtype=np.float64, buffer=self._shm.buf)
        print(time.time() - t, len(points))


if __name__ == '__main__':
    import time
    write = Write()
    read = Read()
    ts = time.time()  # 1主2子进程26-27ms，1主1子进程14ms， 用for的话在1.6s
    process = Process(target=write.working, daemon=True)
    process1 = Process(target=read.working, daemon=True, args=(ts, ))
    process.start()
    # read.working(t=ts)
    process1.start()
    while 1:
        time.sleep(1)
