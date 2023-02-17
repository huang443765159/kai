import pyqtgraph as pg
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGraphicsLineItem, QFrame, QPushButton

from LineUi import Ui_MainWindow


class DrawChat(QMainWindow):

    def __init__(self):
        super(DrawChat, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        widget = QWidget(self)
        widget.resize(500, 500)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setParent(widget)
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self._count = 11

        self.timer3 = pg.QtCore.QTimer()
        self.timer3.timeout.connect(self.cUpdate)
        self.timer3.start(200)

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        pos = a0.pos()
        print(pos)

    def cUpdate(self):
        print(1, self._count)
        self.graphWidget.plot([self._count], [6], pen=None, symbol='o', name='eeee')
        self._count += 1


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    draw = DrawChat()
    draw.show()
    app.exec_()
