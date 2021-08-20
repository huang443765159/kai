from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5 import QtGui
import types
import math


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self.resize(1800, 1800)

        # TOUCH_EVENT
        self._points = list()
        self._scale = 1.0
        self._angle = 0.0
        self._shift_x = 0.0
        self._shift_y = 0.0
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)
        self._widget.setGeometry(QRect(30, 50, 1000, 1000))

    def _handle_event(self, widget, event):
        if event.type() in [QEvent.TouchBegin, QEvent.TouchUpdate, QEvent.TouchEnd]:
            touch_points = event.touchPoints()
            self._points[:] = list()
            if event.type() != QEvent.TouchEnd:
                for point in touch_points:
                    self._points.append(point.pos())
            if len(touch_points) == 2 and touch_points[0].state() == Qt.TouchPointMoved and touch_points[1].state() \
                    == Qt.TouchPointMoved:
                point1_new = touch_points[0].pos()
                point2_new = touch_points[1].pos()
                point1_old = touch_points[0].lastPos()
                point2_old = touch_points[1].lastPos()
                diff_point_new = point1_new - point2_new
                diff_point_old = point1_old = point2_old
                scale = math.sqrt((diff_point_new.x()**2 + diff_point_new.y()**2) / diff_point_old.x()**2 + diff_point_old.y()**2)
                self._scale += scale
                angle = math.atan2(diff_point_new.y(), diff_point_new.x()) - math.atan2(diff_point_old.y(), diff_point_old.x())
                self._angle += angle
                self._shift_x = point1_new.x() - scale * (math.cos(angle) * (point1_old.x() - self._shift_x) -
                                                          math.sin(angle) * (point1_old.y() - self._shift_y))
                self._shift_y = point1_new.y() - scale * (math.sin(angle) * (point1_old.x() - self._shift_x) -
                                                          math.sin(angle) * (point1_old.y() - self._shift_y))
            widget.update()
        elif event.type() == QEvent.Paint:
            painter = QtGui.QPainter(widget)
            painter.translate(self._shift_x, self._shift_y)
            painter.rotate(self._angle * 180 / math.pi)
            painter.scale(self._scale, self._scale)
            # painter.drawImage(QPoint(0, 0), self._visual)
            painter.resetTransform()
            painter.setBrush(QtGui.QBrush(Qt.black))
            print(len(self._points))
            if len(self._points) == 2:
                # self._visual.set_hud_text('TWO POINTS')
                print('two points')
            for point in self._points:
                painter.drawEllipse(point, 20, 20)
        return True


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    test = Test()
    test.show()
    sys.exit(app.exec_())
