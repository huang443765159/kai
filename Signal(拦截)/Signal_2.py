import signal
from PyQt5.QtWidgets import QMainWindow


class Signal(QMainWindow):

    def __init__(self):
        super().__init__()

        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self.close()


#  之有GUI才有close()函数
