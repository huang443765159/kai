from GUI_Thread_V1.UI.UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from practice.ok import Module


class Gui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # call
        self.setupUi(self)
        #
        self.module_1 = Module()
        self.module_2 = Module()
        self.module_1.sign_output.connect(self.report_1)
        self.module_2.sign_output.connect(self.report_2)

    def report_1(self, ts, num):
        self.ui_log_1.append('{:.2f}, {}'.format(ts, num))

    def report_2(self, ts, num):
        self.ui_log_2.append('{:.2f}, {}'.format(ts, num))

    @pyqtSlot()
    def on_btn_start_1_clicked(self):
        self.module_1.start()

    @pyqtSlot()
    def on_btn_stop_1_clicked(self):
        self.module_1.stop()

    @pyqtSlot()
    def on_btn_start_2_clicked(self):
        self.module_2.start()

    @pyqtSlot()
    def on_btn_stop_2_clicked(self):
        self.module_2.stop()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    gui = Gui()
    gui.show()

    sys.exit(app.exec_())
