# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 160)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GUI_SCAN = QtWidgets.QGroupBox(self.centralwidget)
        self.GUI_SCAN.setGeometry(QtCore.QRect(0, 0, 280, 50))
        self.GUI_SCAN.setObjectName("GUI_SCAN")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.GUI_SCAN)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 260, 30))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_add_sphere = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.btn_add_sphere.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_add_sphere.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.btn_add_sphere.setObjectName("btn_add_sphere")
        self.gridLayout_5.addWidget(self.btn_add_sphere, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 260, 30))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btn_quit = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        self.btn_quit.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_quit.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.btn_quit.setObjectName("btn_quit")
        self.gridLayout_6.addWidget(self.btn_quit, 0, 0, 1, 1)
        self.btn_add_line = QtWidgets.QToolButton(self.centralwidget)
        self.btn_add_line.setGeometry(QtCore.QRect(10, 100, 261, 21))
        self.btn_add_line.setObjectName("btn_add_line")
        self.btn_remove_line = QtWidgets.QToolButton(self.centralwidget)
        self.btn_remove_line.setGeometry(QtCore.QRect(10, 130, 261, 22))
        self.btn_remove_line.setObjectName("btn_remove_line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GUI_SCAN.setTitle(_translate("MainWindow", "VTK"))
        self.btn_add_sphere.setText(_translate("MainWindow", "ADD_ONE_SPHERE"))
        self.btn_quit.setText(_translate("MainWindow", "QUIT"))
        self.btn_add_line.setText(_translate("MainWindow", "ADD_LINE"))
        self.btn_remove_line.setText(_translate("MainWindow", "REMOVE_LINE"))
