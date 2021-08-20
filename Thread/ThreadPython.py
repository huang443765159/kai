import threading
import time


class Thread(object):

    def __init__(self):
        self._num = 0
        self._thread = None
        self._thread_switch = False

    def _working(self):
        print('thread running...')
        while self._thread_switch:
            self._num += 1
            print(self._num)
            time.sleep(1)
        print('thread stop')

    def start(self):
        self._thread_switch = True
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self._thread_switch = False
        self._thread.join()


if __name__ == '__main__':

    thread = Thread()
    thread.start()
    time.sleep(2)
    thread.stop()

