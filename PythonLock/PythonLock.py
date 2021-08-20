import threading
import time


class TestLock(object):

    def __init__(self, sid, lock):

        self._sid = sid
        self._lock = lock
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            self._lock.acquire()
            print(self._sid)
            self._lock.release()
            time.sleep(1)


if __name__ == '__main__':

    _lock = threading.Lock()
    for i in range(10):
        thread = TestLock(sid=i, lock=_lock)
    while 1:
        time.sleep(1)
