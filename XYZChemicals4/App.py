import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from example.Gui.Gui import Gui
from example.QTools import QTools
from example.Gui.UI.UI import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)
        # QApplication.setStyle('Fusion')
        # QApplication.setPalette(QTools.get_default_palette())
        QTools.font_size_auto_adapt(qt_ui=self._ui)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
