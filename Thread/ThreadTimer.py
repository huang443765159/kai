import threading


class Hello(object):

    def __init__(self, num):
        self._num = num

    def get_num(self):
        return self._num


class ThreadTimer(Hello):

    def __init__(self, num):
        super(ThreadTimer, self).__init__(num=num)
        self._timer = threading.Timer(3, self._working)
        print(threading.current_thread())

    def _working(self):
        print('hello', threading.current_thread())
        print(self.get_num())

    def start(self):
        self._timer.start()

    def stop(self):
        self._timer.cancel()


if __name__ == '__main__':
    test = ThreadTimer(num=1)
    test.start()
