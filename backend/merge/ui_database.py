# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge_databaseHnipai.ui'
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

class Ui_Database(object):
    def setupUi(self, Database):
        if Database.objectName():
            Database.setObjectName(u"Database")
        Database.resize(435, 665)
        Database.setMinimumSize(QSize(435, 665))
        Database.setMaximumSize(QSize(435, 665))
        Database.setStyleSheet(u"border-radius:5px;")
        self.verticalLayout = QVBoxLayout(Database)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Database)
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
        self.username = QLineEdit(self.frame_4)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 150, 371, 51))
        self.username.setMaximumSize(QSize(371, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.username.setFont(font1)
        self.username.setTabletTracking(True)
        self.username.setStyleSheet(u"QLineEdit{\n"
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
        self.username.setClearButtonEnabled(True)
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 160, 31, 31))
        self.label_36.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_36.setPixmap(QPixmap(u":/icons/asset/user.svg"))
        self.password = QLineEdit(self.frame_4)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 220, 371, 51))
        self.password.setMaximumSize(QSize(371, 51))
        self.password.setFont(font1)
        self.password.setTabletTracking(True)
        self.password.setStyleSheet(u"QLineEdit{\n"
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
        self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.password.setClearButtonEnabled(True)
        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(30, 230, 31, 31))
        self.label_37.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_37.setPixmap(QPixmap(u":/icons/asset/lock.svg"))
        self.hostname = QLineEdit(self.frame_4)
        self.hostname.setObjectName(u"hostname")
        self.hostname.setGeometry(QRect(20, 290, 371, 51))
        self.hostname.setMaximumSize(QSize(371, 51))
        self.hostname.setFont(font1)
        self.hostname.setTabletTracking(True)
        self.hostname.setStyleSheet(u"QLineEdit{\n"
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
        self.hostname.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 300, 31, 31))
        self.label_38.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_38.setPixmap(QPixmap(u":/icons/asset/external-link.svg"))
        self.database_name = QLineEdit(self.frame_4)
        self.database_name.setObjectName(u"database_name")
        self.database_name.setGeometry(QRect(20, 360, 221, 51))
        self.database_name.setMaximumSize(QSize(221, 51))
        self.database_name.setFont(font1)
        self.database_name.setTabletTracking(True)
        self.database_name.setStyleSheet(u"QLineEdit{\n"
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
        self.database_name.setClearButtonEnabled(True)
        self.label_39 = QLabel(self.frame_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 370, 31, 31))
        self.label_39.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_39.setPixmap(QPixmap(u":/icons/asset/database.svg"))
        self.btn_connect_test = QPushButton(self.frame_4)
        self.btn_connect_test.setObjectName(u"btn_connect_test")
        self.btn_connect_test.setGeometry(QRect(20, 430, 181, 41))
        self.btn_connect_test.setMaximumSize(QSize(181, 41))
        self.btn_connect_test.setFont(font1)
        self.btn_connect_test.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
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
        icon.addFile(u":/icons/asset/link-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_test.setIcon(icon)
        self.btn_connect_test.setIconSize(QSize(30, 30))
        self.btn_connect_test.setFlat(True)
        self.label_notification = QLabel(self.frame_4)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 490, 371, 91))
        self.label_notification.setMaximumSize(QSize(371, 91))
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
        self.port = QLineEdit(self.frame_4)
        self.port.setObjectName(u"port")
        self.port.setGeometry(QRect(260, 360, 131, 51))
        self.port.setFont(font1)
        self.port.setTabletTracking(True)
        self.port.setStyleSheet(u"QLineEdit{\n"
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
        self.port.setClearButtonEnabled(True)
        self.label_40 = QLabel(self.frame_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(270, 370, 31, 31))
        self.label_40.setMaximumSize(QSize(31, 31))
        self.label_40.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_40.setPixmap(QPixmap(u":/icons/asset/power.svg"))
        self.btn_update_properties = QPushButton(self.frame_4)
        self.btn_update_properties.setObjectName(u"btn_update_properties")
        self.btn_update_properties.setGeometry(QRect(210, 430, 181, 41))
        self.btn_update_properties.setMaximumSize(QSize(181, 41))
        self.btn_update_properties.setFont(font1)
        self.btn_update_properties.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
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
        icon1.addFile(u":/icons/asset/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_properties.setIcon(icon1)
        self.btn_update_properties.setIconSize(QSize(30, 30))
        self.btn_update_properties.setFlat(True)
        self.database_tables = QComboBox(self.frame_4)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(20, 20, 241, 45))
        self.database_tables.setMinimumSize(QSize(0, 45))
        self.database_tables.setMaximumSize(QSize(371, 40))
        self.database_tables.setFont(font1)
        self.database_tables.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.database_tables.setEditable(False)
        self.database_tables.setFrame(False)
        self.central_tablenam = QLineEdit(self.frame_4)
        self.central_tablenam.setObjectName(u"central_tablenam")
        self.central_tablenam.setGeometry(QRect(20, 80, 231, 45))
        self.central_tablenam.setMaximumSize(QSize(231, 45))
        self.central_tablenam.setFont(font1)
        self.central_tablenam.setTabletTracking(True)
        self.central_tablenam.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.central_tablenam.setClearButtonEnabled(True)
        self.btn_create_central_table = QPushButton(self.frame_4)
        self.btn_create_central_table.setObjectName(u"btn_create_central_table")
        self.btn_create_central_table.setGeometry(QRect(270, 80, 121, 45))
        self.btn_create_central_table.setMaximumSize(QSize(121, 45))
        self.btn_create_central_table.setFont(font1)
        self.btn_create_central_table.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_central_table.setIcon(icon2)
        self.btn_create_central_table.setIconSize(QSize(30, 30))
        self.btn_create_central_table.setFlat(True)
        self.btn_load_tables = QPushButton(self.frame_4)
        self.btn_load_tables.setObjectName(u"btn_load_tables")
        self.btn_load_tables.setGeometry(QRect(270, 20, 121, 45))
        self.btn_load_tables.setMinimumSize(QSize(0, 45))
        self.btn_load_tables.setFont(font1)
        self.btn_load_tables.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
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
        self.btn_load_tables.setIconSize(QSize(30, 30))
        self.btn_load_tables.setFlat(True)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Database)

        QMetaObject.connectSlotsByName(Database)
    # setupUi

    def retranslateUi(self, Database):
        Database.setWindowTitle(QCoreApplication.translate("Database", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Database", u"Central Database", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Database", u"Username", None))
        self.label_36.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Database", u"Password", None))
        self.label_37.setText("")
        self.hostname.setPlaceholderText(QCoreApplication.translate("Database", u"Hostname", None))
        self.label_38.setText("")
        self.database_name.setPlaceholderText(QCoreApplication.translate("Database", u"Database", None))
        self.label_39.setText("")
        self.btn_connect_test.setText(QCoreApplication.translate("Database", u"Test connection", None))
        self.label_notification.setText(QCoreApplication.translate("Database", u"Notification", None))
        self.port.setPlaceholderText(QCoreApplication.translate("Database", u"Port", None))
        self.label_40.setText("")
        self.btn_update_properties.setText(QCoreApplication.translate("Database", u"Update", None))
        self.central_tablenam.setPlaceholderText(QCoreApplication.translate("Database", u"Tablename", None))
        self.btn_create_central_table.setText(QCoreApplication.translate("Database", u"Create", None))
        self.btn_load_tables.setText(QCoreApplication.translate("Database", u"Refresh", None))
    # retranslateUi

