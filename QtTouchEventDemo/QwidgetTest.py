from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QEvent
import types


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        # WIDGET
        self._widget = QWidget(self)
        self._widget.setAttribute(Qt.WA_TranslucentBackground)
        self.setCentralWidget(self._widget)
        self.resize(900, 900)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)
        # BUTTON WIDGET
        widget = QWidget(self._widget)
        widget.resize(200, 200)
        widget.setStyleSheet('QWidget {background: red}')
        widget.setToolTip('button test')
        button = QPushButton(widget)
        button.setStyleSheet('QPushButton {background: blue}')
        button.setText('test')
        button.clicked.connect(lambda: print('clicked'))

    @staticmethod
    def _handle_event(widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            print(touch_points)
            widget.update()
        return True


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())
