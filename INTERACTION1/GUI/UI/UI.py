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
        MainWindow.resize(695, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_device = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_device.setGeometry(QtCore.QRect(10, 20, 371, 91))
        self.tab_device.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_device.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab_device.setElideMode(QtCore.Qt.ElideLeft)
        self.tab_device.setObjectName("tab_device")
        self.device = QtWidgets.QWidget()
        self.device.setObjectName("device")
        self.label_pumps_station = QtWidgets.QLabel(self.device)
        self.label_pumps_station.setGeometry(QtCore.QRect(0, 10, 91, 14))
        self.label_pumps_station.setMinimumSize(QtCore.QSize(0, 14))
        self.label_pumps_station.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_pumps_station.setFont(font)
        self.label_pumps_station.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_pumps_station.setObjectName("label_pumps_station")
        self.ip_local = QtWidgets.QLabel(self.device)
        self.ip_local.setGeometry(QtCore.QRect(170, 10, 150, 14))
        self.ip_local.setMinimumSize(QtCore.QSize(75, 14))
        self.ip_local.setMaximumSize(QtCore.QSize(150, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ip_local.setFont(font)
        self.ip_local.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ip_local.setObjectName("ip_local")
        self.ip_nuc = QtWidgets.QLabel(self.device)
        self.ip_nuc.setGeometry(QtCore.QRect(170, 70, 160, 14))
        self.ip_nuc.setMinimumSize(QtCore.QSize(160, 14))
        self.ip_nuc.setMaximumSize(QtCore.QSize(170, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ip_nuc.setFont(font)
        self.ip_nuc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ip_nuc.setObjectName("ip_nuc")
        self.btn_power_off = QtWidgets.QToolButton(self.device)
        self.btn_power_off.setGeometry(QtCore.QRect(280, 10, 50, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_power_off.setFont(font)
        self.btn_power_off.setObjectName("btn_power_off")
        self.led_pumps_station = QtWidgets.QToolButton(self.device)
        self.led_pumps_station.setGeometry(QtCore.QRect(90, 10, 50, 14))
        self.led_pumps_station.setMinimumSize(QtCore.QSize(50, 0))
        self.led_pumps_station.setMaximumSize(QtCore.QSize(50, 14))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.led_pumps_station.setFont(font)
        self.led_pumps_station.setToolTip("")
        self.led_pumps_station.setToolTipDuration(-1)
        self.led_pumps_station.setObjectName("led_pumps_station")
        self.tab_device.addTab(self.device, "")
        self.tab_pumps_station = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_pumps_station.setGeometry(QtCore.QRect(0, 120, 371, 201))
        self.tab_pumps_station.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_pumps_station.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab_pumps_station.setElideMode(QtCore.Qt.ElideLeft)
        self.tab_pumps_station.setObjectName("tab_pumps_station")
        self.device_3 = QtWidgets.QWidget()
        self.device_3.setObjectName("device_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.device_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 221, 173))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ui_wheel_data = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ui_wheel_data.setMaximumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ui_wheel_data.setFont(font)
        self.ui_wheel_data.setObjectName("ui_wheel_data")
        self.gridLayout_3.addWidget(self.ui_wheel_data, 4, 1, 1, 1)
        self.DRAIN_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DRAIN_6.setMinimumSize(QtCore.QSize(0, 14))
        self.DRAIN_6.setMaximumSize(QtCore.QSize(25, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DRAIN_6.setFont(font)
        self.DRAIN_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DRAIN_6.setObjectName("DRAIN_6")
        self.gridLayout_3.addWidget(self.DRAIN_6, 2, 2, 1, 1)
        self.DRAIN_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DRAIN_10.setMinimumSize(QtCore.QSize(0, 14))
        self.DRAIN_10.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DRAIN_10.setFont(font)
        self.DRAIN_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DRAIN_10.setObjectName("DRAIN_10")
        self.gridLayout_3.addWidget(self.DRAIN_10, 4, 2, 1, 1)
        self.ui_acid_data = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ui_acid_data.setMaximumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ui_acid_data.setFont(font)
        self.ui_acid_data.setObjectName("ui_acid_data")
        self.gridLayout_3.addWidget(self.ui_acid_data, 3, 1, 1, 1)
        self.ui_alkali_data = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ui_alkali_data.setMaximumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ui_alkali_data.setFont(font)
        self.ui_alkali_data.setObjectName("ui_alkali_data")
        self.gridLayout_3.addWidget(self.ui_alkali_data, 2, 1, 1, 1)
        self.DRAIN_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DRAIN_4.setMinimumSize(QtCore.QSize(0, 14))
        self.DRAIN_4.setMaximumSize(QtCore.QSize(25, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DRAIN_4.setFont(font)
        self.DRAIN_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DRAIN_4.setObjectName("DRAIN_4")
        self.gridLayout_3.addWidget(self.DRAIN_4, 1, 2, 1, 1)
        self.DRAIN_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DRAIN_8.setMinimumSize(QtCore.QSize(0, 14))
        self.DRAIN_8.setMaximumSize(QtCore.QSize(20, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DRAIN_8.setFont(font)
        self.DRAIN_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DRAIN_8.setObjectName("DRAIN_8")
        self.gridLayout_3.addWidget(self.DRAIN_8, 3, 2, 1, 1)
        self.label_chem = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_chem.setMinimumSize(QtCore.QSize(0, 14))
        self.label_chem.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_chem.setFont(font)
        self.label_chem.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_chem.setObjectName("label_chem")
        self.gridLayout_3.addWidget(self.label_chem, 0, 0, 1, 1)
        self.ui_wax_data = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ui_wax_data.setMaximumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ui_wax_data.setFont(font)
        self.ui_wax_data.setObjectName("ui_wax_data")
        self.gridLayout_3.addWidget(self.ui_wax_data, 5, 1, 1, 1)
        self.label_wheel_data = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_wheel_data.setMinimumSize(QtCore.QSize(0, 14))
        self.label_wheel_data.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_wheel_data.setFont(font)
        self.label_wheel_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_wheel_data.setObjectName("label_wheel_data")
        self.gridLayout_3.addWidget(self.label_wheel_data, 4, 0, 1, 1)
        self.label_wax_data = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_wax_data.setMinimumSize(QtCore.QSize(0, 14))
        self.label_wax_data.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_wax_data.setFont(font)
        self.label_wax_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_wax_data.setObjectName("label_wax_data")
        self.gridLayout_3.addWidget(self.label_wax_data, 5, 0, 1, 1)
        self.label_acid_data = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_acid_data.setMinimumSize(QtCore.QSize(0, 14))
        self.label_acid_data.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_acid_data.setFont(font)
        self.label_acid_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_acid_data.setObjectName("label_acid_data")
        self.gridLayout_3.addWidget(self.label_acid_data, 3, 0, 1, 1)
        self.label_water_data = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_water_data.setMinimumSize(QtCore.QSize(0, 14))
        self.label_water_data.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_water_data.setFont(font)
        self.label_water_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_water_data.setObjectName("label_water_data")
        self.gridLayout_3.addWidget(self.label_water_data, 1, 0, 1, 1)
        self.label_alkali_data = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_alkali_data.setMinimumSize(QtCore.QSize(0, 14))
        self.label_alkali_data.setMaximumSize(QtCore.QSize(40, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_alkali_data.setFont(font)
        self.label_alkali_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_alkali_data.setObjectName("label_alkali_data")
        self.gridLayout_3.addWidget(self.label_alkali_data, 2, 0, 1, 1)
        self.ui_water_data = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ui_water_data.setMaximumSize(QtCore.QSize(35, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ui_water_data.setFont(font)
        self.ui_water_data.setObjectName("ui_water_data")
        self.gridLayout_3.addWidget(self.ui_water_data, 1, 1, 1, 1)
        self.DRAIN_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DRAIN_12.setMinimumSize(QtCore.QSize(0, 14))
        self.DRAIN_12.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DRAIN_12.setFont(font)
        self.DRAIN_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DRAIN_12.setObjectName("DRAIN_12")
        self.gridLayout_3.addWidget(self.DRAIN_12, 5, 2, 1, 1)
        self.led_water = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.led_water.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_water.setFont(font)
        self.led_water.setObjectName("led_water")
        self.gridLayout_3.addWidget(self.led_water, 1, 3, 1, 1)
        self.led_alkali = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.led_alkali.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_alkali.setFont(font)
        self.led_alkali.setObjectName("led_alkali")
        self.gridLayout_3.addWidget(self.led_alkali, 2, 3, 1, 1)
        self.led_acid = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.led_acid.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_acid.setFont(font)
        self.led_acid.setObjectName("led_acid")
        self.gridLayout_3.addWidget(self.led_acid, 3, 3, 1, 1)
        self.led_wheel = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.led_wheel.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_wheel.setFont(font)
        self.led_wheel.setObjectName("led_wheel")
        self.gridLayout_3.addWidget(self.led_wheel, 4, 3, 1, 1)
        self.led_wax = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        self.led_wax.setMaximumSize(QtCore.QSize(75, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.led_wax.setFont(font)
        self.led_wax.setObjectName("led_wax")
        self.gridLayout_3.addWidget(self.led_wax, 5, 3, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.device_3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(240, 10, 101, 171))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_pumps_switch = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_pumps_switch.setMinimumSize(QtCore.QSize(0, 14))
        self.label_pumps_switch.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_pumps_switch.setFont(font)
        self.label_pumps_switch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_pumps_switch.setObjectName("label_pumps_switch")
        self.gridLayout_5.addWidget(self.label_pumps_switch, 0, 0, 1, 1)
        self.btn_water_wax = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_water_wax.setFont(font)
        self.btn_water_wax.setObjectName("btn_water_wax")
        self.gridLayout_5.addWidget(self.btn_water_wax, 6, 0, 1, 1)
        self.btn_wheel = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_wheel.setFont(font)
        self.btn_wheel.setObjectName("btn_wheel")
        self.gridLayout_5.addWidget(self.btn_wheel, 3, 0, 1, 1)
        self.btn_acid = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_acid.setFont(font)
        self.btn_acid.setObjectName("btn_acid")
        self.gridLayout_5.addWidget(self.btn_acid, 5, 0, 1, 1)
        self.btn_high_water = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_high_water.setFont(font)
        self.btn_high_water.setObjectName("btn_high_water")
        self.gridLayout_5.addWidget(self.btn_high_water, 2, 0, 1, 1)
        self.btn_water_inflow = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_water_inflow.setFont(font)
        self.btn_water_inflow.setObjectName("btn_water_inflow")
        self.gridLayout_5.addWidget(self.btn_water_inflow, 7, 0, 1, 1)
        self.btn_all_stop = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_all_stop.setFont(font)
        self.btn_all_stop.setObjectName("btn_all_stop")
        self.gridLayout_5.addWidget(self.btn_all_stop, 1, 0, 1, 1)
        self.btn_alkali = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_alkali.setFont(font)
        self.btn_alkali.setObjectName("btn_alkali")
        self.gridLayout_5.addWidget(self.btn_alkali, 4, 0, 1, 1)
        self.tab_pumps_station.addTab(self.device_3, "")
        self.tab_logs = QtWidgets.QToolBox(self.centralwidget)
        self.tab_logs.setGeometry(QtCore.QRect(390, 20, 291, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_logs.setFont(font)
        self.tab_logs.setLineWidth(-3)
        self.tab_logs.setObjectName("tab_logs")
        self.page_pumps_station = QtWidgets.QWidget()
        self.page_pumps_station.setGeometry(QtCore.QRect(0, 0, 291, 211))
        self.page_pumps_station.setObjectName("page_pumps_station")
        self.log_pumps_station = QtWidgets.QTextBrowser(self.page_pumps_station)
        self.log_pumps_station.setGeometry(QtCore.QRect(0, 0, 291, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_pumps_station.setFont(font)
        self.log_pumps_station.setObjectName("log_pumps_station")
        self.tab_logs.addItem(self.page_pumps_station, "")
        self.page_network = QtWidgets.QWidget()
        self.page_network.setGeometry(QtCore.QRect(0, 0, 291, 211))
        self.page_network.setObjectName("page_network")
        self.log_network = QtWidgets.QTextBrowser(self.page_network)
        self.log_network.setGeometry(QtCore.QRect(0, 0, 291, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_network.setFont(font)
        self.log_network.setObjectName("log_network")
        self.tab_logs.addItem(self.page_network, "")
        self.page_error = QtWidgets.QWidget()
        self.page_error.setGeometry(QtCore.QRect(0, 0, 291, 211))
        self.page_error.setObjectName("page_error")
        self.log_error = QtWidgets.QTextBrowser(self.page_error)
        self.log_error.setGeometry(QtCore.QRect(0, 0, 291, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_error.setFont(font)
        self.log_error.setObjectName("log_error")
        self.tab_logs.addItem(self.page_error, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_device.setCurrentIndex(0)
        self.tab_pumps_station.setCurrentIndex(0)
        self.tab_logs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_pumps_station.setText(_translate("MainWindow", "PUMPS STATION"))
        self.ip_local.setText(_translate("MainWindow", "LocalIP : 0.0.0.0"))
        self.ip_nuc.setText(_translate("MainWindow", "NucIP : 0.0.0.0"))
        self.btn_power_off.setText(_translate("MainWindow", "POWER\n"
"OFF"))
        self.led_pumps_station.setText(_translate("MainWindow", "OFF"))
        self.tab_device.setTabText(self.tab_device.indexOf(self.device), _translate("MainWindow", "DEVICE"))
        self.DRAIN_6.setText(_translate("MainWindow", "mm"))
        self.DRAIN_10.setText(_translate("MainWindow", "mm"))
        self.DRAIN_4.setText(_translate("MainWindow", "mm"))
        self.DRAIN_8.setText(_translate("MainWindow", "mm"))
        self.label_chem.setText(_translate("MainWindow", "CHEM"))
        self.label_wheel_data.setText(_translate("MainWindow", "WHEEL"))
        self.label_wax_data.setText(_translate("MainWindow", "WAX"))
        self.label_acid_data.setText(_translate("MainWindow", "ACID"))
        self.label_water_data.setText(_translate("MainWindow", "WATER"))
        self.label_alkali_data.setText(_translate("MainWindow", "ALKALI"))
        self.ui_water_data.setText(_translate("MainWindow", "1600"))
        self.DRAIN_12.setText(_translate("MainWindow", "mm"))
        self.led_water.setText(_translate("MainWindow", "full"))
        self.led_alkali.setText(_translate("MainWindow", "full"))
        self.led_acid.setText(_translate("MainWindow", "full"))
        self.led_wheel.setText(_translate("MainWindow", "full"))
        self.led_wax.setText(_translate("MainWindow", "full"))
        self.label_pumps_switch.setText(_translate("MainWindow", "PUMPS  SWITCH"))
        self.btn_water_wax.setText(_translate("MainWindow", "WATER WAX"))
        self.btn_wheel.setText(_translate("MainWindow", "WHEEL"))
        self.btn_acid.setText(_translate("MainWindow", "ACID"))
        self.btn_high_water.setText(_translate("MainWindow", "HIGH WATER"))
        self.btn_water_inflow.setText(_translate("MainWindow", "WATER INFLOW"))
        self.btn_all_stop.setText(_translate("MainWindow", "ALL STOP"))
        self.btn_alkali.setText(_translate("MainWindow", "ALKALI"))
        self.tab_pumps_station.setTabText(self.tab_pumps_station.indexOf(self.device_3), _translate("MainWindow", "INTERACTION"))
        self.tab_logs.setItemText(self.tab_logs.indexOf(self.page_pumps_station), _translate("MainWindow", "PUMPS STATION"))
        self.tab_logs.setItemText(self.tab_logs.indexOf(self.page_network), _translate("MainWindow", "NETWORK"))
        self.tab_logs.setItemText(self.tab_logs.indexOf(self.page_error), _translate("MainWindow", "ERROR"))
