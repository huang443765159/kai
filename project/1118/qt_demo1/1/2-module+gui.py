from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject
import time


class ModuleThread(QObject):

    sign_output = pyqtSignal(float, int)  # time, num

    def __init__(self):
        super().__init__()
        # Thread
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        # self._thread.finished.connect(lambda: print('Finished'))
        self._thread_switch = False

    @pyqtSlot()
    def _working(self):
        num = 0
        while self._thread_switch:
            self.sign_output.emit(time.time(), num)
            num += 1
            time.sleep(1)
            #  放在最后

    def start(self):
        if self._thread_switch is False:
            self._thread_switch = True
            self._thread.start()

    def stop(self):
        self._thread_switch = False
        self._thread.quit()
        #  在调用的瞬间，就开启关闭，所以导致阻塞，等开启完成之后才关闭，但是是先执行的stop


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # Func
    def _report(ts, num):
        print('<{:.2f}> {}'.format(ts, num))

    # Main
    module = ModuleThread()
    module.sign_output.connect(_report)
    module.start()

    sys.exit(app.exec_())

