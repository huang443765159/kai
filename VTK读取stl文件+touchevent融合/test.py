from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QToolBox
from PyQt5.QtCore import Qt, QObject, pyqtSignal


class One(QObject):

    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self._board = QWidget(self._parent)
        self._board.resize(300, 300)
        self._board.setStyleSheet('QWidget {background-color: rgb(60, 60, 60)}')
        self._board.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint)
        # BUTTON
        self._button = QPushButton(self._parent)
        self._button.resize(30, 30)
        self._button.move(50, 50)
        self._button.setText('ok')
        self._button.setStyleSheet('QPushButton {background: rgb(255, 255, 255)}')
        self._button.pressed.connect(self._pressed)
        self._button.released.connect(self._released)
        # TEST_WIDGET
        self._test_widget1 = QToolBox(self._parent)
        self._test_widget1.resize(100, 100)
        self._button.show()
        self._test_widget1.show()
        self._board.show()

    def _pressed(self):
        self._test_widget1.setStyleSheet('QToolBox {background-color: rgb(255, 0, 0)}')
        self._test_widget1.setVisible(True)
        self._button.setText('Pressed')

    def _released(self):
        self._test_widget1.setVisible(False)
        self._button.setText('Released')
