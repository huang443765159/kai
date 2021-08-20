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
        MainWindow.resize(304, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_1.setGeometry(QtCore.QRect(0, 20, 113, 32))
        self.btn_start_1.setObjectName("btn_start_1")
        self.btn_stop_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop_1.setGeometry(QtCore.QRect(170, 20, 113, 32))
        self.btn_stop_1.setObjectName("btn_stop_1")
        self.btn_start_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_2.setGeometry(QtCore.QRect(10, 280, 113, 32))
        self.btn_start_2.setObjectName("btn_start_2")
        self.btn_stop_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop_2.setGeometry(QtCore.QRect(170, 280, 113, 32))
        self.btn_stop_2.setObjectName("btn_stop_2")
        self.ui_log_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ui_log_1.setGeometry(QtCore.QRect(10, 70, 281, 181))
        self.ui_log_1.setObjectName("ui_log_1")
        self.ui_log_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ui_log_2.setGeometry(QtCore.QRect(10, 340, 281, 192))
        self.ui_log_2.setObjectName("ui_log_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 60, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start_1.setText(_translate("MainWindow", "start"))
        self.btn_stop_1.setText(_translate("MainWindow", "stop"))
        self.btn_start_2.setText(_translate("MainWindow", "start"))
        self.btn_stop_2.setText(_translate("MainWindow", "stop"))
        self.label.setText(_translate("MainWindow", "data_log1"))
        self.label_2.setText(_translate("MainWindow", "data_log2"))
