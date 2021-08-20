"""
写一个列表，把callback填进去，如果想拿不同的参数，建议不要使用单例

"""


import time
import threading
from typing import Callable


def singleton(cls):
    _instance = dict()

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    _singleton: type(cls)
    return _singleton


@singleton
class Test:

    def __init__(self):
        self._test_callback = list()
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        num = 0
        while 1:
            num += 1
            for cb in self._test_callback:
                cb(num=num)
            time.sleep(1)

    def register_callback(self, test_callback: Callable):
        self._test_callback.append(test_callback)


class Test1:

    def __init__(self):
        self._test = Test()
        self._test.register_callback(test_callback=self._test_callback)

    def _test_callback(self, num: int):
        print(1, num)


class Test2:

    def __init__(self):
        self._test = Test()
        self._test.register_callback(test_callback=self._test_callback)

    def _test_callback(self, num: int):
        print(2, num)


if __name__ == '__main__':
    test1 = Test1()
    test2 = Test2()
    while 1:
        time.sleep(1)
