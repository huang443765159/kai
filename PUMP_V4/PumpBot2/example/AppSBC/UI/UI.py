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
        MainWindow.resize(187, 176)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_robot = QtWidgets.QGroupBox(self.centralwidget)
        self.group_robot.setGeometry(QtCore.QRect(0, 0, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.group_robot.setFont(font)
        self.group_robot.setObjectName("group_robot")
        self.btn_stop_all = QtWidgets.QToolButton(self.group_robot)
        self.btn_stop_all.setGeometry(QtCore.QRect(130, 40, 45, 54))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_stop_all.setFont(font)
        self.btn_stop_all.setObjectName("btn_stop_all")
        self.led_ch_a = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_a.setGeometry(QtCore.QRect(30, 20, 21, 20))
        self.led_ch_a.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_a.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_a.setFont(font)
        self.led_ch_a.setToolTip("")
        self.led_ch_a.setToolTipDuration(-1)
        self.led_ch_a.setObjectName("led_ch_a")
        self.led_water_high = QtWidgets.QToolButton(self.group_robot)
        self.led_water_high.setGeometry(QtCore.QRect(10, 20, 21, 20))
        self.led_water_high.setMinimumSize(QtCore.QSize(0, 14))
        self.led_water_high.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_water_high.setFont(font)
        self.led_water_high.setToolTip("")
        self.led_water_high.setToolTipDuration(-1)
        self.led_water_high.setObjectName("led_water_high")
        self.led_ch_b = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_b.setGeometry(QtCore.QRect(50, 20, 21, 20))
        self.led_ch_b.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_b.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_b.setFont(font)
        self.led_ch_b.setToolTip("")
        self.led_ch_b.setToolTipDuration(-1)
        self.led_ch_b.setObjectName("led_ch_b")
        self.led_ch_whl = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_whl.setGeometry(QtCore.QRect(70, 20, 21, 20))
        self.led_ch_whl.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_whl.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_whl.setFont(font)
        self.led_ch_whl.setToolTip("")
        self.led_ch_whl.setToolTipDuration(-1)
        self.led_ch_whl.setObjectName("led_ch_whl")
        self.led_ch_wax = QtWidgets.QToolButton(self.group_robot)
        self.led_ch_wax.setGeometry(QtCore.QRect(90, 20, 21, 20))
        self.led_ch_wax.setMinimumSize(QtCore.QSize(0, 14))
        self.led_ch_wax.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_ch_wax.setFont(font)
        self.led_ch_wax.setToolTip("")
        self.led_ch_wax.setToolTipDuration(-1)
        self.led_ch_wax.setObjectName("led_ch_wax")
        self.led_tcp_pump = QtWidgets.QToolButton(self.group_robot)
        self.led_tcp_pump.setGeometry(QtCore.QRect(110, 20, 16, 20))
        self.led_tcp_pump.setMinimumSize(QtCore.QSize(0, 14))
        self.led_tcp_pump.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_tcp_pump.setFont(font)
        self.led_tcp_pump.setToolTip("")
        self.led_tcp_pump.setToolTipDuration(-1)
        self.led_tcp_pump.setText("")
        self.led_tcp_pump.setObjectName("led_tcp_pump")
        self.btn_water = QtWidgets.QCheckBox(self.group_robot)
        self.btn_water.setGeometry(QtCore.QRect(0, 50, 60, 16))
        self.btn_water.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_water.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_water.setFont(font)
        self.btn_water.setChecked(False)
        self.btn_water.setObjectName("btn_water")
        self.btn_ch_a = QtWidgets.QCheckBox(self.group_robot)
        self.btn_ch_a.setGeometry(QtCore.QRect(60, 50, 60, 16))
        self.btn_ch_a.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_a.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_a.setFont(font)
        self.btn_ch_a.setChecked(False)
        self.btn_ch_a.setObjectName("btn_ch_a")
        self.btn_ch_b = QtWidgets.QCheckBox(self.group_robot)
        self.btn_ch_b.setGeometry(QtCore.QRect(0, 70, 60, 16))
        self.btn_ch_b.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_b.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_b.setFont(font)
        self.btn_ch_b.setChecked(False)
        self.btn_ch_b.setObjectName("btn_ch_b")
        self.btn_ch_whl = QtWidgets.QCheckBox(self.group_robot)
        self.btn_ch_whl.setGeometry(QtCore.QRect(60, 70, 60, 16))
        self.btn_ch_whl.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_whl.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_whl.setFont(font)
        self.btn_ch_whl.setChecked(False)
        self.btn_ch_whl.setObjectName("btn_ch_whl")
        self.btn_ch_wax = QtWidgets.QCheckBox(self.group_robot)
        self.btn_ch_wax.setGeometry(QtCore.QRect(0, 90, 60, 16))
        self.btn_ch_wax.setMinimumSize(QtCore.QSize(40, 16))
        self.btn_ch_wax.setMaximumSize(QtCore.QSize(70, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_wax.setFont(font)
        self.btn_ch_wax.setChecked(False)
        self.btn_ch_wax.setObjectName("btn_ch_wax")
        self.group_robot_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_robot_3.setGeometry(QtCore.QRect(0, 109, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_robot_3.setFont(font)
        self.group_robot_3.setObjectName("group_robot_3")
        self.guides_show = QtWidgets.QLabel(self.group_robot_3)
        self.guides_show.setGeometry(QtCore.QRect(10, 40, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.guides_show.setFont(font)
        self.guides_show.setAlignment(QtCore.Qt.AlignCenter)
        self.guides_show.setObjectName("guides_show")
        self.led_guides_1 = QtWidgets.QToolButton(self.group_robot_3)
        self.led_guides_1.setGeometry(QtCore.QRect(20, 20, 16, 20))
        self.led_guides_1.setMinimumSize(QtCore.QSize(0, 14))
        self.led_guides_1.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_guides_1.setFont(font)
        self.led_guides_1.setToolTip("")
        self.led_guides_1.setToolTipDuration(-1)
        self.led_guides_1.setObjectName("led_guides_1")
        self.led_guides_2 = QtWidgets.QToolButton(self.group_robot_3)
        self.led_guides_2.setGeometry(QtCore.QRect(40, 20, 16, 20))
        self.led_guides_2.setMinimumSize(QtCore.QSize(0, 14))
        self.led_guides_2.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_guides_2.setFont(font)
        self.led_guides_2.setToolTip("")
        self.led_guides_2.setToolTipDuration(-1)
        self.led_guides_2.setObjectName("led_guides_2")
        self.led_tcp_guides = QtWidgets.QToolButton(self.group_robot_3)
        self.led_tcp_guides.setGeometry(QtCore.QRect(60, 20, 16, 20))
        self.led_tcp_guides.setMinimumSize(QtCore.QSize(0, 14))
        self.led_tcp_guides.setMaximumSize(QtCore.QSize(1000, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_tcp_guides.setFont(font)
        self.led_tcp_guides.setToolTip("")
        self.led_tcp_guides.setToolTipDuration(-1)
        self.led_tcp_guides.setText("")
        self.led_tcp_guides.setObjectName("led_tcp_guides")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBC"))
        self.group_robot.setTitle(_translate("MainWindow", "BOT2"))
        self.btn_stop_all.setText(_translate("MainWindow", "STOP\n"
"ALL"))
        self.led_ch_a.setText(_translate("MainWindow", "C1"))
        self.led_water_high.setText(_translate("MainWindow", "WAT"))
        self.led_ch_b.setText(_translate("MainWindow", "C2"))
        self.led_ch_whl.setText(_translate("MainWindow", "WHL"))
        self.led_ch_wax.setText(_translate("MainWindow", "WAX"))
        self.btn_water.setText(_translate("MainWindow", "0-WAT"))
        self.btn_ch_a.setText(_translate("MainWindow", "1-CH_A"))
        self.btn_ch_b.setText(_translate("MainWindow", "2-CH_B"))
        self.btn_ch_whl.setText(_translate("MainWindow", "3-WHL"))
        self.btn_ch_wax.setText(_translate("MainWindow", "4-WAX"))
        self.group_robot_3.setTitle(_translate("MainWindow", "GUIDES"))
        self.guides_show.setText(_translate("MainWindow", "CURRENT_STAGE"))
        self.led_guides_1.setText(_translate("MainWindow", "G1"))
        self.led_guides_2.setText(_translate("MainWindow", "G2"))