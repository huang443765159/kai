from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
import time


class TimerOutput(QObject):

    sign_output = pyqtSignal(float, int)

    def __init__(self):
        super().__init__()
        # THREAD
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        # DATA
        self._ts_sleep = 1
        self._num_stand = 1

    @pyqtSlot()
    def _working(self):
        x = 0
        ts_start = time.time()
        while 1:
            x += 1
            # print('{:.2f} {}'.format(time.time()-ts_start, self._num_stand * x))
            self.sign_output.emit(time.time()-ts_start, self._num_stand * x)
            time.sleep(self._ts_sleep)

    def start(self, sleep_time, num_stand):
        self._ts_sleep = sleep_time
        self._num_stand = num_stand
        self._thread.start()


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    def report(ts, num):
        print('{:.2f} {}'.format(ts, num))

    outer_1 = TimerOutput()
    outer_2 = TimerOutput()

    outer_1.sign_output.connect(report)
    outer_2.sign_output.connect(report)

    outer_1.start(sleep_time=1, num_stand=1)
    outer_2.start(sleep_time=2, num_stand=100)

    sys.exit(app.exec_())
