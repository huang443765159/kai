import multiprocessing
import random
import time


class Process(object):

    def __init__(self, queue):
        self._queue = queue
        self._write_processing = multiprocessing.Process(target=self._write_data)
        self._read_processing = multiprocessing.Process(target=self._read_data)
        self._write_processing.start()
        self._read_processing.start()

    def _write_data(self):
        while 1:
            data = random.randint(0, 10)
            self._queue.put(data)
            print('WRITE', data)
            time.sleep(0.2)

    def _read_data(self):
        while 1:
            data = self._queue.get()
            print('READ', data)


if __name__ == '__main__':
    test = Process(queue=multiprocessing.Queue())
