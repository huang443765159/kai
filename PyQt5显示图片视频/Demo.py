import cv2
import threading
from typing import Callable

import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QWidget, QLabel


class Camera:

    def __init__(self, callback: Callable):
        self._callback = callback
        self._cap = cv2.VideoCapture(0)
        self._thread = threading.Thread(target=self._working, daemon=True)
        self._thread_switch = True
        self._thread.start()

    def _working(self):
        while self._thread_switch:
            ret, frame = self._cap.read()
            if ret:
                self._callback(frame)


class Gui(QMainWindow):

    def __init__(self):
        super(Gui, self).__init__()
        self.resize(1000, 1000)
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.resize(1000, 1000)
        self._label = QLabel(self._widget)
        self._label.resize(1000, 1000)
        self._camera = Camera(callback=self._callback)

    def _callback(self, frame: np.ndarray):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5))
        image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self._label.setPixmap(QPixmap.fromImage(image))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Gui()
    win.show()
    sys.exit(app.exec_())
