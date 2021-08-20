from PyQt5.QtWidgets import QMainWindow
from QTChangeColor.UI.UI import Ui_MainWindow
from QTChangeColor.UILed import UILed


class Test(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # LED
        self.btn_water_inflow.stateChanged.connect(self._switch)
        self._led = UILed(self.led_water_inflow, text='False')

    def _switch(self, switch):
        color = 'GREEN' if switch else 'RED'
        text = 'True' if switch else 'False'
        self._led.set_appearance(color=color, text=text)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    test = Test()
    test.show()

    sys.exit(app.exec_())
