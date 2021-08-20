from PyQt5.Qt import *
from PyQt5.QtCore import QTimer
import time


class OneJob(QObject):
    sign_started = pyqtSignal()
    sign_finished = pyqtSignal()

    def __init__(self, timeout, job_name):
        super().__init__()
        self._timeout = timeout
        self._job_name = job_name
        self._ts_start = time.time()

    def start(self):
        self.sign_started.emit()
        print(f"{round(time.time() - self._ts_start, 2)}:[{self._job_name}] I am started...")
        QTimer().singleShot(self._timeout, self._i_am_finished)

    def _i_am_finished(self):
        print(f"{round(time.time() - self._ts_start, 2)}:[{self._job_name}] I am finished...")
        self.sign_finished.emit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    job_1 = OneJob(timeout=1000, job_name="hi")
    job_1.start()

    sys.exit(app.exec_())
