from PyQt5.QtWidgets import QMainWindow, QApplication
from QtCss.UI.UI import Ui_MainWindow
from PyQt5.QtGui import QPalette, QColor


class QtCss(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setText('LED')
        self._clicked = False
        # PALETTE
        self._pal = self.pushButton.palette()
        self._pal.setColor(QPalette.Button, QColor('red'))
        self.pushButton.setPalette(self._pal)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.clicked.connect(self._button_click)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);")

    def _button_click(self):
        if not self._clicked:
            self._pal.setColor(QPalette.Button, QColor(255, 124, 189))
        else:
            self._pal.setColor(QPalette.Button, QColor(100, 234, 210))
        self.pushButton.setPalette(self._pal)
        self.pushButton.setAutoFillBackground(True)
        self._clicked = not self._clicked


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 必须设置，不然button颜色不会改变
    _test = QtCss()
    _test.show()

    sys.exit(app.exec_())
