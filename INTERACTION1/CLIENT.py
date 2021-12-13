import sys
# sys.path.append('/home/pi/Desktop/')
import signal
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from INTERACTION1.Core import Core
from INTERACTION1.GUI.UI.UI import Ui_MainWindow
from INTERACTION1.GUI.BasicClass.UILed import UILed
from INTERACTION1.GUI.GuiPumpsStation import GuiInteraction


class RaspGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._core = Core()
        # LED
        self.leds = dict()
        self.leds['PUMPS STATION'] = UILed(self.led_pumps_station, text='OFF')
        self.leds['WATER'] = UILed(self.led_water, text=' ')
        self.leds['ALKALI'] = UILed(self.led_alkali, text=' ')
        self.leds['ACID'] = UILed(self.led_acid, text=' ')
        self.leds['WHEEL'] = UILed(self.led_wheel, text=' ')
        self.leds['WAX'] = UILed(self.led_wax, text=' ')
        self._gui = GuiInteraction(ui=self, core=self._core)
        # SIGNAL
        signal.signal(signal.SIGINT, self.closeEvent)

    def closeEvent(self, event_signum=None, frame=None):
        self._core.exit()
        self.close()

    @pyqtSlot()
    def on_btn_power_off_clicked(self):
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(10)
        dialog = QMessageBox(None)
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
        dialog.setText('POWER OFF')
        dialog.setIcon(QMessageBox.Warning)
        dialog.setStandardButtons(QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.Close)
        btn_cancel = dialog.button(QMessageBox.Cancel)
        btn_cancel.setText('CANCEL')
        btn_cancel.setFont(font)
        btn_reset = dialog.button(QMessageBox.Reset)
        btn_reset.setText('RESET')
        btn_reset.setFont(font)
        btn_close = dialog.button(QMessageBox.Close)
        btn_close.setText('POWER OFF')
        btn_close.setFont(font)
        dialog.exec_()
        dialog.activateWindow()
        btn_clicked = dialog.clickedButton()
        if btn_clicked == btn_cancel:
            pass
        elif btn_clicked == btn_reset:
            pass
        elif btn_clicked == btn_close:
            self.closeEvent()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _gui = RaspGui()
    _gui.show()

    sys.exit(app.exec_())
