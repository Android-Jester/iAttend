# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exit_cameraFMxOxx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1098, 900)
        Dialog.setMinimumSize(QSize(1098, 900))
        Dialog.setMaximumSize(QSize(1098, 900))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/video.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.frame_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_3)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 600))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.camera_view = QFrame(self.frame_4)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 600))
        self.camera_view.setMaximumSize(QSize(16777215, 600))
        self.camera_view.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.camera_view.setFrameShape(QFrame.StyledPanel)
        self.camera_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.camera_view)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.camera_feeds = QLabel(self.camera_view)
        self.camera_feeds.setObjectName(u"camera_feeds")
        self.camera_feeds.setMinimumSize(QSize(0, 600))
        self.camera_feeds.setMaximumSize(QSize(16777215, 600))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.camera_feeds.setFont(font1)
        self.camera_feeds.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.camera_feeds.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_feeds.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.camera_feeds)


        self.verticalLayout_3.addWidget(self.camera_view)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(535, 16777215))
        self.frame_6.setStyleSheet(u"\n"
"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:5px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.btn_exit_cam_connect = QPushButton(self.frame_6)
        self.btn_exit_cam_connect.setObjectName(u"btn_exit_cam_connect")
        self.btn_exit_cam_connect.setGeometry(QRect(10, 70, 141, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_exit_cam_connect.setFont(font2)
        self.btn_exit_cam_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_cam_connect.setIcon(icon)
        self.btn_exit_cam_connect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_connect.setFlat(True)
        self.btn_exit_cam_disconect = QPushButton(self.frame_6)
        self.btn_exit_cam_disconect.setObjectName(u"btn_exit_cam_disconect")
        self.btn_exit_cam_disconect.setGeometry(QRect(170, 70, 151, 41))
        self.btn_exit_cam_disconect.setFont(font2)
        self.btn_exit_cam_disconect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_cam_disconect.setIcon(icon1)
        self.btn_exit_cam_disconect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_disconect.setFlat(True)
        self.exit_comboBox = QComboBox(self.frame_6)
        self.exit_comboBox.addItem("")
        self.exit_comboBox.addItem("")
        self.exit_comboBox.addItem("")
        self.exit_comboBox.addItem("")
        self.exit_comboBox.addItem("")
        self.exit_comboBox.addItem("")
        self.exit_comboBox.setObjectName(u"exit_comboBox")
        self.exit_comboBox.setGeometry(QRect(340, 70, 181, 41))
        self.exit_comboBox.setMinimumSize(QSize(0, 41))
        self.exit_comboBox.setMaximumSize(QSize(16777215, 41))
        self.exit_comboBox.setFont(font2)
        self.exit_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(35,35,35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.exit_comboBox.setFrame(False)
        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 20, 41, 31))
        self.label_28.setStyleSheet(u"background-color: rgb(35,35,35);")
        self.label_28.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.exit_cam_ip = QLineEdit(self.frame_6)
        self.exit_cam_ip.setObjectName(u"exit_cam_ip")
        self.exit_cam_ip.setGeometry(QRect(10, 10, 511, 51))
        self.exit_cam_ip.setFont(font2)
        self.exit_cam_ip.setStyleSheet(u"QLineEdit{\n"
"    background-color: rgb(35,35,35);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.exit_cam_ip.setClearButtonEnabled(True)
        self.label_notification = QLabel(self.frame_6)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 120, 511, 71))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.btn_exit_cam_connect.raise_()
        self.btn_exit_cam_disconect.raise_()
        self.exit_comboBox.raise_()
        self.exit_cam_ip.raise_()
        self.label_28.raise_()
        self.label_notification.raise_()

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(520, 16777215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:5px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(9)
        self.entry_blur_label = QLabel(self.frame_7)
        self.entry_blur_label.setObjectName(u"entry_blur_label")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.entry_blur_label.setFont(font4)
        self.entry_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_blur_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.entry_blur_label, 3, 0, 1, 1)

        self.contrast = QSlider(self.frame_7)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setMaximum(100)
        self.contrast.setValue(60)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.contrast, 3, 1, 1, 1)

        self.sharpness_value = QLabel(self.frame_7)
        self.sharpness_value.setObjectName(u"sharpness_value")
        self.sharpness_value.setMinimumSize(QSize(50, 0))
        self.sharpness_value.setFont(font4)
        self.sharpness_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.sharpness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sharpness_value, 2, 2, 1, 1)

        self.entry_dilation_label = QLabel(self.frame_7)
        self.entry_dilation_label.setObjectName(u"entry_dilation_label")
        self.entry_dilation_label.setFont(font4)
        self.entry_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_dilation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.entry_dilation_label, 1, 0, 1, 1)

        self.sharpness = QSlider(self.frame_7)
        self.sharpness.setObjectName(u"sharpness")
        self.sharpness.setMaximum(100)
        self.sharpness.setValue(50)
        self.sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.sharpness, 2, 1, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 2)

        self.brigthness = QSlider(self.frame_7)
        self.brigthness.setObjectName(u"brigthness")
        self.brigthness.setMaximum(100)
        self.brigthness.setValue(30)
        self.brigthness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.brigthness, 1, 1, 1, 1)

        self.brigthness_value = QLabel(self.frame_7)
        self.brigthness_value.setObjectName(u"brigthness_value")
        self.brigthness_value.setMinimumSize(QSize(50, 0))
        self.brigthness_value.setFont(font4)
        self.brigthness_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.brigthness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.brigthness_value, 1, 2, 1, 1)

        self.contrast_value = QLabel(self.frame_7)
        self.contrast_value.setObjectName(u"contrast_value")
        self.contrast_value.setMinimumSize(QSize(50, 0))
        self.contrast_value.setFont(font4)
        self.contrast_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.contrast_value, 3, 2, 1, 1)

        self.entry_erosion_label = QLabel(self.frame_7)
        self.entry_erosion_label.setObjectName(u"entry_erosion_label")
        self.entry_erosion_label.setFont(font4)
        self.entry_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_erosion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.entry_erosion_label, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.camera_feeds.setText("")
        self.btn_exit_cam_connect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.btn_exit_cam_disconect.setText(QCoreApplication.translate("Dialog", u"Disconnect", None))
        self.exit_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))
        self.exit_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))
        self.exit_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))
        self.exit_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"3", None))
        self.exit_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"4", None))
        self.exit_comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"5", None))

        self.label_28.setText("")
        self.exit_cam_ip.setPlaceholderText(QCoreApplication.translate("Dialog", u"Camera Id/IP ?", None))
        self.label_notification.setText(QCoreApplication.translate("Dialog", u"Notification", None))
        self.entry_blur_label.setText(QCoreApplication.translate("Dialog", u"Contrast", None))
        self.sharpness_value.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.entry_dilation_label.setText(QCoreApplication.translate("Dialog", u"Brigthness", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Image enhancement", None))
#if QT_CONFIG(tooltip)
        self.brigthness.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.brigthness_value.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.contrast_value.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.entry_erosion_label.setText(QCoreApplication.translate("Dialog", u"Sharpness", None))
    # retranslateUi

