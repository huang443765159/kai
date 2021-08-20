from PyQt5.QtWidgets import QMainWindow, QApplication
from QtQpalete.UI.UI import Ui_MainWindow
from PyQt5.QtGui import QPalette, QColor


class QtCss(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._clicked = False
        # PALETTE
        self._pal = self.btn_led.palette()
        self._pal.setColor(QPalette.Button, QColor('red'))
        self.btn_led.setPalette(self._pal)
        self.btn_led.setAutoFillBackground(True)
        self.btn_led.clicked.connect(self._button_click)

    def _button_click(self):
        if not self._clicked:
            self._pal.setColor(QPalette.Button, QColor(255, 124, 189))
        else:
            self._pal.setColor(QPalette.Button, QColor(100, 234, 210))
        self.btn_led.setPalette(self._pal)
        self.btn_led.setAutoFillBackground(True)
        self._clicked = not self._clicked


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 必须设置，不然button颜色不会改变
    _test = QtCss()
    _test.show()

    sys.exit(app.exec_())
