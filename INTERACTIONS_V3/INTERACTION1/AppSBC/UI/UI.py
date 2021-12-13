# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 317)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_robot = QtWidgets.QGroupBox(self.centralwidget)
        self.group_robot.setGeometry(QtCore.QRect(0, 0, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.group_robot.setFont(font)
        self.group_robot.setObjectName("group_robot")
        self.btn_stop_all = QtWidgets.QToolButton(self.group_robot)
        self.btn_stop_all.setGeometry(QtCore.QRect(210, 20, 45, 54))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_stop_all.setFont(font)
        self.btn_stop_all.setObjectName("btn_stop_all")
        self.led_lb_bot = QtWidgets.QLabel(self.group_robot)
        self.led_lb_bot.setGeometry(QtCore.QRect(5, 20, 30, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.led_lb_bot.setFont(font)
        self.led_lb_bot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.led_lb_bot.setObjectName("led_lb_bot")
        self.led_ch_a = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_a.setGeometry(QtCore.QRect(100, 20, 21, 20))
        self.led_ch_a.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_a.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_a.setFont(font)
        self.led_ch_a.setToolTip("")
        self.led_ch_a.setToolTipDuration(-1)
        self.led_ch_a.setObjectName("led_ch_a")
        self.led_water_high = QtWidgets.QToolButton(self.group_robot)
        self.led_water_high.setGeometry(QtCore.QRect(80, 20, 21, 20))
        self.led_water_high.setMinimumSize(QtCore.QSize(0, 14))
        self.led_water_high.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_water_high.setFont(font)
        self.led_water_high.setToolTip("")
        self.led_water_high.setToolTipDuration(-1)
        self.led_water_high.setObjectName("led_water_high")
        self.led_ch_b = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_b.setGeometry(QtCore.QRect(120, 20, 21, 20))
        self.led_ch_b.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_b.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_b.setFont(font)
        self.led_ch_b.setToolTip("")
        self.led_ch_b.setToolTipDuration(-1)
        self.led_ch_b.setObjectName("led_ch_b")
        self.led_ch_whl = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_whl.setGeometry(QtCore.QRect(140, 20, 21, 20))
        self.led_ch_whl.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_whl.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_whl.setFont(font)
        self.led_ch_whl.setToolTip("")
        self.led_ch_whl.setToolTipDuration(-1)
        self.led_ch_whl.setObjectName("led_ch_whl")
        self.led_ch_wax = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_wax.setGeometry(QtCore.QRect(160, 20, 21, 20))
        self.led_ch_wax.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_wax.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_wax.setFont(font)
        self.led_ch_wax.setToolTip("")
        self.led_ch_wax.setToolTipDuration(-1)
        self.led_ch_wax.setObjectName("led_ch_wax")
        self.led_tcp_pump = QtWidgets.QToolButton(self.group_robot)
        self.led_tcp_pump.setGeometry(QtCore.QRect(180, 20, 16, 20))
        self.led_tcp_pump.setMinimumSize(QtCore.QSize(0, 14))
        self.led_tcp_pump.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_tcp_pump.setFont(font)
        self.led_tcp_pump.setToolTip("")
        self.led_tcp_pump.setToolTipDuration(-1)
        self.led_tcp_pump.setText("")
        self.led_tcp_pump.setObjectName("led_tcp_pump")
        self.group_robot_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_robot_2.setGeometry(QtCore.QRect(0, 90, 260, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.group_robot_2.setFont(font)
        self.group_robot_2.setObjectName("group_robot_2")
        self.btn_water = QtWidgets.QCheckBox(self.group_robot_2)
        self.btn_water.setGeometry(QtCore.QRect(10, 60, 60, 16))
        self.btn_water.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_water.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_water.setFont(font)
        self.btn_water.setChecked(False)
        self.btn_water.setObjectName("btn_water")
        self.btn_ch_a = QtWidgets.QCheckBox(self.group_robot_2)
        self.btn_ch_a.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.btn_ch_a.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_a.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_a.setFont(font)
        self.btn_ch_a.setChecked(False)
        self.btn_ch_a.setObjectName("btn_ch_a")
        self.btn_ch_b = QtWidgets.QCheckBox(self.group_robot_2)
        self.btn_ch_b.setGeometry(QtCore.QRect(10, 100, 60, 16))
        self.btn_ch_b.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_b.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_b.setFont(font)
        self.btn_ch_b.setChecked(False)
        self.btn_ch_b.setObjectName("btn_ch_b")
        self.btn_ch_whl = QtWidgets.QCheckBox(self.group_robot_2)
        self.btn_ch_whl.setGeometry(QtCore.QRect(10, 120, 60, 16))
        self.btn_ch_whl.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_whl.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_whl.setFont(font)
        self.btn_ch_whl.setChecked(False)
        self.btn_ch_whl.setObjectName("btn_ch_whl")
        self.btn_ch_wax = QtWidgets.QCheckBox(self.group_robot_2)
        self.btn_ch_wax.setGeometry(QtCore.QRect(10, 140, 60, 16))
        self.btn_ch_wax.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_wax.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_wax.setFont(font)
        self.btn_ch_wax.setChecked(False)
        self.btn_ch_wax.setObjectName("btn_ch_wax")
        self.table_liquids = QtWidgets.QTableWidget(self.group_robot_2)
        self.table_liquids.setGeometry(QtCore.QRect(70, 40, 180, 120))
        self.table_liquids.setObjectName("table_liquids")
        self.table_liquids.setColumnCount(2)
        self.table_liquids.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.table_liquids.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_liquids.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_liquids.setItem(1, 0, item)
        self.table_liquids.verticalHeader().setDefaultSectionSize(20)
        self.group_robot_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_robot_3.setGeometry(QtCore.QRect(0, 270, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.group_robot_3.setFont(font)
        self.group_robot_3.setObjectName("group_robot_3")
        self.guides_show = QtWidgets.QLabel(self.group_robot_3)
        self.guides_show.setGeometry(QtCore.QRect(60, 20, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.guides_show.setFont(font)
        self.guides_show.setAlignment(QtCore.Qt.AlignCenter)
        self.guides_show.setObjectName("guides_show")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOT1"))
        self.group_robot.setTitle(_translate("MainWindow", "DEVICE"))
        self.btn_stop_all.setText(_translate("MainWindow", "STOP\n"
"ALL"))
        self.led_lb_bot.setText(_translate("MainWindow", "BOT1"))
        self.led_ch_a.setText(_translate("MainWindow", "C1"))
        self.led_water_high.setText(_translate("MainWindow", "WAT"))
        self.led_ch_b.setText(_translate("MainWindow", "C2"))
        self.led_ch_whl.setText(_translate("MainWindow", "WHL"))
        self.led_ch_wax.setText(_translate("MainWindow", "WAX"))
        self.group_robot_2.setTitle(_translate("MainWindow", "LIQUID"))
        self.btn_water.setText(_translate("MainWindow", "0-WAT"))
        self.btn_ch_a.setText(_translate("MainWindow", "1-CH_A"))
        self.btn_ch_b.setText(_translate("MainWindow", "2-CH_B"))
        self.btn_ch_whl.setText(_translate("MainWindow", "3-WHL"))
        self.btn_ch_wax.setText(_translate("MainWindow", "4-WAX"))
        item = self.table_liquids.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "WATER"))
        item = self.table_liquids.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CH_A"))
        item = self.table_liquids.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "CH_B"))
        item = self.table_liquids.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CH_WHL"))
        item = self.table_liquids.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "CH_WAX"))
        item = self.table_liquids.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TS_REMAIN"))
        item = self.table_liquids.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LEVEL"))
        __sortingEnabled = self.table_liquids.isSortingEnabled()
        self.table_liquids.setSortingEnabled(False)
        self.table_liquids.setSortingEnabled(__sortingEnabled)
        self.group_robot_3.setTitle(_translate("MainWindow", "GUIDES"))
        self.guides_show.setText(_translate("MainWindow", "CURRENT_STAGE"))
