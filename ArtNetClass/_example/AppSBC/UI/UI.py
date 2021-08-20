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
        MainWindow.resize(201, 131)
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.channel = QtWidgets.QSpinBox(self.groupBox)
        self.channel.setGeometry(QtCore.QRect(60, 20, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.channel.setFont(font)
        self.channel.setObjectName("channel")
        self.btn_r = QtWidgets.QPushButton(self.groupBox)
        self.btn_r.setGeometry(QtCore.QRect(20, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_r.setFont(font)
        self.btn_r.setObjectName("btn_r")
        self.btn_g = QtWidgets.QPushButton(self.groupBox)
        self.btn_g.setGeometry(QtCore.QRect(60, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_g.setFont(font)
        self.btn_g.setObjectName("btn_g")
        self.btn_b = QtWidgets.QPushButton(self.groupBox)
        self.btn_b.setGeometry(QtCore.QRect(100, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_b.setFont(font)
        self.btn_b.setObjectName("btn_b")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(23, 24, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_blink = QtWidgets.QCheckBox(self.groupBox)
        self.btn_blink.setGeometry(QtCore.QRect(20, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_blink.setFont(font)
        self.btn_blink.setObjectName("btn_blink")
        self.btn_all = QtWidgets.QCheckBox(self.groupBox)
        self.btn_all.setGeometry(QtCore.QRect(120, 0, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_all.setFont(font)
        self.btn_all.setObjectName("btn_all")
        self.btn_color = QtWidgets.QPushButton(self.groupBox)
        self.btn_color.setGeometry(QtCore.QRect(140, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_color.setFont(font)
        self.btn_color.setObjectName("btn_color")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBC"))
        self.groupBox.setTitle(_translate("MainWindow", "LED"))
        self.btn_r.setText(_translate("MainWindow", "R"))
        self.btn_g.setText(_translate("MainWindow", "G"))
        self.btn_b.setText(_translate("MainWindow", "B"))
        self.label.setText(_translate("MainWindow", "CH"))
        self.btn_blink.setText(_translate("MainWindow", "BLINK"))
        self.btn_all.setText(_translate("MainWindow", "ALL"))
        self.btn_color.setText(_translate("MainWindow", "CF"))