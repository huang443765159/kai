"""
单例的类初始化的时候不能加参数，如果加了参数，谁先实例化参数就是谁
以下为测试代码
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

    def __init__(self, test_callback: Callable):
        self._test_callback = test_callback
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        num = 0
        while 1:
            num += 1
            self._test_callback(num=num)
            time.sleep(1)


class Test1:

    def __init__(self):
        self._test = Test(test_callback=self._test_callback)

    def _test_callback(self, num: int):
        print(1, num)


class Test2:

    def __init__(self):
        self._test = Test(test_callback=self._test_callback)

    def _test_callback(self, num: int):
        print(2, num)


if __name__ == '__main__':
    test1 = Test1()
    test2 = Test2()
    while 1:
        time.sleep(1)
