# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.test_fun_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.test_fun_log.setGeometry(QtCore.QRect(10, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.test_fun_log.setFont(font)
        self.test_fun_log.setObjectName("test_fun_log")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_connected = QtWidgets.QCheckBox(self.centralwidget)
        self.btn_connected.setGeometry(QtCore.QRect(100, 0, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_connected.setFont(font)
        self.btn_connected.setObjectName("btn_connected")
        self.btn_tcp_works = QtWidgets.QCheckBox(self.centralwidget)
        self.btn_tcp_works.setGeometry(QtCore.QRect(10, 0, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_tcp_works.setFont(font)
        self.btn_tcp_works.setChecked(True)
        self.btn_tcp_works.setObjectName("btn_tcp_works")
        self.ip_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_edit.setGeometry(QtCore.QRect(50, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ip_edit.setFont(font)
        self.ip_edit.setObjectName("ip_edit")
        self.port_eidt = QtWidgets.QLineEdit(self.centralwidget)
        self.port_eidt.setGeometry(QtCore.QRect(50, 50, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.port_eidt.setFont(font)
        self.port_eidt.setObjectName("port_eidt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.type_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.type_edit.setGeometry(QtCore.QRect(50, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.type_edit.setFont(font)
        self.type_edit.setObjectName("type_edit")
        self.error_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.error_log.setGeometry(QtCore.QRect(10, 380, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.error_log.setFont(font)
        self.error_log.setObjectName("error_log")
        self.event_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.event_log.setGeometry(QtCore.QRect(10, 290, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.event_log.setFont(font)
        self.event_log.setObjectName("event_log")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 450, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.data_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.data_log.setGeometry(QtCore.QRect(10, 200, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data_log.setFont(font)
        self.data_log.setObjectName("data_log")
        self.btn_welcome = QtWidgets.QPushButton(self.centralwidget)
        self.btn_welcome.setGeometry(QtCore.QRect(0, 90, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_welcome.setFont(font)
        self.btn_welcome.setObjectName("btn_welcome")
        self.btn_forward = QtWidgets.QPushButton(self.centralwidget)
        self.btn_forward.setGeometry(QtCore.QRect(100, 90, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_forward.setFont(font)
        self.btn_forward.setObjectName("btn_forward")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(0, 120, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(100, 120, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.btn_wash_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_wash_start.setGeometry(QtCore.QRect(0, 150, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_wash_start.setFont(font)
        self.btn_wash_start.setObjectName("btn_wash_start")
        self.btn_wash_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_wash_end.setGeometry(QtCore.QRect(100, 150, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_wash_end.setFont(font)
        self.btn_wash_end.setObjectName("btn_wash_end")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ip"))
        self.label_2.setText(_translate("MainWindow", "port"))
        self.btn_connected.setText(_translate("MainWindow", "CONNECTED"))
        self.btn_tcp_works.setText(_translate("MainWindow", "TCP WORKS"))
        self.label_3.setText(_translate("MainWindow", "type"))
        self.label_4.setText(_translate("MainWindow", "Test Fun"))
        self.label_5.setText(_translate("MainWindow", "error"))
        self.label_6.setText(_translate("MainWindow", "event"))
        self.label_7.setText(_translate("MainWindow", "data"))
        self.btn_welcome.setText(_translate("MainWindow", "Welcome"))
        self.btn_forward.setText(_translate("MainWindow", "Forward"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_wash_start.setText(_translate("MainWindow", "Wash Start"))
        self.btn_wash_end.setText(_translate("MainWindow", "Wash End"))
