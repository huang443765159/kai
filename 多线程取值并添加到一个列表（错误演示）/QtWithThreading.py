from PyQt5.QtCore import QObject
import threading
import time


class Test(object):

    def __init__(self, id, num):
        super().__init__()
        self._id = id
        self._num = num

    def get_id(self):
        print(self._id, self._num)
    #     self._thread = threading.Thread(target=self._working)
    #     self._thread.daemon = True
    #     self._thread.start()
    #
    # def _working(self):
    #     while 1:
    #         print(self._id, self._num)
    #         time.sleep(1)


class Test2(QObject):

    def __init__(self):
        super().__init__()
        self._test = dict()
        for i in range(1, 3):
            self._test[i] = Test(id=i, num=i*10)
        self._thread = threading.Thread(target=self._working)
        self._thread.daemon = True
        self._thread.start()

    def _working(self):
        while 1:
            for test in self._test.values():
                test.get_id()
                time.sleep(1)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    test = Test2()

    sys.exit(app.exec_())
