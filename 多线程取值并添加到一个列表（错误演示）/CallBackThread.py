from 多线程取值并添加到一个列表.Thread import Test
# import threading


class Test2(object):

    def __init__(self, data_cb):
        self._data_ = data_cb

        self._test1 = Test(1, self._data_cb_, 1)
        self._test2 = Test(2, self._data_cb_1, 100)
        self._test_list = [None, None]
        self._test1.start()
        self._test2.start()

    def _data_cb_(self, name, data):
        # global data_list
        # data_list[0] = name, data
        self._test_list[0] = (name, data)
        # print(threading.currentThread())

    def _data_cb_1(self, name, data):
        # global data_list
        # data_list[1] = name, data
        self._test_list[1] = (name, data)
        # print(threading.currentThread())

    def get_data(self):
        # self._data_(data=data_list)
        self._data_(data=self._test_list)


if __name__ == '__main__':
    import time

    def _get_data(data):
        ts_start = time.time()
        while time.time() - ts_start <= 1:
            print(data[0][0], data[0][1], data[1][0], data[1][1])
            time.sleep(1/8)

    test = Test2(_get_data)
    test.get_data()