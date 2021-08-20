import queue
import threading
import time


class SonThread(object):

    def __init__(self, data_cb, sid):

        self._data_cb = data_cb
        self._sid = sid

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self._data_cb(id=self._sid, data=1)
            time.sleep(1)


class Main(SonThread):

    def __init__(self, sid):
        super().__init__(data_cb=self._data_cb_, sid=sid)

    def _data_cb_(self, id, data):
        self.q = queue.SimpleQueue()
        self.q.put((id, data))
        print((id, data))

    def get_data(self):
        print(self.q.get())


if __name__ == '__main__':

    for i in range(10):
        main = Main(sid=i)
        main.get_data()
    while 1:
        time.sleep(1)
