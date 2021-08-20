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
        MainWindow.resize(280, 750)
        MainWindow.setMinimumSize(QtCore.QSize(0, 750))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 760))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ui_tcp_connected = QtWidgets.QRadioButton(self.centralwidget)
        self.ui_tcp_connected.setGeometry(QtCore.QRect(170, 0, 120, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_tcp_connected.setFont(font)
        self.ui_tcp_connected.setObjectName("ui_tcp_connected")
        self.ui_tcp_ena = QtWidgets.QCheckBox(self.centralwidget)
        self.ui_tcp_ena.setGeometry(QtCore.QRect(10, 0, 120, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_tcp_ena.setFont(font)
        self.ui_tcp_ena.setChecked(True)
        self.ui_tcp_ena.setObjectName("ui_tcp_ena")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 210, 280, 110))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.ui_log_event = QtWidgets.QTextBrowser(self.groupBox)
        self.ui_log_event.setGeometry(QtCore.QRect(0, 20, 280, 90))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_log_event.setFont(font)
        self.ui_log_event.setObjectName("ui_log_event")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 330, 280, 110))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ui_log_inviter = QtWidgets.QTextBrowser(self.groupBox_2)
        self.ui_log_inviter.setGeometry(QtCore.QRect(0, 20, 280, 90))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_log_inviter.setFont(font)
        self.ui_log_inviter.setObjectName("ui_log_inviter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 450, 280, 140))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.ui_log_recv = QtWidgets.QTextBrowser(self.groupBox_3)
        self.ui_log_recv.setGeometry(QtCore.QRect(0, 20, 280, 120))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_log_recv.setFont(font)
        self.ui_log_recv.setObjectName("ui_log_recv")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 20, 280, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ui_my_ip = QtWidgets.QLineEdit(self.groupBox_4)
        self.ui_my_ip.setGeometry(QtCore.QRect(70, 40, 140, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ui_my_ip.setFont(font)
        self.ui_my_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_my_ip.setObjectName("ui_my_ip")
        self.ui_server_port = QtWidgets.QLineEdit(self.groupBox_4)
        self.ui_server_port.setGeometry(QtCore.QRect(210, 40, 60, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ui_server_port.setFont(font)
        self.ui_server_port.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_server_port.setObjectName("ui_server_port")
        self.ui_server = QtWidgets.QTableWidget(self.groupBox_4)
        self.ui_server.setGeometry(QtCore.QRect(10, 60, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ui_server.setFont(font)
        self.ui_server.setObjectName("ui_server")
        self.ui_server.setColumnCount(2)
        self.ui_server.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.ui_server.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ui_server.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.ui_server.setHorizontalHeaderItem(1, item)
        self.ui_server.verticalHeader().setDefaultSectionSize(20)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ui_device_token = QtWidgets.QLineEdit(self.groupBox_4)
        self.ui_device_token.setGeometry(QtCore.QRect(70, 20, 81, 21))
        self.ui_device_token.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_device_token.setObjectName("ui_device_token")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ui_device_type = QtWidgets.QLineEdit(self.groupBox_4)
        self.ui_device_type.setGeometry(QtCore.QRect(210, 20, 61, 21))
        self.ui_device_type.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_device_type.setObjectName("ui_device_type")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 130, 280, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.ui_tx_msg = QtWidgets.QLineEdit(self.groupBox_5)
        self.ui_tx_msg.setGeometry(QtCore.QRect(10, 20, 179, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ui_tx_msg.setFont(font)
        self.ui_tx_msg.setObjectName("ui_tx_msg")
        self.btn_tcp_send = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_tcp_send.setGeometry(QtCore.QRect(200, 20, 69, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_tcp_send.setFont(font)
        self.btn_tcp_send.setObjectName("btn_tcp_send")
        self.btn_bad_1_before = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_bad_1_before.setGeometry(QtCore.QRect(10, 50, 35, 22))
        self.btn_bad_1_before.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bad_1_before.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bad_1_before.setFont(font)
        self.btn_bad_1_before.setObjectName("btn_bad_1_before")
        self.btn_bad_2_more = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_bad_2_more.setGeometry(QtCore.QRect(45, 50, 35, 22))
        self.btn_bad_2_more.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bad_2_more.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bad_2_more.setFont(font)
        self.btn_bad_2_more.setObjectName("btn_bad_2_more")
        self.btn_bad_3_less = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_bad_3_less.setGeometry(QtCore.QRect(80, 50, 35, 22))
        self.btn_bad_3_less.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bad_3_less.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bad_3_less.setFont(font)
        self.btn_bad_3_less.setObjectName("btn_bad_3_less")
        self.btn_bad_4_empty = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_bad_4_empty.setGeometry(QtCore.QRect(115, 50, 35, 22))
        self.btn_bad_4_empty.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bad_4_empty.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bad_4_empty.setFont(font)
        self.btn_bad_4_empty.setObjectName("btn_bad_4_empty")
        self.btn_bad_5_x2 = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_bad_5_x2.setGeometry(QtCore.QRect(150, 50, 35, 22))
        self.btn_bad_5_x2.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bad_5_x2.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bad_5_x2.setFont(font)
        self.btn_bad_5_x2.setObjectName("btn_bad_5_x2")
        self.btn_send_loop = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_send_loop.setGeometry(QtCore.QRect(230, 50, 40, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_send_loop.setFont(font)
        self.btn_send_loop.setObjectName("btn_send_loop")
        self.btn_send_large = QtWidgets.QToolButton(self.groupBox_5)
        self.btn_send_large.setGeometry(QtCore.QRect(190, 50, 40, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.btn_send_large.setFont(font)
        self.btn_send_large.setObjectName("btn_send_large")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 600, 280, 140))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.ui_log_error = QtWidgets.QTextBrowser(self.groupBox_6)
        self.ui_log_error.setGeometry(QtCore.QRect(0, 20, 280, 120))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ui_log_error.setFont(font)
        self.ui_log_error.setObjectName("ui_log_error")
        self.ui_inviter_ena = QtWidgets.QCheckBox(self.centralwidget)
        self.ui_inviter_ena.setGeometry(QtCore.QRect(80, 0, 120, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_inviter_ena.setFont(font)
        self.ui_inviter_ena.setChecked(True)
        self.ui_inviter_ena.setObjectName("ui_inviter_ena")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ANET_CLIENT"))
        self.ui_tcp_connected.setText(_translate("MainWindow", "TCP_CONNECTED"))
        self.ui_tcp_ena.setText(_translate("MainWindow", "TCP_ENA"))
        self.groupBox.setTitle(_translate("MainWindow", "ANET_EVENT"))
        self.groupBox_2.setTitle(_translate("MainWindow", "INVITER"))
        self.groupBox_3.setTitle(_translate("MainWindow", "RX"))
        self.groupBox_4.setTitle(_translate("MainWindow", "DEVICE"))
        self.label_3.setText(_translate("MainWindow", "MY_IP"))
        item = self.ui_server.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Server"))
        item = self.ui_server.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP"))
        item = self.ui_server.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.label_4.setText(_translate("MainWindow", "TOKEN"))
        self.label_6.setText(_translate("MainWindow", "TYPE"))
        self.groupBox_5.setTitle(_translate("MainWindow", "TX"))
        self.ui_tx_msg.setText(_translate("MainWindow", "Hello"))
        self.btn_tcp_send.setText(_translate("MainWindow", "TCP_SEND"))
        self.btn_bad_1_before.setText(_translate("MainWindow", "BEFORE"))
        self.btn_bad_2_more.setText(_translate("MainWindow", "MORE"))
        self.btn_bad_3_less.setText(_translate("MainWindow", "LESS"))
        self.btn_bad_4_empty.setText(_translate("MainWindow", "EMPTY"))
        self.btn_bad_5_x2.setText(_translate("MainWindow", "x2"))
        self.btn_send_loop.setText(_translate("MainWindow", "LOOP"))
        self.btn_send_large.setText(_translate("MainWindow", "LARGE"))
        self.groupBox_6.setTitle(_translate("MainWindow", "ERROR"))
        self.ui_inviter_ena.setText(_translate("MainWindow", "INVITER_ENA"))
