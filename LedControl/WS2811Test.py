import sys
sys.path.append('/home/pi/Desktop')
import time
import board
import neopixel
from PyQt5.QtWidgets import QMainWindow
from LedControl.UI.UI import Ui_MainWindow


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # NEO
        self._pixels = neopixel.NeoPixel(board.D18, 100)
        self._pixels.fill((0, 255, 0))
        # BTN
        self._ui.btn_r.clicked.connect(self._set_r)
        self._ui.btn_g.clicked.connect(self._set_g)
        self._ui.btn_b.clicked.connect(self._set_b)
        self._ui.btn_blink.clicked.connect(self._set_blink)

    def _set_r(self):
        for i in range(100):
            self._pixels[i] = (255, 0, 0)

    def _set_g(self):
        for i in range(100):
            self._pixels[i] = (0, 255, 0)

    def _set_b(self):
        for i in range(100):
            self._pixels[i] = (0, 0, 255)

    def _set_blink(self):
        for i in range(100):
            self._pixels[i * 3] = (100, 0, 0)
            time.sleep(0.1)
            self._pixels[i * 3 - 1] = (0, 100, 0)
            time.sleep(0.1)
            self._pixels[i * 3 - 2] = (0, 0, 100)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit(app.exec_())
