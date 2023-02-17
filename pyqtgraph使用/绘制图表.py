import random

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # 从接收指令开始，做500ms检测，如果里面有3或者4个下降的
        acid_press = [1.1, 1.0, 0.9, 0.8, 0.7, 0.3, 0.0, 0.0, 0.0, 0.0, 0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        acid_stop_press = [1.1, 0.9, 0.8, 0.2, 0.1, 0.0]

        whl_start_press = [0.0, 0.1, 0.2, 0.3, 0.4, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
        whl_stop_press = [1.5, 1.1, 0.5, 0.2, 0.0, 0.0, 0.0]

        acid_stop_press1 = [1.1, 1.1, 0.8, 0.5, 0.3, 0.2, 0.1, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.7, 0.8, 0.9, 0.9, 0.9, 0.9]

        # plot data: x, y values
        self.graphWidget.plot(time, acid_press)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.drawLine(10, 0, 10, 200)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
