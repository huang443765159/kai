from PyQt5.QtWidgets import QMainWindow
from practice.ok import Module
from GUI_Thread_V1.UI.Ui import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot


class Gui(QMainWindow, Ui_MainWindow):  # 建立qt界面环境

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.module = Module()  # 建立Module的实例
        self.module1 = Module()
        self.module.sign_output.connect(self.report)
        self.module1.sign_output1.connect(self.report1)

    def report(self, ts, num):
        self.ui_log_1.append('{:.2f} {}'.format(ts, num))

    def report1(self, ts, num):
        self.lineEdit.setText('{:.2f} {}'.format(ts, num))

    @pyqtSlot()
    def on_btn_start_1_clicked(self):
        self.module.start()

    @pyqtSlot()
    def on_btn_start_2_clicked(self):
        self.module1.start()


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    gui = Gui()
    gui.show()

    sys.exit(app.exec_())
