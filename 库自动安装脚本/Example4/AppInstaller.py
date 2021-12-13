import sys
sys.path.append('/home/xyz/Documents')
from PyQt5.QtWidgets import QMainWindow

from Example4.ToolInstaller.Gui.Gui import Gui
from Example4.ToolInstaller.Gui.UI.UI import Ui_MainWindow

"""
注：启动程序前需先配置好git上的ssh密钥
原因：现在无法使用https直接拉取git工程
"""


class AppTool(QMainWindow):

    def __init__(self):
        super(AppTool, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    tool = AppTool()
    tool.show()
    sys.exit(app.exec_())
