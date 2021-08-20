from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class MousePos(QMainWindow):

    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        # MOUSE_POS
        self._mouse_pos = self._widget.mapFromGlobal(QCursor.pos())
        print(self._mouse_pos.x(), self._mouse_pos.y())
