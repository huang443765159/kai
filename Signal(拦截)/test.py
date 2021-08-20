import threading
import signal
import time
import sys


class Test(object):

    def __init__(self):

        self._thread = None
        self._thread_switch = False

        self.signal = signal.signal(signal.SIGINT, self.ctrl_c)

    def _working(self):
        count = 0
        while self._thread_switch:
            count += 1
            print(count)
            time.sleep(1)

    def ctrl_c(self, signum=None, handle=None):
        print('Stop')
        sys.exit(0)

    def launch(self):
        if self._thread_switch is False:
            self._thread_switch = True
            self._thread = threading.Thread(target=self._working)
            self._thread.daemon = True
            self._thread.start()

    def stop(self):
        if self._thread_switch:
            self._thread_switch = False
            self._thread.join()


if __name__ == '__main__':

    test = Test()
    test.launch()
    while 1:
        time.sleep(1)

