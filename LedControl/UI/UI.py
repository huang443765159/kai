# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 52)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_r = QtWidgets.QPushButton(self.centralwidget)
        self.btn_r.setGeometry(QtCore.QRect(40, 10, 113, 32))
        self.btn_r.setObjectName("btn_r")
        self.btn_g = QtWidgets.QPushButton(self.centralwidget)
        self.btn_g.setGeometry(QtCore.QRect(170, 10, 113, 32))
        self.btn_g.setObjectName("btn_g")
        self.btn_b = QtWidgets.QPushButton(self.centralwidget)
        self.btn_b.setGeometry(QtCore.QRect(310, 10, 113, 32))
        self.btn_b.setObjectName("btn_b")
        self.btn_blink = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blink.setGeometry(QtCore.QRect(450, 10, 113, 32))
        self.btn_blink.setObjectName("btn_blink")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_r.setText(_translate("MainWindow", "R"))
        self.btn_g.setText(_translate("MainWindow", "G"))
        self.btn_b.setText(_translate("MainWindow", "B"))
        self.btn_blink.setText(_translate("MainWindow", "Blimk"))