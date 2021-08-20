# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hello(object):
    def setupUi(self, hello):
        hello.setObjectName("hello")
        hello.resize(394, 487)
        self.widget = QtWidgets.QWidget(hello)
        self.widget.setGeometry(QtCore.QRect(30, 40, 330, 390))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.area_rec = QtWidgets.QTabWidget(self.widget)
        self.area_rec.setGeometry(QtCore.QRect(0, 0, 330, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.area_rec.setFont(font)
        self.area_rec.setTabPosition(QtWidgets.QTabWidget.West)
        self.area_rec.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.area_rec.setObjectName("area_rec")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_reset_record = QtWidgets.QToolButton(self.tab)
        self.btn_reset_record.setGeometry(QtCore.QRect(270, 10, 20, 30))
        self.btn_reset_record.setMinimumSize(QtCore.QSize(15, 16))
        self.btn_reset_record.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_reset_record.setFont(font)
        self.btn_reset_record.setObjectName("btn_reset_record")
        self.btn_open_record = QtWidgets.QToolButton(self.tab)
        self.btn_open_record.setGeometry(QtCore.QRect(10, 10, 250, 30))
        self.btn_open_record.setMinimumSize(QtCore.QSize(50, 16))
        self.btn_open_record.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_open_record.setFont(font)
        self.btn_open_record.setObjectName("btn_open_record")
        self.label_record = QtWidgets.QLabel(self.tab)
        self.label_record.setGeometry(QtCore.QRect(10, 50, 290, 20))
        self.label_record.setMinimumSize(QtCore.QSize(30, 0))
        self.label_record.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_record.setFont(font)
        self.label_record.setObjectName("label_record")
        self.line_9 = QtWidgets.QFrame(self.tab)
        self.line_9.setGeometry(QtCore.QRect(0, 50, 300, 2))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_9.setFont(font)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.area_rec.addTab(self.tab, "")
        self.area_seg = QtWidgets.QTabWidget(self.widget)
        self.area_seg.setGeometry(QtCore.QRect(0, 175, 330, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.area_seg.setFont(font)
        self.area_seg.setTabPosition(QtWidgets.QTabWidget.West)
        self.area_seg.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.area_seg.setObjectName("area_seg")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_reset_segments = QtWidgets.QToolButton(self.tab_2)
        self.btn_reset_segments.setGeometry(QtCore.QRect(270, 10, 20, 30))
        self.btn_reset_segments.setMinimumSize(QtCore.QSize(15, 16))
        self.btn_reset_segments.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_reset_segments.setFont(font)
        self.btn_reset_segments.setObjectName("btn_reset_segments")
        self.auto_segments = QtWidgets.QCheckBox(self.tab_2)
        self.auto_segments.setGeometry(QtCore.QRect(10, 10, 171, 30))
        self.auto_segments.setMinimumSize(QtCore.QSize(20, 16))
        self.auto_segments.setMaximumSize(QtCore.QSize(200, 30))
        self.auto_segments.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.auto_segments.setFont(font)
        self.auto_segments.setStatusTip("")
        self.auto_segments.setWhatsThis("")
        self.auto_segments.setChecked(False)
        self.auto_segments.setObjectName("auto_segments")
        self.btn_segments = QtWidgets.QToolButton(self.tab_2)
        self.btn_segments.setGeometry(QtCore.QRect(180, 10, 80, 30))
        self.btn_segments.setMinimumSize(QtCore.QSize(50, 16))
        self.btn_segments.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_segments.setFont(font)
        self.btn_segments.setObjectName("btn_segments")
        self.area_seg.addTab(self.tab_2, "")
        self.area_car = QtWidgets.QTabWidget(self.widget)
        self.area_car.setGeometry(QtCore.QRect(0, 235, 330, 145))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.area_car.setFont(font)
        self.area_car.setTabPosition(QtWidgets.QTabWidget.West)
        self.area_car.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.area_car.setObjectName("area_car")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.car_rotate = QtWidgets.QDial(self.tab_3)
        self.car_rotate.setGeometry(QtCore.QRect(0, 17, 110, 110))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.car_rotate.setFont(font)
        self.car_rotate.setTabletTracking(False)
        self.car_rotate.setMinimum(-100)
        self.car_rotate.setMaximum(100)
        self.car_rotate.setSingleStep(5)
        self.car_rotate.setPageStep(1)
        self.car_rotate.setTracking(True)
        self.car_rotate.setOrientation(QtCore.Qt.Horizontal)
        self.car_rotate.setInvertedAppearance(False)
        self.car_rotate.setInvertedControls(False)
        self.car_rotate.setWrapping(False)
        self.car_rotate.setNotchesVisible(False)
        self.car_rotate.setObjectName("car_rotate")
        self.car_pos_x = QtWidgets.QSlider(self.tab_3)
        self.car_pos_x.setGeometry(QtCore.QRect(160, 30, 135, 51))
        self.car_pos_x.setStyleSheet("QSlider::groove:horizontal { \n"
" background-color: rgb(120, 120, 120);\n"
" border: 0px solid #424242; \n"
" height: 4px; \n"
" border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
" background-color: rgb(50, 50, 50); \n"
" border: 2px solid rgb(50, 50, 50); \n"
" width: 30px; \n"
" height: 40px; \n"
" border-radius: 16px; \n"
"margin-top:-15px;\n"
"margin-bottom:-15px;\n"
"\n"
"}")
        self.car_pos_x.setMinimum(-200)
        self.car_pos_x.setMaximum(200)
        self.car_pos_x.setSingleStep(5)
        self.car_pos_x.setPageStep(1)
        self.car_pos_x.setOrientation(QtCore.Qt.Horizontal)
        self.car_pos_x.setObjectName("car_pos_x")
        self.car_pos_z = QtWidgets.QSlider(self.tab_3)
        self.car_pos_z.setGeometry(QtCore.QRect(100, 30, 61, 85))
        self.car_pos_z.setStyleSheet("QSlider::groove:vertical\n"
"{\n"
"background: rgb(120, 120, 120);\n"
"border-color: rgb(120, 120, 120);\n"
"border-width:1 px;\n"
"width: 4px;\n"
"}\n"
" \n"
"QSlider::handle:vertical \n"
"{width: 30px;\n"
"height:33px;\n"
"background-color: rgb(50, 50, 50);\n"
"border-color: rgb(50, 50, 50);\n"
"border-width: 1px;\n"
"margin-left:-15px;\n"
"margin-right:-15px;\n"
"border-radius:16px;\n"
"}")
        self.car_pos_z.setMinimum(-100)
        self.car_pos_z.setMaximum(100)
        self.car_pos_z.setSingleStep(5)
        self.car_pos_z.setPageStep(1)
        self.car_pos_z.setOrientation(QtCore.Qt.Vertical)
        self.car_pos_z.setObjectName("car_pos_z")
        self.label_car_pos_x = QtWidgets.QLabel(self.tab_3)
        self.label_car_pos_x.setGeometry(QtCore.QRect(200, 5, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_car_pos_x.setFont(font)
        self.label_car_pos_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_car_pos_x.setObjectName("label_car_pos_x")
        self.label_car_rot = QtWidgets.QLabel(self.tab_3)
        self.label_car_rot.setGeometry(QtCore.QRect(20, 5, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_car_rot.setFont(font)
        self.label_car_rot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_car_rot.setObjectName("label_car_rot")
        self.label_car_pos_z = QtWidgets.QLabel(self.tab_3)
        self.label_car_pos_z.setGeometry(QtCore.QRect(100, 5, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_car_pos_z.setFont(font)
        self.label_car_pos_z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_car_pos_z.setObjectName("label_car_pos_z")
        self.btn_reset_car_pose = QtWidgets.QToolButton(self.tab_3)
        self.btn_reset_car_pose.setGeometry(QtCore.QRect(270, 0, 20, 30))
        self.btn_reset_car_pose.setMinimumSize(QtCore.QSize(15, 16))
        self.btn_reset_car_pose.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_reset_car_pose.setFont(font)
        self.btn_reset_car_pose.setObjectName("btn_reset_car_pose")
        self.line_8 = QtWidgets.QFrame(self.tab_3)
        self.line_8.setGeometry(QtCore.QRect(0, 120, 300, 2))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_car = QtWidgets.QLabel(self.tab_3)
        self.label_car.setGeometry(QtCore.QRect(10, 120, 280, 20))
        self.label_car.setMinimumSize(QtCore.QSize(30, 0))
        self.label_car.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_car.setFont(font)
        self.label_car.setObjectName("label_car")
        self.btn_save_car_to_npy_file = QtWidgets.QToolButton(self.tab_3)
        self.btn_save_car_to_npy_file.setGeometry(QtCore.QRect(160, 85, 135, 30))
        self.btn_save_car_to_npy_file.setMinimumSize(QtCore.QSize(60, 16))
        self.btn_save_car_to_npy_file.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_save_car_to_npy_file.setFont(font)
        self.btn_save_car_to_npy_file.setObjectName("btn_save_car_to_npy_file")
        self.area_car.addTab(self.tab_3, "")
        self.area_scan = QtWidgets.QTabWidget(self.widget)
        self.area_scan.setGeometry(QtCore.QRect(0, 75, 330, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.area_scan.setFont(font)
        self.area_scan.setTabPosition(QtWidgets.QTabWidget.West)
        self.area_scan.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.area_scan.setObjectName("area_scan")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scan_p1 = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.scan_p1.setGeometry(QtCore.QRect(10, 10, 60, 30))
        self.scan_p1.setMinimumSize(QtCore.QSize(50, 16))
        self.scan_p1.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.scan_p1.setFont(font)
        self.scan_p1.setDecimals(1)
        self.scan_p1.setMaximum(10.0)
        self.scan_p1.setSingleStep(0.5)
        self.scan_p1.setObjectName("scan_p1")
        self.scan_p2 = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.scan_p2.setGeometry(QtCore.QRect(80, 10, 70, 30))
        self.scan_p2.setMinimumSize(QtCore.QSize(50, 16))
        self.scan_p2.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.scan_p2.setFont(font)
        self.scan_p2.setDecimals(1)
        self.scan_p2.setMaximum(10.0)
        self.scan_p2.setSingleStep(0.5)
        self.scan_p2.setProperty("value", 6.0)
        self.scan_p2.setObjectName("scan_p2")
        self.btn_scan_start = QtWidgets.QToolButton(self.tab_4)
        self.btn_scan_start.setGeometry(QtCore.QRect(10, 50, 140, 30))
        self.btn_scan_start.setMinimumSize(QtCore.QSize(60, 16))
        self.btn_scan_start.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_scan_start.setFont(font)
        self.btn_scan_start.setObjectName("btn_scan_start")
        self.auto_save_rec_file = QtWidgets.QCheckBox(self.tab_4)
        self.auto_save_rec_file.setGeometry(QtCore.QRect(170, 10, 120, 30))
        self.auto_save_rec_file.setMinimumSize(QtCore.QSize(20, 16))
        self.auto_save_rec_file.setMaximumSize(QtCore.QSize(200, 30))
        self.auto_save_rec_file.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.auto_save_rec_file.setFont(font)
        self.auto_save_rec_file.setStatusTip("")
        self.auto_save_rec_file.setWhatsThis("")
        self.auto_save_rec_file.setChecked(False)
        self.auto_save_rec_file.setObjectName("auto_save_rec_file")
        self.btn_save_as_rec_file = QtWidgets.QToolButton(self.tab_4)
        self.btn_save_as_rec_file.setGeometry(QtCore.QRect(160, 50, 130, 30))
        self.btn_save_as_rec_file.setMinimumSize(QtCore.QSize(60, 16))
        self.btn_save_as_rec_file.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_save_as_rec_file.setFont(font)
        self.btn_save_as_rec_file.setObjectName("btn_save_as_rec_file")
        self.area_scan.addTab(self.tab_4, "")

        self.retranslateUi(hello)
        self.area_rec.setCurrentIndex(0)
        self.area_seg.setCurrentIndex(0)
        self.area_car.setCurrentIndex(0)
        self.area_scan.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(hello)

    def retranslateUi(self, hello):
        _translate = QtCore.QCoreApplication.translate
        hello.setWindowTitle(_translate("hello", "sss"))
        self.btn_reset_record.setText(_translate("hello", "R"))
        self.btn_open_record.setText(_translate("hello", "OPEN_FILE (.rec .npy)"))
        self.label_record.setText(_translate("hello", "REC:"))
        self.area_rec.setTabText(self.area_rec.indexOf(self.tab), _translate("hello", "REC"))
        self.btn_reset_segments.setText(_translate("hello", "R"))
        self.auto_segments.setToolTip(_translate("hello", "Automatic segmentation"))
        self.auto_segments.setText(_translate("hello", "AUTO_SEGMENTS"))
        self.btn_segments.setText(_translate("hello", "SEGM"))
        self.area_seg.setTabText(self.area_seg.indexOf(self.tab_2), _translate("hello", "SEG"))
        self.label_car_pos_x.setText(_translate("hello", "0.00"))
        self.label_car_rot.setText(_translate("hello", "0"))
        self.label_car_pos_z.setText(_translate("hello", "0.00"))
        self.btn_reset_car_pose.setText(_translate("hello", "R"))
        self.label_car.setText(_translate("hello", "CAR:"))
        self.btn_save_car_to_npy_file.setText(_translate("hello", "SAVE_TO_NPY_FILE"))
        self.area_car.setTabText(self.area_car.indexOf(self.tab_3), _translate("hello", "CAR"))
        self.btn_scan_start.setText(_translate("hello", "SCAN_START"))
        self.auto_save_rec_file.setToolTip(_translate("hello", "Automatic segmentation"))
        self.auto_save_rec_file.setText(_translate("hello", "AUTO_SAVE"))
        self.btn_save_as_rec_file.setText(_translate("hello", "SAVE_TO_REC"))
        self.area_scan.setTabText(self.area_scan.indexOf(self.tab_4), _translate("hello", "SCAN"))
