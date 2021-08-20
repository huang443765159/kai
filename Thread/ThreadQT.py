from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread
import time


class Thread(QObject):

    sign_data = pyqtSignal(int)  # data

    def __init__(self):
        super().__init__()
        self._thread = QThread()
        self.moveToThread(self._thread)
        self._thread.started.connect(self._working)
        self._thread.start()
        self._thread_switch = True

    @pyqtSlot()
    def _working(self):
        num = 0
        while self._thread_switch:
            num += 1
            print(num)
            self.sign_data.emit(num)
            time.sleep(1)

    def start(self):
        self._thread_switch = True
        self._thread.start()

    def stop(self):
        self._thread_switch = False
        self._thread.quit()
        self._thread.wait()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication  # 终端ssh无法启动带Qwidget的程序，换成QtCore内的QCoreApplication即可
    from PyQt5.QtCore import QCoreApplication

    app = QCoreApplication(sys.argv)
    thread = Thread()
    thread.sign_data.connect(lambda x: print('SIGNAL', x))

    sys.exit(app.exec_())

