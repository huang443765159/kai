# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_install = QtWidgets.QToolButton(self.centralwidget)
        self.btn_install.setGeometry(QtCore.QRect(235, 455, 191, 22))
        self.btn_install.setObjectName("btn_install")
        self.table_libs = QtWidgets.QTableWidget(self.centralwidget)
        self.table_libs.setGeometry(QtCore.QRect(10, 10, 421, 438))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_libs.setFont(font)
        self.table_libs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_libs.setObjectName("table_libs")
        self.table_libs.setColumnCount(4)
        self.table_libs.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_libs.setItem(7, 1, item)
        self.table_libs.horizontalHeader().setDefaultSectionSize(100)
        self.table_libs.horizontalHeader().setMinimumSectionSize(19)
        self.table_libs.verticalHeader().setDefaultSectionSize(22)
        self.btn_check_libs = QtWidgets.QToolButton(self.centralwidget)
        self.btn_check_libs.setGeometry(QtCore.QRect(30, 455, 191, 22))
        self.btn_check_libs.setObjectName("btn_check_libs")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(121, 10, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_install.setText(_translate("MainWindow", "INSTALL"))
        item = self.table_libs.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_libs.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_libs.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_libs.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_libs.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_libs.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_libs.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.table_libs.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.table_libs.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.table_libs.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        item = self.table_libs.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "10"))
        item = self.table_libs.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "11"))
        item = self.table_libs.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "12"))
        item = self.table_libs.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "13"))
        item = self.table_libs.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "14"))
        item = self.table_libs.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "15"))
        item = self.table_libs.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "16"))
        item = self.table_libs.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "17"))
        item = self.table_libs.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "18"))
        item = self.table_libs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LIBS"))
        item = self.table_libs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VERSION"))
        item = self.table_libs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LATEST_VERSION"))
        item = self.table_libs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IS_INSTALLED"))
        __sortingEnabled = self.table_libs.isSortingEnabled()
        self.table_libs.setSortingEnabled(False)
        self.table_libs.setSortingEnabled(__sortingEnabled)
        self.btn_check_libs.setText(_translate("MainWindow", "CHECK_LIBS"))
