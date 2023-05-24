# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restapi_endpointscQCTNm.ui'
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

class Ui_RESTAPI(object):
    def setupUi(self, RESTAPI):
        if RESTAPI.objectName():
            RESTAPI.setObjectName(u"RESTAPI")
        RESTAPI.resize(530, 510)
        RESTAPI.setMinimumSize(QSize(530, 510))
        RESTAPI.setMaximumSize(QSize(530, 520))
        self.verticalLayout = QVBoxLayout(RESTAPI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(RESTAPI)
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
        self.label.setPixmap(QPixmap(u":/icons/asset/database.svg"))

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
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.details_url = QLineEdit(self.frame_4)
        self.details_url.setObjectName(u"details_url")
        self.details_url.setGeometry(QRect(20, 100, 470, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_url.sizePolicy().hasHeightForWidth())
        self.details_url.setSizePolicy(sizePolicy)
        self.details_url.setMinimumSize(QSize(470, 0))
        self.details_url.setMaximumSize(QSize(400, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.details_url.setFont(font1)
        self.details_url.setTabletTracking(True)
        self.details_url.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.details_url.setClearButtonEnabled(True)
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 110, 31, 31))
        self.label_36.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_36.setPixmap(QPixmap(u":/icons/asset/user.svg"))
        self.image_url = QLineEdit(self.frame_4)
        self.image_url.setObjectName(u"image_url")
        self.image_url.setGeometry(QRect(20, 180, 470, 51))
        sizePolicy.setHeightForWidth(self.image_url.sizePolicy().hasHeightForWidth())
        self.image_url.setSizePolicy(sizePolicy)
        self.image_url.setMinimumSize(QSize(470, 0))
        self.image_url.setMaximumSize(QSize(470, 51))
        self.image_url.setFont(font1)
        self.image_url.setTabletTracking(True)
        self.image_url.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_url.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 190, 31, 31))
        self.label_38.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_38.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 320, 470, 101))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_notification.sizePolicy().hasHeightForWidth())
        self.label_notification.setSizePolicy(sizePolicy1)
        self.label_notification.setMinimumSize(QSize(470, 0))
        self.label_notification.setMaximumSize(QSize(470, 101))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_notification.setFont(font2)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.sqlite = QRadioButton(self.frame_4)
        self.sqlite.setObjectName(u"sqlite")
        self.sqlite.setGeometry(QRect(20, 40, 91, 20))
        sizePolicy.setHeightForWidth(self.sqlite.sizePolicy().hasHeightForWidth())
        self.sqlite.setSizePolicy(sizePolicy)
        self.sqlite.setMaximumSize(QSize(100, 20))
        self.sqlite.setFont(font1)
        self.sqlite.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(35,35,35)\n"
"}")
        self.sqlite.setChecked(True)
        self.API = QRadioButton(self.frame_4)
        self.API.setObjectName(u"API")
        self.API.setGeometry(QRect(150, 40, 100, 20))
        sizePolicy.setHeightForWidth(self.API.sizePolicy().hasHeightForWidth())
        self.API.setSizePolicy(sizePolicy)
        self.API.setMaximumSize(QSize(100, 20))
        self.API.setFont(font1)
        self.API.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(35,35,35)\n"
"}")
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 30, 180, 41))
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(180, 41))
        self.comboBox.setMaximumSize(QSize(145, 41))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.type = QLineEdit(self.frame_4)
        self.type.setObjectName(u"type")
        self.type.setGeometry(QRect(20, 250, 470, 51))
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        self.type.setMinimumSize(QSize(0, 51))
        self.type.setMaximumSize(QSize(470, 51))
        self.type.setFont(font1)
        self.type.setTabletTracking(True)
        self.type.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.type.setClearButtonEnabled(True)
        self.label_39 = QLabel(self.frame_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 260, 31, 31))
        self.label_39.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_39.setPixmap(QPixmap(u":/icons/asset/external-link.svg"))

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(RESTAPI)

        QMetaObject.connectSlotsByName(RESTAPI)
    # setupUi

    def retranslateUi(self, RESTAPI):
        RESTAPI.setWindowTitle(QCoreApplication.translate("RESTAPI", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("RESTAPI", u"REST API", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.details_url.setPlaceholderText(QCoreApplication.translate("RESTAPI", u"Details url", None))
        self.label_36.setText("")
        self.image_url.setPlaceholderText(QCoreApplication.translate("RESTAPI", u"Images url", None))
        self.label_38.setText("")
        self.label_notification.setText(QCoreApplication.translate("RESTAPI", u"Notification", None))
        self.sqlite.setText(QCoreApplication.translate("RESTAPI", u"SQLite", None))
        self.API.setText(QCoreApplication.translate("RESTAPI", u"Rest API", None))
        self.type.setPlaceholderText(QCoreApplication.translate("RESTAPI", u"Type", None))
        self.label_39.setText("")
    # retranslateUi

