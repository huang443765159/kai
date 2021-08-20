import sys
sys.path.append('Desktop')
from PyQt5.QtCore import Qt
import vtkmodules.all as vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5 import QtGui
from QtabWidget.UI.UI import Ui_Form
from QtabWidget.UI.UI2 import Ui_hello


class Test(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.resize(1000, 1000)
        self._widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # VTK
        self._vtk_widget = QVTKRenderWindowInteractor(self._widget)
        self._vtk_widget.SetInteractorStyle(vtk.vtkInteractorStyleMultiTouchCamera())
        self._vtk_widget.resize(1000, 1000)
        self.setWindowFlags(Qt.NoDropShadowWindowHint)
        # PAINTER
        # UI
        self._ui = Ui_Form()
        self._ui.setupUi(self._widget)
        self._ui.widget.move(30, 30)
        self._ui.widget.setVisible(False)
        self._ui.widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # 设置边边的颜色
        self._pal = self._ui.widget.palette()
        self._pal.setColor(QPalette.Background, QtGui.QColor(0, 0, 0))
        self._ui.widget.setAutoFillBackground(True)  # 把QTapWidget的边边拿出来
        self._ui.widget.setPalette(self._pal)

        self._ui2 = Ui_hello()
        self._ui2.setupUi(self._widget)
        self._ui2.widget.move(30, 200)
        self._ui2.widget.setVisible(False)
        self._ui2.widget.setWindowFlags(Qt.NoDropShadowWindowHint)
        # BTN
        self._btn1 = QPushButton('BTN1', self._widget)
        self._btn1.resize(50, 70)
        self._btn1.move(500, 50)
        self._btn1.show()
        self._btn2 = QPushButton('BTN2', self._widget)
        self._btn2.resize(50, 70)
        self._btn2.move(500, 150)
        self._btn2.show()
        # SIGNAL
        self._btn1.clicked.connect(self._set_widget1_visible)
        self._btn2.clicked.connect(self._set_widget2_visible)
        # ATTR
        self._ui_ena = False
        self._ui_ena2 = False
        sheet = """
             QTabWidget::tab-bar {
 background-color: black;
}

QTabBar::tab {
    background-color: black;
    border-color:white;
    font: bold 12px 'Arial';
    color: white;
    height:60px;

}
QTabBar::tab:!selected {
    background-color: black;
    color: white;
 }

 QTabWidget::pane { 
     position: absolute;
     background-color: black;
 }

            """
        self._ui.widget.setStyleSheet(sheet)
        self._ui2.widget.setAutoFillBackground(True)

    def _set_widget1_visible(self):
        self._ui_ena = not self._ui_ena
        self._ui.widget.setVisible(self._ui_ena)
        # self._ui.widget.move(5000, 5000) if not self._ui_ena else self._ui.widget.move(30, 30)

    def _set_widget2_visible(self):
        self._ui_ena2 = not self._ui_ena2
        self._ui2.widget.setVisible(self._ui_ena2)
        # self._ui2.widget.move(-5000, -5000) if not self._ui_ena2 else self._ui2.widget.move(30, 200)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    QApplication.setStyle('Fusion')
    test = Test()
    test.show()
    app.exit(app.exec_())
