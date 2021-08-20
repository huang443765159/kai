# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flo = QtWidgets.QTextBrowser(self.centralwidget)
        self.flo.setGeometry(QtCore.QRect(10, 70, 100, 110))
        self.flo.setObjectName("flo")
        self.flo1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.flo1.setGeometry(QtCore.QRect(130, 70, 100, 111))
        self.flo1.setObjectName("flo1")
        self.btn_output = QtWidgets.QPushButton(self.centralwidget)
        self.btn_output.setGeometry(QtCore.QRect(0, 30, 113, 32))
        self.btn_output.setObjectName("btn_output")
        self.btn_output1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_output1.setGeometry(QtCore.QRect(120, 30, 113, 32))
        self.btn_output1.setObjectName("btn_output1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_output.setText(_translate("MainWindow", "start"))
        self.btn_output1.setText(_translate("MainWindow", "start1"))
