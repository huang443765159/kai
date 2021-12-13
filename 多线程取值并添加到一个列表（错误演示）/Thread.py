import threading
import time


class Test(object):

    def __init__(self, name, data_cb, num):

        self._name = name
        self._data_cb = data_cb
        self._num = num

        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True

    def _working(self):
        num = 0
        while 1:
            num += 1
            self._data_cb(name=self._name, data=self._num * num)
            time.sleep(1)

    def start(self):
        self._thread.start()


if __name__ == '__main__':

    data_list = [None, None]

    def data_cb_(name, data):
        global data_list
        # print(f'<DATA> {name} {data}')
        data_list[0] = (name, data)


    def data_cb_1(name, data):
        global data_list
        # print(f'<DATA> {name} {data}')
        data_list[1] = (name, data)

    def get_data():
        print(data_list)

    test1 = Test(1, data_cb_, 1)
    test2 = Test(2, data_cb_1, 100)

    test1.start()
    test2.start()

    while 1:
        time.sleep(1)
        get_data()
