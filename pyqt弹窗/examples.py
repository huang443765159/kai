import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("弹出式对话框例子")
        self.resize(400, 200)
        self.btn1 = QPushButton(self)
        self.btn1.setText("消息框")
        self.btn1.clicked.connect(self.msg1)
        layout = QVBoxLayout()

        self.btn2 = QPushButton(self)
        self.btn2.setText("问答对话框")
        self.btn2.clicked.connect(self.msg2)

        self.btn3 = QPushButton()
        self.btn3.setText("警告对话框")
        self.btn3.clicked.connect(self.msg3)

        self.btn4 = QPushButton()
        self.btn4.setText("严重错误对话框")
        self.btn4.clicked.connect(self.msg4)

        self.btn5 = QPushButton()
        self.btn5.setText("关于对话框")
        self.btn5.clicked.connect(self.msg5)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)

        self.setLayout(layout)

    def msg1(self):
        # 使用infomation信息框
        relay = QMessageBox.information(self, "车辆总数", "100", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(relay)

    def msg2(self):
        relay = QMessageBox.question(self, "标题", "问答消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(relay)

    def msg3(self):
        QMessageBox.warning(self, "标题", "警告消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg4(self):
        QMessageBox.critical(self, "标题", "严重错误消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def msg5(self):
        QMessageBox.about(self, "标题", "关于消息正文")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
