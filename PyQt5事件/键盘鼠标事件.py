import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


class AppWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('鼠标事件')
        self.setCentralWidget(QWidget())
        self.statusBar().showMessage('ready')
        self.resize(500, 500)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        key = a0.key()
        if key == Qt.Key_Up:
            print(1)
        elif key == Qt.Key_Left:
            print(2)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        pos = a0.pos()
        btn = a0.button()
        if btn == Qt.LeftButton:
            print('Left Button')
        elif btn == Qt.RightButton:
            print('Right Button')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())
