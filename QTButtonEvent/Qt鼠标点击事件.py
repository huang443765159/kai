import sys
import types
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

# handle_event和原widget的点击事件不可共存, 注掉16/17行即可正常运行


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.event = types.MethodType(self._handle_event, self._widget)
        self._widget.setAttribute(Qt.WA_AcceptTouchEvents)
        self._widget.resize(500, 500)
        self._widget.show()
        self.resize(500, 500)

    def _handle_event(self, w, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                print('left button pressed')
                print(event.x(), event.y())  # 鼠标位置
        if event.type() == QEvent.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                print('left button released')
        w.update()
        return True

    def mousePressEvent(self, event):
        print('mouse pressed')

    def mouseReleaseEvent(self, event):
        print('mouse release')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
