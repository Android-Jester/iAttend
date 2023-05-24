# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordJINdKg.ui'
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

class Ui_Forgot(object):
    def setupUi(self, Forgot):
        if Forgot.objectName():
            Forgot.setObjectName(u"Forgot")
        Forgot.resize(513, 413)
        self.horizontalLayout_2 = QHBoxLayout(Forgot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Forgot)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"    background-color: rgb(35, 35, 35);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 15, 20, 0)
        self.title_frame = QFrame(self.frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 40))
        self.title_frame.setMaximumSize(QSize(16777215, 40))
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/key.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.title_frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_minimize = QPushButton(self.title_frame)
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

        self.btn_maximize = QPushButton(self.title_frame)
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

        self.btn_close = QPushButton(self.title_frame)
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


        self.verticalLayout_2.addWidget(self.title_frame)

        self.info_label = QLabel(self.frame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMinimumSize(QSize(0, 31))
        self.info_label.setMaximumSize(QSize(16777215, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.info_label.setFont(font1)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.info_label)

        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 50))
        self.username.setMaximumSize(QSize(16777215, 45))
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:7px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.username.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.username)

        self.reference = QLineEdit(self.frame)
        self.reference.setObjectName(u"reference")
        self.reference.setMinimumSize(QSize(0, 50))
        self.reference.setMaximumSize(QSize(16777215, 45))
        self.reference.setFont(font)
        self.reference.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:7px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reference.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.reference)

        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 50))
        self.password.setMaximumSize(QSize(16777215, 45))
        self.password.setFont(font)
        self.password.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:7px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.password)

        self.btn_frame = QFrame(self.frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setMinimumSize(QSize(200, 55))
        self.btn_frame.setMaximumSize(QSize(510, 55))
        self.btn_frame.setFrameShape(QFrame.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Plain)
        self.btn_send = QPushButton(self.btn_frame)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(270, 10, 171, 41))
        self.btn_send.setFont(font)
        self.btn_send.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_send.setIconSize(QSize(30, 30))
        self.btn_send.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_frame)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Forgot)

        QMetaObject.connectSlotsByName(Forgot)
    # setupUi

    def retranslateUi(self, Forgot):
        Forgot.setWindowTitle(QCoreApplication.translate("Forgot", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Forgot", u"Reset Password", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.info_label.setText(QCoreApplication.translate("Forgot", u"Provide details to reset password", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Forgot", u"Username", None))
        self.reference.setPlaceholderText(QCoreApplication.translate("Forgot", u"Reference", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Forgot", u"Password", None))
        self.btn_send.setText(QCoreApplication.translate("Forgot", u"Reset", None))
    # retranslateUi

