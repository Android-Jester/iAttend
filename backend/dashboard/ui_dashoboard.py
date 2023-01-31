# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardgstzXB.ui'
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
import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1519, 1000)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setGeometry(QRect(0, 0, 1545, 1000))
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 1000))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.other_fields)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(5, 0))
        self.logo.setMaximumSize(QSize(60, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.options)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.options)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")

        self.horizontalLayout_19.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(100, 0))
        self.controls_frame.setMaximumSize(QSize(100, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(40, 20, 16, 16))
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
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(10, 20, 16, 16))
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
        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 16, 16))
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

        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(70, 0))
        self.menu_frame.setMaximumSize(QSize(80, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 635))
        self.frame.setMaximumSize(QSize(16777215, 635))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"padding-right:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(False)
        self.btn_home.setFlat(True)

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_database = QPushButton(self.frame)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setMinimumSize(QSize(0, 70))
        self.btn_database.setMaximumSize(QSize(16777215, 70))
        self.btn_database.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon1)
        self.btn_database.setIconSize(QSize(45, 45))
        self.btn_database.setCheckable(True)
        self.btn_database.setFlat(True)

        self.verticalLayout.addWidget(self.btn_database)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"padding-right:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon2)
        self.btn_search.setIconSize(QSize(42, 42))
        self.btn_search.setCheckable(True)
        self.btn_search.setFlat(True)

        self.verticalLayout.addWidget(self.btn_search)

        self.btn_batch = QPushButton(self.frame)
        self.btn_batch.setObjectName(u"btn_batch")
        self.btn_batch.setMinimumSize(QSize(0, 70))
        self.btn_batch.setMaximumSize(QSize(16777215, 70))
        self.btn_batch.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch.setIcon(icon3)
        self.btn_batch.setIconSize(QSize(40, 40))
        self.btn_batch.setFlat(True)

        self.verticalLayout.addWidget(self.btn_batch)

        self.btn_camera = QPushButton(self.frame)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(0, 70))
        self.btn_camera.setMaximumSize(QSize(16777215, 70))
        self.btn_camera.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon4)
        self.btn_camera.setIconSize(QSize(40, 40))
        self.btn_camera.setFlat(True)

        self.verticalLayout.addWidget(self.btn_camera)

        self.btn_report = QPushButton(self.frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(0, 70))
        self.btn_report.setMaximumSize(QSize(16777215, 70))
        self.btn_report.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"padding-right:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon5)
        self.btn_report.setIconSize(QSize(43, 43))
        self.btn_report.setFlat(True)

        self.verticalLayout.addWidget(self.btn_report)

        self.btn_mail_report_or_data = QPushButton(self.frame)
        self.btn_mail_report_or_data.setObjectName(u"btn_mail_report_or_data")
        self.btn_mail_report_or_data.setMinimumSize(QSize(0, 70))
        self.btn_mail_report_or_data.setMaximumSize(QSize(16777215, 70))
        self.btn_mail_report_or_data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mail_report_or_data.setIcon(icon6)
        self.btn_mail_report_or_data.setIconSize(QSize(40, 40))
        self.btn_mail_report_or_data.setFlat(True)

        self.verticalLayout.addWidget(self.btn_mail_report_or_data)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.btn_help = QPushButton(self.menu_frame)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 70))
        self.btn_help.setMaximumSize(QSize(16777215, 70))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon7)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_help)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 15, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 430))
        self.info_frame.setMaximumSize(QSize(16777215, 500))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 30, 261, 291))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 30, 191, 41))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.firstname.setFont(font3)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(290, 80, 191, 41))
        self.middlename.setFont(font3)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 130, 191, 41))
        self.lastname.setFont(font3)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(290, 180, 191, 41))
        self.refrence.setFont(font3)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(290, 230, 191, 41))
        self.index.setFont(font3)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coledge = QLabel(self.info_frame)
        self.coledge.setObjectName(u"coledge")
        self.coledge.setGeometry(QRect(290, 280, 191, 41))
        self.coledge.setFont(font3)
        self.coledge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.coledge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.validity = QLabel(self.info_frame)
        self.validity.setObjectName(u"validity")
        self.validity.setGeometry(QRect(20, 330, 261, 41))
        self.validity.setFont(font3)
        self.validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"\n"
"}")
        self.validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nationality = QLabel(self.info_frame)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setGeometry(QRect(290, 330, 191, 41))
        self.nationality.setFont(font3)
        self.nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.year = QLabel(self.info_frame)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(20, 380, 151, 41))
        self.year.setFont(font3)
        self.year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.program = QLabel(self.info_frame)
        self.program.setObjectName(u"program")
        self.program.setGeometry(QRect(180, 380, 301, 41))
        self.program.setFont(font3)
        self.program.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.program.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_out = QLabel(self.info_frame)
        self.last_out.setObjectName(u"last_out")
        self.last_out.setGeometry(QRect(20, 430, 291, 41))
        self.last_out.setFont(font3)
        self.last_out.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.last_out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 10, 481, 481))
        self.image_2.setFont(font2)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.last_in = QLabel(self.info_frame)
        self.last_in.setObjectName(u"last_in")
        self.last_in.setGeometry(QRect(320, 430, 161, 41))
        self.last_in.setFont(font3)
        self.last_in.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.last_in.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.middlename.raise_()
        self.lastname.raise_()
        self.refrence.raise_()
        self.index.raise_()
        self.coledge.raise_()
        self.validity.raise_()
        self.nationality.raise_()
        self.year.raise_()
        self.program.raise_()
        self.last_out.raise_()
        self.last_in.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 430))
        self.frame_3.setMaximumSize(QSize(16777215, 430))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 310, 481, 121))
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.camera_ip = QLineEdit(self.frame_3)
        self.camera_ip.setObjectName(u"camera_ip")
        self.camera_ip.setGeometry(QRect(20, 50, 461, 51))
        font4 = QFont()
        font4.setPointSize(10)
        self.camera_ip.setFont(font4)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_ip.setClearButtonEnabled(True)
        self.btn_connect_detect = QPushButton(self.frame_3)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(20, 120, 131, 41))
        self.btn_connect_detect.setFont(font4)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_connect_detect.setIcon(icon4)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, 60, 41, 31))
        self.label_27.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(160, 120, 141, 41))
        self.btn_disconnect.setFont(font4)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon8)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 120, 171, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.firstname_23 = QLabel(self.frame_3)
        self.firstname_23.setObjectName(u"firstname_23")
        self.firstname_23.setGeometry(QRect(10, 10, 481, 171))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.firstname_23.setFont(font5)
        self.firstname_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_24 = QLabel(self.frame_3)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(10, 210, 481, 81))
        self.firstname_24.setFont(font5)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_open_exit_camera_ui = QPushButton(self.frame_3)
        self.btn_open_exit_camera_ui.setObjectName(u"btn_open_exit_camera_ui")
        self.btn_open_exit_camera_ui.setGeometry(QRect(180, 230, 141, 41))
        self.btn_open_exit_camera_ui.setFont(font4)
        self.btn_open_exit_camera_ui.setStyleSheet(u"QPushButton{\n"
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
        self.btn_open_exit_camera_ui.setIcon(icon4)
        self.btn_open_exit_camera_ui.setIconSize(QSize(30, 30))
        self.btn_open_exit_camera_ui.setFlat(True)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(340, 230, 141, 41))
        self.btn_clear_label.setFont(font4)
        self.btn_clear_label.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon9)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_open_database = QPushButton(self.frame_3)
        self.btn_open_database.setObjectName(u"btn_open_database")
        self.btn_open_database.setGeometry(QRect(20, 230, 141, 41))
        self.btn_open_database.setFont(font4)
        self.btn_open_database.setStyleSheet(u"QPushButton{\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_database.setIcon(icon10)
        self.btn_open_database.setIconSize(QSize(30, 30))
        self.btn_open_database.setFlat(True)
        self.firstname_23.raise_()
        self.label_notification.raise_()
        self.camera_ip.raise_()
        self.btn_connect_detect.raise_()
        self.label_27.raise_()
        self.btn_disconnect.raise_()
        self.comboBox.raise_()
        self.firstname_24.raise_()
        self.btn_open_exit_camera_ui.raise_()
        self.btn_clear_label.raise_()
        self.btn_open_database.raise_()

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 700))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 700))
        self.camera_frame.setMaximumSize(QSize(16777215, 700))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font2)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_view.setAlignment(Qt.AlignCenter)
        self.camera_view.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(20)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(10)
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 3)

        self.brightness_value = QLabel(self.frame_4)
        self.brightness_value.setObjectName(u"brightness_value")
        self.brightness_value.setMinimumSize(QSize(50, 0))
        self.brightness_value.setMaximumSize(QSize(50, 16777215))
        self.brightness_value.setFont(font5)
        self.brightness_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_value, 4, 2, 1, 1)

        self.brightness_label = QLabel(self.frame_4)
        self.brightness_label.setObjectName(u"brightness_label")
        self.brightness_label.setFont(font5)
        self.brightness_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.brightness_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.brightness_label, 4, 0, 1, 1)

        self.brigthness = QSlider(self.frame_4)
        self.brigthness.setObjectName(u"brigthness")
        self.brigthness.setMaximum(100)
        self.brigthness.setValue(30)
        self.brigthness.setSliderPosition(30)
        self.brigthness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.brigthness, 4, 1, 1, 1)

        self.sharpness = QSlider(self.frame_4)
        self.sharpness.setObjectName(u"sharpness")
        self.sharpness.setMaximum(100)
        self.sharpness.setValue(50)
        self.sharpness.setSliderPosition(50)
        self.sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sharpness, 5, 1, 1, 1)

        self.sharp_label = QLabel(self.frame_4)
        self.sharp_label.setObjectName(u"sharp_label")
        self.sharp_label.setFont(font5)
        self.sharp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_label, 5, 0, 1, 1)

        self.sharp_value = QLabel(self.frame_4)
        self.sharp_value.setObjectName(u"sharp_value")
        self.sharp_value.setMinimumSize(QSize(50, 0))
        self.sharp_value.setMaximumSize(QSize(50, 16777215))
        self.sharp_value.setFont(font5)
        self.sharp_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.sharp_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sharp_value, 5, 2, 1, 1)

        self.contrast = QSlider(self.frame_4)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setStyleSheet(u"QSlider:groove:horizontal{\n"
"	margin:2px;\n"
"	height:1px;\n"
"}\n"
"")
        self.contrast.setMaximum(100)
        self.contrast.setValue(60)
        self.contrast.setSliderPosition(60)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.contrast, 6, 1, 1, 1)

        self.contrast_label = QLabel(self.frame_4)
        self.contrast_label.setObjectName(u"contrast_label")
        self.contrast_label.setFont(font5)
        self.contrast_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.contrast_label, 6, 0, 1, 1)

        self.contrast_value = QLabel(self.frame_4)
        self.contrast_value.setObjectName(u"contrast_value")
        self.contrast_value.setMinimumSize(QSize(50, 0))
        self.contrast_value.setMaximumSize(QSize(50, 16777215))
        self.contrast_value.setFont(font5)
        self.contrast_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.contrast_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.contrast_value, 6, 2, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 20, 150, 20))
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.scan_range_label = QLabel(self.frame_5)
        self.scan_range_label.setObjectName(u"scan_range_label")
        self.scan_range_label.setGeometry(QRect(20, 160, 431, 51))
        self.scan_range_label.setFont(font3)
        self.scan_range_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:45px;\n"
"\n"
"}")
        self.scan_range_label.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 170, 31, 31))
        self.label_42.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_42.setPixmap(QPixmap(u":/icons/asset/camera.svg"))
        self.btn_scan_range = QPushButton(self.frame_5)
        self.btn_scan_range.setObjectName(u"btn_scan_range")
        self.btn_scan_range.setGeometry(QRect(300, 80, 151, 51))
        self.btn_scan_range.setFont(font4)
        self.btn_scan_range.setStyleSheet(u"QPushButton{\n"
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
        self.btn_scan_range.setIcon(icon2)
        self.btn_scan_range.setIconSize(QSize(30, 30))
        self.btn_scan_range.setFlat(True)
        self.scan_range = QLineEdit(self.frame_5)
        self.scan_range.setObjectName(u"scan_range")
        self.scan_range.setGeometry(QRect(20, 80, 271, 51))
        self.scan_range.setFont(font4)
        self.scan_range.setStyleSheet(u"QLineEdit{\n"
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
        self.scan_range.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_frame_2 = QFrame(self.search)
        self.left_frame_2.setObjectName(u"left_frame_2")
        self.left_frame_2.setMinimumSize(QSize(500, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 500))
        self.top.setMaximumSize(QSize(500, 490))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_validity = QLabel(self.top)
        self.db_validity.setObjectName(u"db_validity")
        self.db_validity.setGeometry(QRect(20, 390, 261, 41))
        self.db_validity.setFont(font3)
        self.db_validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"}")
        self.db_validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(290, 240, 191, 41))
        self.db_refrence.setFont(font3)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_year = QLabel(self.top)
        self.db_year.setObjectName(u"db_year")
        self.db_year.setGeometry(QRect(20, 440, 151, 41))
        self.db_year.setFont(font3)
        self.db_year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_nationality = QLabel(self.top)
        self.db_nationality.setObjectName(u"db_nationality")
        self.db_nationality.setGeometry(QRect(290, 390, 191, 41))
        self.db_nationality.setFont(font3)
        self.db_nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 90, 261, 291))
        self.db_image_data.setFont(font2)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.db_image_data.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(290, 190, 191, 41))
        self.db_lastname.setFont(font3)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(290, 140, 191, 41))
        self.db_middlename.setFont(font3)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(290, 90, 191, 41))
        self.db_firstname.setFont(font3)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_index = QLabel(self.top)
        self.db_index.setObjectName(u"db_index")
        self.db_index.setGeometry(QRect(290, 290, 191, 41))
        self.db_index.setFont(font3)
        self.db_index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_programe = QLabel(self.top)
        self.db_programe.setObjectName(u"db_programe")
        self.db_programe.setGeometry(QRect(180, 440, 301, 41))
        self.db_programe.setFont(font3)
        self.db_programe.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_programe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_college = QLabel(self.top)
        self.db_college.setObjectName(u"db_college")
        self.db_college.setGeometry(QRect(290, 340, 191, 41))
        self.db_college.setFont(font3)
        self.db_college.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_college.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_box = QLineEdit(self.top)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(20, 20, 321, 41))
        self.search_box.setFont(font4)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
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
        self.search_box.setClearButtonEnabled(True)
        self.btn_search_page = QPushButton(self.top)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(350, 20, 131, 41))
        self.btn_search_page.setFont(font4)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
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
        self.btn_search_page.setIcon(icon2)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_29 = QLabel(self.top)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 481, 61))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_29.setFont(font7)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3 = QLabel(self.top)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setGeometry(QRect(10, 80, 481, 411))
        self.image_3.setFont(font2)
        self.image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_3.setAlignment(Qt.AlignCenter)
        self.image_3.raise_()
        self.label_29.raise_()
        self.db_validity.raise_()
        self.db_refrence.raise_()
        self.db_year.raise_()
        self.db_nationality.raise_()
        self.db_image_data.raise_()
        self.db_lastname.raise_()
        self.db_middlename.raise_()
        self.db_firstname.raise_()
        self.db_index.raise_()
        self.db_programe.raise_()
        self.db_college.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 300))
        self.bottom.setMaximumSize(QSize(16777215, 500))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.frame_6 = QFrame(self.bottom)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 190, 461, 240))
        self.frame_6.setMinimumSize(QSize(0, 240))
        self.frame_6.setMaximumSize(QSize(16777215, 240))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)

        self.verticalLayout_12.addWidget(self.calendarWidget)

        self.start_date = QRadioButton(self.bottom)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(20, 90, 261, 20))
        self.start_date.setFont(font6)
        self.start_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_date.setIcon(icon11)
        self.start_date.setChecked(True)
        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(20, 130, 211, 51))
        self.db_start_date.setFont(font4)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_start_date.setInputMethodHints(Qt.ImhPreferNumbers)
        self.db_start_date.setClearButtonEnabled(True)
        self.db_end_date = QLineEdit(self.bottom)
        self.db_end_date.setObjectName(u"db_end_date")
        self.db_end_date.setGeometry(QRect(260, 130, 221, 51))
        self.db_end_date.setFont(font4)
        self.db_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_end_date.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.bottom)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 140, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 80, 481, 361))
        self.label_30.setMinimumSize(QSize(0, 345))
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_reload = QPushButton(self.bottom)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setGeometry(QRect(340, 20, 141, 41))
        self.btn_reload.setFont(font4)
        self.btn_reload.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}")
        self.btn_reload.setIcon(icon9)
        self.btn_reload.setIconSize(QSize(30, 30))
        self.btn_reload.setFlat(True)
        self.btn_csv = QPushButton(self.bottom)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setGeometry(QRect(20, 20, 131, 41))
        self.btn_csv.setFont(font4)
        self.btn_csv.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_csv.setIcon(icon12)
        self.btn_csv.setIconSize(QSize(30, 30))
        self.btn_csv.setFlat(True)
        self.label_26 = QLabel(self.bottom)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 140, 31, 31))
        self.label_26.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_40 = QLabel(self.bottom)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 10, 481, 61))
        self.label_40.setFont(font7)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox = QCheckBox(self.bottom)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(290, 90, 191, 20))
        self.checkBox.setFont(font4)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/asset/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon13)
        self.btn_json = QPushButton(self.bottom)
        self.btn_json.setObjectName(u"btn_json")
        self.btn_json.setGeometry(QRect(170, 20, 151, 41))
        self.btn_json.setFont(font4)
        self.btn_json.setStyleSheet(u"QPushButton{\n"
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
        self.btn_json.setIcon(icon12)
        self.btn_json.setIconSize(QSize(30, 30))
        self.btn_json.setFlat(True)
        self.label_40.raise_()
        self.label_30.raise_()
        self.frame_6.raise_()
        self.start_date.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.db_end_date.raise_()
        self.btn_reload.raise_()
        self.btn_csv.raise_()
        self.label_26.raise_()
        self.checkBox.raise_()
        self.btn_json.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.NoFrame)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 9, 12)
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_5.addWidget(self.rigth_frame)

        self.stackedWidget.addWidget(self.search)
        self.batch = QWidget()
        self.batch.setObjectName(u"batch")
        self.verticalLayout_20 = QVBoxLayout(self.batch)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_27 = QFrame(self.batch)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 100))
        self.frame_27.setMaximumSize(QSize(16777215, 100))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_27)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, 0, 1101, 91))
        self.label_45.setFont(font7)
        self.label_45.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.batch_notification = QLabel(self.frame_27)
        self.batch_notification.setObjectName(u"batch_notification")
        self.batch_notification.setGeometry(QRect(1120, 0, 301, 91))
        font8 = QFont()
        font8.setFamily(u"Microsoft Sans Serif")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.batch_notification.setFont(font8)
        self.batch_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.batch_notification.setAlignment(Qt.AlignCenter)
        self.batch_notification.setWordWrap(True)
        self.btn_batch_browse = QPushButton(self.frame_27)
        self.btn_batch_browse.setObjectName(u"btn_batch_browse")
        self.btn_batch_browse.setGeometry(QRect(340, 20, 131, 51))
        self.btn_batch_browse.setFont(font4)
        self.btn_batch_browse.setStyleSheet(u"QPushButton{\n"
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
        self.btn_batch_browse.setIcon(icon12)
        self.btn_batch_browse.setIconSize(QSize(30, 30))
        self.btn_batch_browse.setFlat(True)
        self.batch_browse = QLineEdit(self.frame_27)
        self.batch_browse.setObjectName(u"batch_browse")
        self.batch_browse.setGeometry(QRect(20, 20, 301, 51))
        self.batch_browse.setFont(font4)
        self.batch_browse.setStyleSheet(u"QLineEdit{\n"
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
        self.batch_browse.setReadOnly(True)
        self.batch_browse.setClearButtonEnabled(True)
        self.btn_start_job = QPushButton(self.frame_27)
        self.btn_start_job.setObjectName(u"btn_start_job")
        self.btn_start_job.setGeometry(QRect(490, 20, 131, 51))
        self.btn_start_job.setFont(font4)
        self.btn_start_job.setStyleSheet(u"QPushButton{\n"
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
        self.btn_start_job.setIcon(icon11)
        self.btn_start_job.setIconSize(QSize(30, 30))
        self.btn_start_job.setFlat(True)
        self.btn_batch_mail = QPushButton(self.frame_27)
        self.btn_batch_mail.setObjectName(u"btn_batch_mail")
        self.btn_batch_mail.setGeometry(QRect(940, 20, 141, 51))
        self.btn_batch_mail.setFont(font4)
        self.btn_batch_mail.setStyleSheet(u"QPushButton{\n"
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
        self.btn_batch_mail.setIcon(icon6)
        self.btn_batch_mail.setIconSize(QSize(30, 30))
        self.btn_batch_mail.setFlat(True)
        self.btn_batch_folder = QPushButton(self.frame_27)
        self.btn_batch_folder.setObjectName(u"btn_batch_folder")
        self.btn_batch_folder.setGeometry(QRect(640, 20, 131, 51))
        self.btn_batch_folder.setFont(font4)
        self.btn_batch_folder.setStyleSheet(u"QPushButton{\n"
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
        icon14 = QIcon()
        icon14.addFile(u":/icons/asset/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch_folder.setIcon(icon14)
        self.btn_batch_folder.setIconSize(QSize(30, 30))
        self.btn_batch_folder.setFlat(True)
        self.btn_batch_images = QPushButton(self.frame_27)
        self.btn_batch_images.setObjectName(u"btn_batch_images")
        self.btn_batch_images.setGeometry(QRect(790, 20, 131, 51))
        self.btn_batch_images.setFont(font4)
        self.btn_batch_images.setStyleSheet(u"QPushButton{\n"
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
        icon15 = QIcon()
        icon15.addFile(u":/icons/asset/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch_images.setIcon(icon15)
        self.btn_batch_images.setIconSize(QSize(30, 30))
        self.btn_batch_images.setFlat(True)

        self.verticalLayout_20.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.batch)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_29)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_batch = QTableWidget(self.frame_29)
        if (self.tableWidget_batch.columnCount() < 8):
            self.tableWidget_batch.setColumnCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.tableWidget_batch.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        self.tableWidget_batch.setObjectName(u"tableWidget_batch")
        self.tableWidget_batch.setFont(font4)
        self.tableWidget_batch.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_batch.setFrameShape(QFrame.NoFrame)
        self.tableWidget_batch.setFrameShadow(QFrame.Plain)
        self.tableWidget_batch.setSortingEnabled(True)
        self.tableWidget_batch.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_batch.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_batch.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.tableWidget_batch)


        self.verticalLayout_20.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.batch)
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.horizontalLayout_6 = QHBoxLayout(self.camera)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_child = QFrame(self.camera)
        self.left_child.setObjectName(u"left_child")
        self.left_child.setMaximumSize(QSize(450, 16777215))
        self.left_child.setFrameShape(QFrame.NoFrame)
        self.left_child.setFrameShadow(QFrame.Plain)
        self.firstname_25 = QLabel(self.left_child)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 10, 441, 201))
        self.firstname_25.setFont(font5)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_camera_one_connect = QPushButton(self.left_child)
        self.btn_camera_one_connect.setObjectName(u"btn_camera_one_connect")
        self.btn_camera_one_connect.setGeometry(QRect(20, 150, 131, 41))
        self.btn_camera_one_connect.setFont(font4)
        self.btn_camera_one_connect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_one_connect.setIcon(icon4)
        self.btn_camera_one_connect.setIconSize(QSize(30, 30))
        self.btn_camera_one_connect.setFlat(True)
        self.btn_camera_one_disconnect = QPushButton(self.left_child)
        self.btn_camera_one_disconnect.setObjectName(u"btn_camera_one_disconnect")
        self.btn_camera_one_disconnect.setGeometry(QRect(160, 150, 141, 41))
        self.btn_camera_one_disconnect.setFont(font4)
        self.btn_camera_one_disconnect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_one_disconnect.setIcon(icon8)
        self.btn_camera_one_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_one_disconnect.setFlat(True)
        self.camera_one_comboBox = QComboBox(self.left_child)
        self.camera_one_comboBox.setObjectName(u"camera_one_comboBox")
        self.camera_one_comboBox.setGeometry(QRect(330, 80, 111, 50))
        self.camera_one_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_one_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_one_comboBox.setFont(font4)
        self.camera_one_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_one_comboBox.setFrame(False)
        self.camera_one_id_ip = QLineEdit(self.left_child)
        self.camera_one_id_ip.setObjectName(u"camera_one_id_ip")
        self.camera_one_id_ip.setGeometry(QRect(20, 80, 301, 51))
        self.camera_one_id_ip.setFont(font4)
        self.camera_one_id_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_one_id_ip.setClearButtonEnabled(True)
        self.label_31 = QLabel(self.left_child)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 90, 41, 31))
        self.label_31.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_two_disconnect = QPushButton(self.left_child)
        self.btn_camera_two_disconnect.setObjectName(u"btn_camera_two_disconnect")
        self.btn_camera_two_disconnect.setGeometry(QRect(160, 390, 141, 41))
        self.btn_camera_two_disconnect.setFont(font4)
        self.btn_camera_two_disconnect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_two_disconnect.setIcon(icon8)
        self.btn_camera_two_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_two_disconnect.setFlat(True)
        self.camera_two_id_ip = QLineEdit(self.left_child)
        self.camera_two_id_ip.setObjectName(u"camera_two_id_ip")
        self.camera_two_id_ip.setGeometry(QRect(20, 320, 301, 51))
        self.camera_two_id_ip.setFont(font4)
        self.camera_two_id_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_two_id_ip.setClearButtonEnabled(True)
        self.btn_camera_two_connect = QPushButton(self.left_child)
        self.btn_camera_two_connect.setObjectName(u"btn_camera_two_connect")
        self.btn_camera_two_connect.setGeometry(QRect(20, 390, 131, 41))
        self.btn_camera_two_connect.setFont(font4)
        self.btn_camera_two_connect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_two_connect.setIcon(icon4)
        self.btn_camera_two_connect.setIconSize(QSize(30, 30))
        self.btn_camera_two_connect.setFlat(True)
        self.firstname_26 = QLabel(self.left_child)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 260, 441, 191))
        self.firstname_26.setFont(font5)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_32 = QLabel(self.left_child)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(30, 330, 41, 31))
        self.label_32.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_three_disconnect = QPushButton(self.left_child)
        self.btn_camera_three_disconnect.setObjectName(u"btn_camera_three_disconnect")
        self.btn_camera_three_disconnect.setGeometry(QRect(160, 630, 141, 41))
        self.btn_camera_three_disconnect.setFont(font4)
        self.btn_camera_three_disconnect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_three_disconnect.setIcon(icon8)
        self.btn_camera_three_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_three_disconnect.setFlat(True)
        self.camera_three_id_ip = QLineEdit(self.left_child)
        self.camera_three_id_ip.setObjectName(u"camera_three_id_ip")
        self.camera_three_id_ip.setGeometry(QRect(20, 560, 301, 51))
        self.camera_three_id_ip.setFont(font4)
        self.camera_three_id_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_three_id_ip.setClearButtonEnabled(True)
        self.btn_camera_three_connect = QPushButton(self.left_child)
        self.btn_camera_three_connect.setObjectName(u"btn_camera_three_connect")
        self.btn_camera_three_connect.setGeometry(QRect(20, 630, 131, 41))
        self.btn_camera_three_connect.setFont(font4)
        self.btn_camera_three_connect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_three_connect.setIcon(icon4)
        self.btn_camera_three_connect.setIconSize(QSize(30, 30))
        self.btn_camera_three_connect.setFlat(True)
        self.firstname_27 = QLabel(self.left_child)
        self.firstname_27.setObjectName(u"firstname_27")
        self.firstname_27.setGeometry(QRect(10, 500, 441, 191))
        self.firstname_27.setFont(font5)
        self.firstname_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_33 = QLabel(self.left_child)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 570, 41, 31))
        self.label_33.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_four_disconnect = QPushButton(self.left_child)
        self.btn_camera_four_disconnect.setObjectName(u"btn_camera_four_disconnect")
        self.btn_camera_four_disconnect.setGeometry(QRect(160, 870, 141, 41))
        self.btn_camera_four_disconnect.setFont(font4)
        self.btn_camera_four_disconnect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_four_disconnect.setIcon(icon8)
        self.btn_camera_four_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_four_disconnect.setFlat(True)
        self.camera_four_id_ip = QLineEdit(self.left_child)
        self.camera_four_id_ip.setObjectName(u"camera_four_id_ip")
        self.camera_four_id_ip.setGeometry(QRect(20, 800, 301, 51))
        self.camera_four_id_ip.setFont(font4)
        self.camera_four_id_ip.setStyleSheet(u"QLineEdit{\n"
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
        self.camera_four_id_ip.setClearButtonEnabled(True)
        self.btn_camera_four_connect = QPushButton(self.left_child)
        self.btn_camera_four_connect.setObjectName(u"btn_camera_four_connect")
        self.btn_camera_four_connect.setGeometry(QRect(20, 870, 131, 41))
        self.btn_camera_four_connect.setFont(font4)
        self.btn_camera_four_connect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_four_connect.setIcon(icon4)
        self.btn_camera_four_connect.setIconSize(QSize(30, 30))
        self.btn_camera_four_connect.setFlat(True)
        self.firstname_28 = QLabel(self.left_child)
        self.firstname_28.setObjectName(u"firstname_28")
        self.firstname_28.setGeometry(QRect(10, 740, 441, 191))
        self.firstname_28.setFont(font5)
        self.firstname_28.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_34 = QLabel(self.left_child)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 810, 41, 31))
        self.label_34.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_cast_cam_one = QPushButton(self.left_child)
        self.btn_cast_cam_one.setObjectName(u"btn_cast_cam_one")
        self.btn_cast_cam_one.setGeometry(QRect(310, 150, 131, 41))
        self.btn_cast_cam_one.setFont(font4)
        self.btn_cast_cam_one.setStyleSheet(u"QPushButton{\n"
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
        icon16 = QIcon()
        icon16.addFile(u":/icons/asset/cast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cast_cam_one.setIcon(icon16)
        self.btn_cast_cam_one.setIconSize(QSize(30, 30))
        self.btn_cast_cam_one.setFlat(True)
        self.camera_two_comboBox = QComboBox(self.left_child)
        self.camera_two_comboBox.setObjectName(u"camera_two_comboBox")
        self.camera_two_comboBox.setGeometry(QRect(330, 320, 111, 50))
        self.camera_two_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_two_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_two_comboBox.setFont(font4)
        self.camera_two_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_two_comboBox.setFrame(False)
        self.btn_cast_cam_one_2 = QPushButton(self.left_child)
        self.btn_cast_cam_one_2.setObjectName(u"btn_cast_cam_one_2")
        self.btn_cast_cam_one_2.setGeometry(QRect(310, 390, 131, 41))
        self.btn_cast_cam_one_2.setFont(font4)
        self.btn_cast_cam_one_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_cast_cam_one_2.setIcon(icon16)
        self.btn_cast_cam_one_2.setIconSize(QSize(30, 30))
        self.btn_cast_cam_one_2.setFlat(True)
        self.camera_three_comboBox = QComboBox(self.left_child)
        self.camera_three_comboBox.setObjectName(u"camera_three_comboBox")
        self.camera_three_comboBox.setGeometry(QRect(330, 560, 111, 50))
        self.camera_three_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_three_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_three_comboBox.setFont(font4)
        self.camera_three_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_three_comboBox.setFrame(False)
        self.btn_cast_cam_three = QPushButton(self.left_child)
        self.btn_cast_cam_three.setObjectName(u"btn_cast_cam_three")
        self.btn_cast_cam_three.setGeometry(QRect(310, 630, 131, 41))
        self.btn_cast_cam_three.setFont(font4)
        self.btn_cast_cam_three.setStyleSheet(u"QPushButton{\n"
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
        self.btn_cast_cam_three.setIcon(icon16)
        self.btn_cast_cam_three.setIconSize(QSize(30, 30))
        self.btn_cast_cam_three.setFlat(True)
        self.camera_four_comboBox = QComboBox(self.left_child)
        self.camera_four_comboBox.setObjectName(u"camera_four_comboBox")
        self.camera_four_comboBox.setGeometry(QRect(330, 800, 111, 50))
        self.camera_four_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_four_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_four_comboBox.setFont(font4)
        self.camera_four_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_four_comboBox.setFrame(False)
        self.btn_cast_cam_four = QPushButton(self.left_child)
        self.btn_cast_cam_four.setObjectName(u"btn_cast_cam_four")
        self.btn_cast_cam_four.setGeometry(QRect(310, 870, 131, 41))
        self.btn_cast_cam_four.setFont(font4)
        self.btn_cast_cam_four.setStyleSheet(u"QPushButton{\n"
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
        self.btn_cast_cam_four.setIcon(icon16)
        self.btn_cast_cam_four.setIconSize(QSize(30, 30))
        self.btn_cast_cam_four.setFlat(True)
        self.firstname_28.raise_()
        self.firstname_27.raise_()
        self.firstname_26.raise_()
        self.firstname_25.raise_()
        self.btn_camera_one_connect.raise_()
        self.btn_camera_one_disconnect.raise_()
        self.camera_one_comboBox.raise_()
        self.camera_one_id_ip.raise_()
        self.label_31.raise_()
        self.btn_camera_two_disconnect.raise_()
        self.camera_two_id_ip.raise_()
        self.btn_camera_two_connect.raise_()
        self.label_32.raise_()
        self.btn_camera_three_disconnect.raise_()
        self.camera_three_id_ip.raise_()
        self.btn_camera_three_connect.raise_()
        self.label_33.raise_()
        self.btn_camera_four_disconnect.raise_()
        self.camera_four_id_ip.raise_()
        self.btn_camera_four_connect.raise_()
        self.label_34.raise_()
        self.btn_cast_cam_one.raise_()
        self.camera_two_comboBox.raise_()
        self.btn_cast_cam_one_2.raise_()
        self.camera_three_comboBox.raise_()
        self.btn_cast_cam_three.raise_()
        self.camera_four_comboBox.raise_()
        self.btn_cast_cam_four.raise_()

        self.horizontalLayout_6.addWidget(self.left_child)

        self.rignt_child = QFrame(self.camera)
        self.rignt_child.setObjectName(u"rignt_child")
        self.rignt_child.setFrameShape(QFrame.NoFrame)
        self.rignt_child.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.rignt_child)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.camera_down = QFrame(self.rignt_child)
        self.camera_down.setObjectName(u"camera_down")
        self.camera_down.setFrameShape(QFrame.StyledPanel)
        self.camera_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.camera_down)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.camera_1 = QLabel(self.camera_down)
        self.camera_1.setObjectName(u"camera_1")
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.camera_1.setFont(font9)
        self.camera_1.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_1.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_1)

        self.camera_2 = QLabel(self.camera_down)
        self.camera_2.setObjectName(u"camera_2")
        self.camera_2.setFont(font9)
        self.camera_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_2.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_2)


        self.verticalLayout_10.addWidget(self.camera_down)

        self.camera_top = QFrame(self.rignt_child)
        self.camera_top.setObjectName(u"camera_top")
        self.camera_top.setFrameShape(QFrame.StyledPanel)
        self.camera_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.camera_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.camera_3 = QLabel(self.camera_top)
        self.camera_3.setObjectName(u"camera_3")
        self.camera_3.setFont(font9)
        self.camera_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_3.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_3)

        self.camera_4 = QLabel(self.camera_top)
        self.camera_4.setObjectName(u"camera_4")
        self.camera_4.setFont(font9)
        self.camera_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_4.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_4)


        self.verticalLayout_10.addWidget(self.camera_top)


        self.horizontalLayout_6.addWidget(self.rignt_child)

        self.stackedWidget.addWidget(self.camera)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.horizontalLayout_14 = QHBoxLayout(self.database)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.left_fram_reg = QFrame(self.database)
        self.left_fram_reg.setObjectName(u"left_fram_reg")
        self.left_fram_reg.setMinimumSize(QSize(660, 0))
        self.left_fram_reg.setMaximumSize(QSize(500, 16777215))
        self.left_fram_reg.setFrameShape(QFrame.NoFrame)
        self.left_fram_reg.setFrameShadow(QFrame.Raised)
        self.reg_image = QLabel(self.left_fram_reg)
        self.reg_image.setObjectName(u"reg_image")
        self.reg_image.setGeometry(QRect(30, 130, 291, 291))
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.reg_image.setFont(font10)
        self.reg_image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.reg_image.setAlignment(Qt.AlignCenter)
        self.reg_firstname = QLineEdit(self.left_fram_reg)
        self.reg_firstname.setObjectName(u"reg_firstname")
        self.reg_firstname.setGeometry(QRect(340, 130, 291, 51))
        self.reg_firstname.setFont(font4)
        self.reg_firstname.setTabletTracking(True)
        self.reg_firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_firstname.setClearButtonEnabled(True)
        self.reg_image_2 = QLabel(self.left_fram_reg)
        self.reg_image_2.setObjectName(u"reg_image_2")
        self.reg_image_2.setGeometry(QRect(10, 110, 641, 511))
        self.reg_image_2.setFont(font10)
        self.reg_image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_2.setAlignment(Qt.AlignCenter)
        self.reg_middlename = QLineEdit(self.left_fram_reg)
        self.reg_middlename.setObjectName(u"reg_middlename")
        self.reg_middlename.setGeometry(QRect(340, 190, 291, 51))
        self.reg_middlename.setFont(font4)
        self.reg_middlename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_middlename.setClearButtonEnabled(True)
        self.reg_lastname = QLineEdit(self.left_fram_reg)
        self.reg_lastname.setObjectName(u"reg_lastname")
        self.reg_lastname.setGeometry(QRect(340, 250, 291, 51))
        self.reg_lastname.setFont(font4)
        self.reg_lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_lastname.setClearButtonEnabled(True)
        self.reg_index = QLineEdit(self.left_fram_reg)
        self.reg_index.setObjectName(u"reg_index")
        self.reg_index.setGeometry(QRect(340, 370, 291, 51))
        self.reg_index.setFont(font4)
        self.reg_index.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_index.setClearButtonEnabled(True)
        self.reg_college = QLineEdit(self.left_fram_reg)
        self.reg_college.setObjectName(u"reg_college")
        self.reg_college.setGeometry(QRect(340, 430, 291, 51))
        self.reg_college.setFont(font4)
        self.reg_college.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_college.setClearButtonEnabled(True)
        self.reg_student_ref = QLineEdit(self.left_fram_reg)
        self.reg_student_ref.setObjectName(u"reg_student_ref")
        self.reg_student_ref.setGeometry(QRect(340, 310, 291, 51))
        self.reg_student_ref.setFont(font4)
        self.reg_student_ref.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_student_ref.setClearButtonEnabled(True)
        self.reg_nationality = QLineEdit(self.left_fram_reg)
        self.reg_nationality.setObjectName(u"reg_nationality")
        self.reg_nationality.setGeometry(QRect(30, 430, 291, 51))
        self.reg_nationality.setFont(font4)
        self.reg_nationality.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_nationality.setClearButtonEnabled(True)
        self.reg_start_date = QLineEdit(self.left_fram_reg)
        self.reg_start_date.setObjectName(u"reg_start_date")
        self.reg_start_date.setGeometry(QRect(30, 490, 291, 51))
        self.reg_start_date.setFont(font4)
        self.reg_start_date.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_start_date.setClearButtonEnabled(True)
        self.reg_end_date = QLineEdit(self.left_fram_reg)
        self.reg_end_date.setObjectName(u"reg_end_date")
        self.reg_end_date.setGeometry(QRect(340, 490, 291, 51))
        self.reg_end_date.setFont(font4)
        self.reg_end_date.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_end_date.setClearButtonEnabled(True)
        self.label_35 = QLabel(self.left_fram_reg)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(40, 500, 31, 31))
        self.label_35.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.reg_programs = QComboBox(self.left_fram_reg)
        self.reg_programs.setObjectName(u"reg_programs")
        self.reg_programs.setGeometry(QRect(340, 550, 291, 50))
        self.reg_programs.setMinimumSize(QSize(0, 50))
        self.reg_programs.setMaximumSize(QSize(16777215, 50))
        self.reg_programs.setFont(font4)
        self.reg_programs.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_programs.setFrame(False)
        self.btn_search_reg = QPushButton(self.left_fram_reg)
        self.btn_search_reg.setObjectName(u"btn_search_reg")
        self.btn_search_reg.setGeometry(QRect(510, 30, 121, 41))
        self.btn_search_reg.setFont(font4)
        self.btn_search_reg.setStyleSheet(u"QPushButton{\n"
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
        self.btn_search_reg.setIcon(icon2)
        self.btn_search_reg.setIconSize(QSize(30, 30))
        self.btn_search_reg.setFlat(True)
        self.label_37 = QLabel(self.left_fram_reg)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 10, 641, 81))
        self.label_37.setFont(font7)
        self.label_37.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_reg = QLineEdit(self.left_fram_reg)
        self.search_reg.setObjectName(u"search_reg")
        self.search_reg.setGeometry(QRect(30, 30, 461, 41))
        self.search_reg.setFont(font4)
        self.search_reg.setStyleSheet(u"QLineEdit{\n"
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
        self.search_reg.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.left_fram_reg)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 640, 641, 61))
        self.label_38.setFont(font7)
        self.label_38.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_register = QPushButton(self.left_fram_reg)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(30, 650, 131, 41))
        self.btn_register.setFont(font4)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
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
        self.btn_register.setIcon(icon1)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.btn_update = QPushButton(self.left_fram_reg)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(190, 650, 131, 41))
        self.btn_update.setFont(font4)
        self.btn_update.setStyleSheet(u"QPushButton{\n"
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
        self.btn_update.setIcon(icon15)
        self.btn_update.setIconSize(QSize(30, 30))
        self.btn_update.setFlat(True)
        self.btn_remove = QPushButton(self.left_fram_reg)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(340, 650, 131, 41))
        self.btn_remove.setFont(font4)
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
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
        icon17 = QIcon()
        icon17.addFile(u":/icons/asset/user-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon17)
        self.btn_remove.setIconSize(QSize(30, 30))
        self.btn_remove.setFlat(True)
        self.btn_clear = QPushButton(self.left_fram_reg)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(500, 650, 131, 41))
        self.btn_clear.setFont(font4)
        self.btn_clear.setStyleSheet(u"QPushButton{\n"
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
        self.btn_clear.setIcon(icon9)
        self.btn_clear.setIconSize(QSize(30, 30))
        self.btn_clear.setFlat(True)
        self.label_39 = QLabel(self.left_fram_reg)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 810, 641, 131))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.image_file_reg = QLineEdit(self.left_fram_reg)
        self.image_file_reg.setObjectName(u"image_file_reg")
        self.image_file_reg.setGeometry(QRect(30, 870, 451, 51))
        self.image_file_reg.setFont(font4)
        self.image_file_reg.setStyleSheet(u"QLineEdit{\n"
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
        self.image_file_reg.setClearButtonEnabled(True)
        self.btn_browse_reg = QPushButton(self.left_fram_reg)
        self.btn_browse_reg.setObjectName(u"btn_browse_reg")
        self.btn_browse_reg.setGeometry(QRect(510, 870, 121, 51))
        self.btn_browse_reg.setFont(font4)
        self.btn_browse_reg.setStyleSheet(u"QPushButton{\n"
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
        self.btn_browse_reg.setIcon(icon3)
        self.btn_browse_reg.setIconSize(QSize(30, 30))
        self.btn_browse_reg.setFlat(True)
        self.reg_college_2 = QComboBox(self.left_fram_reg)
        self.reg_college_2.setObjectName(u"reg_college_2")
        self.reg_college_2.setGeometry(QRect(30, 550, 291, 50))
        self.reg_college_2.setMinimumSize(QSize(0, 50))
        self.reg_college_2.setMaximumSize(QSize(16777215, 50))
        self.reg_college_2.setFont(font4)
        self.reg_college_2.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_college_2.setFrame(False)
        self.label_36 = QLabel(self.left_fram_reg)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(350, 500, 31, 31))
        self.label_36.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.file_system = QRadioButton(self.left_fram_reg)
        self.file_system.setObjectName(u"file_system")
        self.file_system.setGeometry(QRect(220, 840, 131, 20))
        self.file_system.setFont(font4)
        self.file_system.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.file_system.setIcon(icon15)
        self.online_image = QRadioButton(self.left_fram_reg)
        self.online_image.setObjectName(u"online_image")
        self.online_image.setGeometry(QRect(110, 840, 101, 20))
        self.online_image.setFont(font4)
        self.online_image.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/asset/download-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.online_image.setIcon(icon18)
        self.reg_email = QLineEdit(self.left_fram_reg)
        self.reg_email.setObjectName(u"reg_email")
        self.reg_email.setGeometry(QRect(30, 730, 421, 51))
        self.reg_email.setFont(font4)
        self.reg_email.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
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
        self.reg_email.setClearButtonEnabled(True)
        self.label_43 = QLabel(self.left_fram_reg)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 720, 641, 71))
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_44 = QLabel(self.left_fram_reg)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(40, 740, 31, 31))
        self.label_44.setPixmap(QPixmap(u":/icons/asset/mail.svg"))
        self.btn_send_mail = QPushButton(self.left_fram_reg)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        self.btn_send_mail.setGeometry(QRect(470, 730, 161, 51))
        self.btn_send_mail.setFont(font4)
        self.btn_send_mail.setStyleSheet(u"QPushButton{\n"
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
        icon19 = QIcon()
        icon19.addFile(u":/icons/asset/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_mail.setIcon(icon19)
        self.btn_send_mail.setIconSize(QSize(30, 30))
        self.btn_send_mail.setFlat(True)
        self.image_less = QRadioButton(self.left_fram_reg)
        self.image_less.setObjectName(u"image_less")
        self.image_less.setGeometry(QRect(340, 840, 131, 20))
        self.image_less.setFont(font4)
        self.image_less.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);")
        self.image_less.setIcon(icon15)
        self.label_43.raise_()
        self.label_37.raise_()
        self.search_reg.raise_()
        self.reg_image_2.raise_()
        self.reg_image.raise_()
        self.reg_firstname.raise_()
        self.reg_middlename.raise_()
        self.reg_lastname.raise_()
        self.reg_index.raise_()
        self.reg_college.raise_()
        self.reg_student_ref.raise_()
        self.reg_nationality.raise_()
        self.reg_start_date.raise_()
        self.label_35.raise_()
        self.reg_programs.raise_()
        self.btn_search_reg.raise_()
        self.label_38.raise_()
        self.btn_register.raise_()
        self.btn_update.raise_()
        self.btn_remove.raise_()
        self.btn_clear.raise_()
        self.label_39.raise_()
        self.image_file_reg.raise_()
        self.btn_browse_reg.raise_()
        self.reg_college_2.raise_()
        self.reg_end_date.raise_()
        self.label_36.raise_()
        self.file_system.raise_()
        self.online_image.raise_()
        self.reg_email.raise_()
        self.label_44.raise_()
        self.btn_send_mail.raise_()
        self.image_less.raise_()

        self.horizontalLayout_14.addWidget(self.left_fram_reg)

        self.right_frame_reg = QFrame(self.database)
        self.right_frame_reg.setObjectName(u"right_frame_reg")
        self.right_frame_reg.setFrameShape(QFrame.NoFrame)
        self.right_frame_reg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.right_frame_reg)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 10, 0)
        self.frame_11 = QFrame(self.right_frame_reg)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 470))
        self.frame_15.setMaximumSize(QSize(16777215, 470))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_15)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.reg_cap_frame = QLabel(self.frame_15)
        self.reg_cap_frame.setObjectName(u"reg_cap_frame")
        self.reg_cap_frame.setFont(font10)
        self.reg_cap_frame.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_cap_frame.setPixmap(QPixmap(u":/icons/asset/camera.svg"))
        self.reg_cap_frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.reg_cap_frame)


        self.verticalLayout_18.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 200))
        self.frame_16.setMaximumSize(QSize(16777215, 200))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(350, 0))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_17)
        self.verticalLayout_24.setSpacing(9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius:10px;")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.btn_camera_reg_connect = QPushButton(self.frame_24)
        self.btn_camera_reg_connect.setObjectName(u"btn_camera_reg_connect")
        self.btn_camera_reg_connect.setGeometry(QRect(20, 140, 141, 41))
        self.btn_camera_reg_connect.setFont(font4)
        self.btn_camera_reg_connect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_reg_connect.setIcon(icon4)
        self.btn_camera_reg_connect.setIconSize(QSize(30, 30))
        self.btn_camera_reg_connect.setFlat(True)
        self.reg_camera_combo = QComboBox(self.frame_24)
        self.reg_camera_combo.setObjectName(u"reg_camera_combo")
        self.reg_camera_combo.setGeometry(QRect(20, 80, 311, 45))
        self.reg_camera_combo.setMinimumSize(QSize(0, 45))
        self.reg_camera_combo.setMaximumSize(QSize(16777215, 45))
        self.reg_camera_combo.setFont(font4)
        self.reg_camera_combo.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"background-color: rgb(45, 45, 45);\n"
"}")
        self.reg_camera_combo.setFrame(False)
        self.btn_camera_reg_disconnect = QPushButton(self.frame_24)
        self.btn_camera_reg_disconnect.setObjectName(u"btn_camera_reg_disconnect")
        self.btn_camera_reg_disconnect.setGeometry(QRect(180, 140, 151, 41))
        self.btn_camera_reg_disconnect.setFont(font4)
        self.btn_camera_reg_disconnect.setStyleSheet(u"QPushButton{\n"
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
        self.btn_camera_reg_disconnect.setIcon(icon8)
        self.btn_camera_reg_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_reg_disconnect.setFlat(True)
        self.reg_camera_ip = QLineEdit(self.frame_24)
        self.reg_camera_ip.setObjectName(u"reg_camera_ip")
        self.reg_camera_ip.setGeometry(QRect(20, 20, 311, 51))
        self.reg_camera_ip.setFont(font4)
        self.reg_camera_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_camera_ip.setClearButtonEnabled(True)
        self.label_41 = QLabel(self.frame_24)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 30, 41, 31))
        self.label_41.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_41.setPixmap(QPixmap(u":/icons/asset/video.svg"))

        self.verticalLayout_24.addWidget(self.frame_24)


        self.horizontalLayout_11.addWidget(self.frame_17)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius:10px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_23)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(30)
        self.label_2 = QLabel(self.frame_23)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.reg_brigthness_slider = QSlider(self.frame_23)
        self.reg_brigthness_slider.setObjectName(u"reg_brigthness_slider")
        self.reg_brigthness_slider.setMinimumSize(QSize(240, 0))
        self.reg_brigthness_slider.setMaximumSize(QSize(240, 16777215))
        self.reg_brigthness_slider.setValue(30)
        self.reg_brigthness_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.reg_brigthness_slider, 1, 1, 1, 1)

        self.reg_bright_value = QLabel(self.frame_23)
        self.reg_bright_value.setObjectName(u"reg_bright_value")
        self.reg_bright_value.setFont(font4)
        self.reg_bright_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.reg_bright_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.reg_bright_value, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame_23)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)

        self.reg_sharpness_slider = QSlider(self.frame_23)
        self.reg_sharpness_slider.setObjectName(u"reg_sharpness_slider")
        self.reg_sharpness_slider.setMinimumSize(QSize(240, 0))
        self.reg_sharpness_slider.setMaximumSize(QSize(240, 16777215))
        self.reg_sharpness_slider.setValue(50)
        self.reg_sharpness_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.reg_sharpness_slider, 2, 1, 1, 1)

        self.reg_sharpness_value = QLabel(self.frame_23)
        self.reg_sharpness_value.setObjectName(u"reg_sharpness_value")
        self.reg_sharpness_value.setFont(font4)
        self.reg_sharpness_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.reg_sharpness_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.reg_sharpness_value, 2, 2, 1, 1)

        self.label_8 = QLabel(self.frame_23)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)

        self.reg_contrast_slider = QSlider(self.frame_23)
        self.reg_contrast_slider.setObjectName(u"reg_contrast_slider")
        self.reg_contrast_slider.setMinimumSize(QSize(240, 0))
        self.reg_contrast_slider.setMaximumSize(QSize(240, 16777215))
        self.reg_contrast_slider.setValue(60)
        self.reg_contrast_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.reg_contrast_slider, 3, 1, 1, 1)

        self.reg_contrast_value = QLabel(self.frame_23)
        self.reg_contrast_value.setObjectName(u"reg_contrast_value")
        self.reg_contrast_value.setFont(font4)
        self.reg_contrast_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.reg_contrast_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.reg_contrast_value, 3, 2, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_23)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 250))
        self.frame_10.setMaximumSize(QSize(16777215, 250))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, -1, 0, 0)
        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(379, 240))
        self.frame_21.setMaximumSize(QSize(379, 240))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, 9, -1)
        self.change_date_box = QRadioButton(self.frame_21)
        self.change_date_box.setObjectName(u"change_date_box")
        self.change_date_box.setMinimumSize(QSize(0, 25))
        self.change_date_box.setMaximumSize(QSize(16777215, 20))
        self.change_date_box.setFont(font4)
        self.change_date_box.setStyleSheet(u"color: rgb(255,255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"padding-left:5px;\n"
"border-radius:7px;")
        self.change_date_box.setIcon(icon11)

        self.verticalLayout_21.addWidget(self.change_date_box)

        self.calendarWidget_reg = QCalendarWidget(self.frame_21)
        self.calendarWidget_reg.setObjectName(u"calendarWidget_reg")
        self.calendarWidget_reg.setGridVisible(False)
        self.calendarWidget_reg.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_reg.setNavigationBarVisible(True)

        self.verticalLayout_21.addWidget(self.calendarWidget_reg)


        self.gridLayout_3.addWidget(self.frame_21, 1, 1, 1, 1)

        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(370, 240))
        self.frame_20.setMaximumSize(QSize(370, 240))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.email_from = QLineEdit(self.frame_20)
        self.email_from.setObjectName(u"email_from")
        self.email_from.setGeometry(QRect(20, 40, 332, 41))
        self.email_from.setMinimumSize(QSize(332, 0))
        self.email_from.setMaximumSize(QSize(332, 16777215))
        self.email_from.setFont(font4)
        self.email_from.setStyleSheet(u"QLineEdit{\n"
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
        self.email_from.setClearButtonEnabled(True)
        self.email_sender = QLineEdit(self.frame_20)
        self.email_sender.setObjectName(u"email_sender")
        self.email_sender.setGeometry(QRect(20, 140, 332, 41))
        self.email_sender.setMinimumSize(QSize(332, 0))
        self.email_sender.setMaximumSize(QSize(332, 16777215))
        self.email_sender.setFont(font4)
        self.email_sender.setStyleSheet(u"QLineEdit{\n"
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
        self.email_sender.setClearButtonEnabled(True)
        self.sender_password = QLineEdit(self.frame_20)
        self.sender_password.setObjectName(u"sender_password")
        self.sender_password.setGeometry(QRect(20, 190, 332, 41))
        self.sender_password.setMinimumSize(QSize(332, 0))
        self.sender_password.setMaximumSize(QSize(332, 16777215))
        self.sender_password.setFont(font4)
        self.sender_password.setStyleSheet(u"QLineEdit{\n"
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
        self.sender_password.setEchoMode(QLineEdit.Password)
        self.sender_password.setClearButtonEnabled(True)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 111, 20))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email_subject = QLineEdit(self.frame_20)
        self.email_subject.setObjectName(u"email_subject")
        self.email_subject.setGeometry(QRect(20, 90, 332, 41))
        self.email_subject.setMinimumSize(QSize(332, 0))
        self.email_subject.setMaximumSize(QSize(332, 16777215))
        self.email_subject.setFont(font4)
        self.email_subject.setStyleSheet(u"QLineEdit{\n"
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
        self.email_subject.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.frame_20, 1, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_10)


        self.verticalLayout_15.addWidget(self.frame_11)


        self.horizontalLayout_14.addWidget(self.right_frame_reg)

        self.stackedWidget.addWidget(self.database)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_13 = QVBoxLayout(self.report)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 12, 0)
        self.frame_7 = QFrame(self.report)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 650))
        self.frame_7.setMaximumSize(QSize(16777215, 650))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, 0, 0)
        self.plot_area = QLabel(self.frame_7)
        self.plot_area.setObjectName(u"plot_area")
        self.plot_area.setMinimumSize(QSize(699, 632))
        self.plot_area.setMaximumSize(QSize(699, 632))
        self.plot_area.setFont(font6)
        self.plot_area.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.plot_area.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.plot_area)

        self.plot_area_2 = QLabel(self.frame_7)
        self.plot_area_2.setObjectName(u"plot_area_2")
        self.plot_area_2.setMinimumSize(QSize(710, 632))
        self.plot_area_2.setMaximumSize(QSize(698, 632))
        self.plot_area_2.setFont(font6)
        self.plot_area_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.plot_area_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.plot_area_2)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.report)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, 0, -1)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 20, 361, 241))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.calendarWidget_report = QCalendarWidget(self.frame_12)
        self.calendarWidget_report.setObjectName(u"calendarWidget_report")
        self.calendarWidget_report.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_report.setNavigationBarVisible(True)

        self.verticalLayout_16.addWidget(self.calendarWidget_report)

        self.report_start_date = QLineEdit(self.frame_9)
        self.report_start_date.setObjectName(u"report_start_date")
        self.report_start_date.setGeometry(QRect(760, 20, 181, 51))
        self.report_start_date.setFont(font4)
        self.report_start_date.setStyleSheet(u"QLineEdit{\n"
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
        self.report_start_date.setClearButtonEnabled(True)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(770, 30, 31, 31))
        self.label_23.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_23.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.report_end_date = QLineEdit(self.frame_9)
        self.report_end_date.setObjectName(u"report_end_date")
        self.report_end_date.setGeometry(QRect(970, 20, 201, 51))
        self.report_end_date.setFont(font4)
        self.report_end_date.setStyleSheet(u"QLineEdit{\n"
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
        self.report_end_date.setClearButtonEnabled(True)
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(980, 30, 31, 31))
        self.label_24.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_24.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.file_name = QLineEdit(self.frame_9)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(1200, 20, 211, 51))
        self.file_name.setFont(font4)
        self.file_name.setStyleSheet(u"QLineEdit{\n"
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
        self.file_name.setClearButtonEnabled(True)
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(1210, 30, 31, 31))
        self.label_20.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_20.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.btn_load = QPushButton(self.frame_9)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(760, 220, 141, 45))
        self.btn_load.setMinimumSize(QSize(0, 45))
        self.btn_load.setMaximumSize(QSize(16777215, 45))
        self.btn_load.setFont(font4)
        self.btn_load.setStyleSheet(u"QPushButton{\n"
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
        icon20 = QIcon()
        icon20.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load.setIcon(icon20)
        self.btn_load.setIconSize(QSize(30, 30))
        self.btn_load.setFlat(True)
        self.btn_save = QPushButton(self.frame_9)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(930, 220, 141, 45))
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setMaximumSize(QSize(16777215, 45))
        self.btn_save.setFont(font4)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
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
        icon21 = QIcon()
        icon21.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon21)
        self.btn_save.setIconSize(QSize(30, 30))
        self.btn_save.setFlat(True)
        self.btn_refresh = QPushButton(self.frame_9)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(1100, 220, 141, 45))
        self.btn_refresh.setMinimumSize(QSize(0, 45))
        self.btn_refresh.setMaximumSize(QSize(16777215, 45))
        self.btn_refresh.setFont(font4)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
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
        icon22 = QIcon()
        icon22.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon22)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.btn_remove_combox_item = QPushButton(self.frame_9)
        self.btn_remove_combox_item.setObjectName(u"btn_remove_combox_item")
        self.btn_remove_combox_item.setGeometry(QRect(1270, 220, 141, 45))
        self.btn_remove_combox_item.setMinimumSize(QSize(0, 45))
        self.btn_remove_combox_item.setMaximumSize(QSize(16777215, 45))
        self.btn_remove_combox_item.setFont(font4)
        self.btn_remove_combox_item.setStyleSheet(u"QPushButton{\n"
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
        icon23 = QIcon()
        icon23.addFile(u":/icons/asset/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_combox_item.setIcon(icon23)
        self.btn_remove_combox_item.setIconSize(QSize(30, 30))
        self.btn_remove_combox_item.setFlat(True)
        self.college_comboBox = QComboBox(self.frame_9)
        self.college_comboBox.setObjectName(u"college_comboBox")
        self.college_comboBox.setGeometry(QRect(760, 90, 131, 50))
        self.college_comboBox.setMinimumSize(QSize(0, 50))
        self.college_comboBox.setMaximumSize(QSize(16777215, 50))
        self.college_comboBox.setFont(font4)
        self.college_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.college_comboBox.setFrame(False)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(380, 20, 361, 241))
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.calendarWidget_report_2 = QCalendarWidget(self.frame_14)
        self.calendarWidget_report_2.setObjectName(u"calendarWidget_report_2")
        self.calendarWidget_report_2.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_report_2.setNavigationBarVisible(True)

        self.verticalLayout_19.addWidget(self.calendarWidget_report_2)

        self.college_courses = QComboBox(self.frame_9)
        self.college_courses.setObjectName(u"college_courses")
        self.college_courses.setGeometry(QRect(900, 90, 291, 50))
        self.college_courses.setMinimumSize(QSize(0, 50))
        self.college_courses.setMaximumSize(QSize(16777215, 50))
        self.college_courses.setFont(font4)
        self.college_courses.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.college_courses.setFrame(False)
        self.frame_18 = QFrame(self.frame_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(760, 160, 651, 41))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pie_chart = QRadioButton(self.frame_18)
        self.pie_chart.setObjectName(u"pie_chart")
        self.pie_chart.setFont(font6)
        self.pie_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pie_chart.setChecked(False)

        self.horizontalLayout_16.addWidget(self.pie_chart)

        self.bar_chart = QRadioButton(self.frame_18)
        self.bar_chart.setObjectName(u"bar_chart")
        self.bar_chart.setFont(font6)
        self.bar_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.bar_chart.setChecked(True)

        self.horizontalLayout_16.addWidget(self.bar_chart)

        self.line_graph = QRadioButton(self.frame_18)
        self.line_graph.setObjectName(u"line_graph")
        self.line_graph.setFont(font6)
        self.line_graph.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_16.addWidget(self.line_graph)

        self.date_range_comboBox = QComboBox(self.frame_9)
        self.date_range_comboBox.setObjectName(u"date_range_comboBox")
        self.date_range_comboBox.setGeometry(QRect(1200, 90, 211, 50))
        self.date_range_comboBox.setMinimumSize(QSize(0, 50))
        self.date_range_comboBox.setMaximumSize(QSize(16777215, 50))
        self.date_range_comboBox.setFont(font4)
        self.date_range_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.date_range_comboBox.setEditable(False)
        self.date_range_comboBox.setFrame(False)

        self.verticalLayout_14.addWidget(self.frame_9)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.report)
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.horizontalLayout_12 = QHBoxLayout(self.settings)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.settings)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(710, 0))
        self.frame_19.setMaximumSize(QSize(710, 16777215))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_19)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.frame_26 = QFrame(self.frame_19)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(700, 0))
        self.frame_26.setMaximumSize(QSize(695, 16777215))
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_15.setSpacing(9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 12, -1)
        self.textEdit = QTextEdit(self.frame_26)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(685, 0))
        self.textEdit.setMaximumSize(QSize(680, 16777215))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"}")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.textEdit)


        self.verticalLayout_4.addWidget(self.frame_26)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.frame_25 = QFrame(self.settings)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, -1, 0, -1)
        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(720, 16777215))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.textEdit_2 = QTextEdit(self.frame_28)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(700, 0))
        self.textEdit_2.setMaximumSize(QSize(680, 16777215))
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"}")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.textEdit_2)


        self.verticalLayout_25.addWidget(self.frame_28)


        self.horizontalLayout_12.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)

        self.btn_backup = QPushButton(self.centralwidget)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setGeometry(QRect(0, 830, 70, 70))
        self.btn_backup.setMinimumSize(QSize(0, 70))
        self.btn_backup.setMaximumSize(QSize(16777215, 70))
        self.btn_backup.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        self.btn_backup.setIcon(icon10)
        self.btn_backup.setIconSize(QSize(40, 40))
        self.btn_backup.setFlat(True)
        dashboard.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("dashboard", u"iAttend", None))
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_database.setText("")
        self.btn_search.setText("")
        self.btn_batch.setText("")
        self.btn_camera.setText("")
        self.btn_report.setText("")
        self.btn_mail_report_or_data.setText("")
        self.btn_help.setText("")
        self.image.setText("")
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.coledge.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.program.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.last_out.setText(QCoreApplication.translate("dashboard", u"Last seen", None))
        self.image_2.setText("")
        self.last_in.setText(QCoreApplication.translate("dashboard", u"Duration", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.label_27.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Entry camera", None))
        self.firstname_24.setText("")
        self.btn_open_exit_camera_ui.setText(QCoreApplication.translate("dashboard", u"Check Out", None))
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_open_database.setText(QCoreApplication.translate("dashboard", u"Check In", None))
        self.camera_view.setText("")
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Image Enhancement", None))
        self.brightness_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.brightness_label.setText(QCoreApplication.translate("dashboard", u"Brigthness", None))
        self.sharp_label.setText(QCoreApplication.translate("dashboard", u"Sharpness", None))
        self.sharp_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.contrast_label.setText(QCoreApplication.translate("dashboard", u"Contrast", None))
        self.contrast_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Camera Scan", None))
        self.scan_range_label.setText("")
        self.label_42.setText("")
        self.btn_scan_range.setText(QCoreApplication.translate("dashboard", u"Scan", None))
        self.scan_range.setPlaceholderText(QCoreApplication.translate("dashboard", u"Scan range ?", None))
        self.db_validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.db_refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.db_year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.db_nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.db_image_data.setText("")
        self.db_lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.db_programe.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.db_college.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_29.setText("")
        self.image_3.setText("")
        self.start_date.setText(QCoreApplication.translate("dashboard", u"Switch  Between Date Fields", None))
        self.db_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.db_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_25.setText("")
        self.label_30.setText("")
        self.btn_reload.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_csv.setText(QCoreApplication.translate("dashboard", u"CSV", None))
        self.label_26.setText("")
        self.label_40.setText("")
        self.checkBox.setText(QCoreApplication.translate("dashboard", u"Search by program", None))
        self.btn_json.setText(QCoreApplication.translate("dashboard", u"JSON", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Time In", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Time Out", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Duration", None));
        self.label_45.setText("")
        self.batch_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_batch_browse.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.batch_browse.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_start_job.setText(QCoreApplication.translate("dashboard", u"Insert", None))
        self.btn_batch_mail.setText(QCoreApplication.translate("dashboard", u"Mail", None))
        self.btn_batch_folder.setText(QCoreApplication.translate("dashboard", u"Images", None))
        self.btn_batch_images.setText(QCoreApplication.translate("dashboard", u"Insert", None))
        ___qtablewidgetitem6 = self.tableWidget_batch.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem7 = self.tableWidget_batch.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("dashboard", u"Index", None));
        ___qtablewidgetitem8 = self.tableWidget_batch.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem9 = self.tableWidget_batch.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem10 = self.tableWidget_batch.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("dashboard", u"College", None));
        ___qtablewidgetitem11 = self.tableWidget_batch.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("dashboard", u"Naionality", None));
        ___qtablewidgetitem12 = self.tableWidget_batch.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("dashboard", u"Validity", None));
        ___qtablewidgetitem13 = self.tableWidget_batch.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("dashboard", u"E-mail", None));
        self.firstname_25.setText(QCoreApplication.translate("dashboard", u"Camera one", None))
        self.btn_camera_one_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_camera_one_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_one_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.label_31.setText("")
        self.btn_camera_two_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_two_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_two_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_26.setText(QCoreApplication.translate("dashboard", u"Camera two", None))
        self.label_32.setText("")
        self.btn_camera_three_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_three_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_three_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_27.setText(QCoreApplication.translate("dashboard", u"Camera three", None))
        self.label_33.setText("")
        self.btn_camera_four_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_four_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_four_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_28.setText(QCoreApplication.translate("dashboard", u"Camera four", None))
        self.label_34.setText("")
        self.btn_cast_cam_one.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.btn_cast_cam_one_2.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.btn_cast_cam_three.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.btn_cast_cam_four.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.camera_1.setText("")
        self.camera_2.setText("")
        self.camera_3.setText("")
        self.camera_4.setText("")
        self.reg_image.setText("")
        self.reg_firstname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.reg_image_2.setText("")
        self.reg_middlename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.reg_lastname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reg_index.setPlaceholderText(QCoreApplication.translate("dashboard", u"Index", None))
        self.reg_college.setPlaceholderText(QCoreApplication.translate("dashboard", u"College", None))
        self.reg_student_ref.setPlaceholderText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.reg_nationality.setPlaceholderText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.reg_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date", None))
        self.reg_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date", None))
        self.label_35.setText("")
        self.btn_search_reg.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_37.setText("")
        self.search_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.label_38.setText("")
        self.btn_register.setText(QCoreApplication.translate("dashboard", u"Register", None))
        self.btn_update.setText(QCoreApplication.translate("dashboard", u"Update", None))
        self.btn_remove.setText(QCoreApplication.translate("dashboard", u"Remove", None))
        self.btn_clear.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.label_39.setText(QCoreApplication.translate("dashboard", u"Image file", None))
        self.image_file_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.btn_browse_reg.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.label_36.setText("")
        self.file_system.setText(QCoreApplication.translate("dashboard", u"System", None))
        self.online_image.setText(QCoreApplication.translate("dashboard", u"Online", None))
        self.reg_email.setPlaceholderText(QCoreApplication.translate("dashboard", u"Email", None))
        self.label_43.setText("")
        self.label_44.setText("")
        self.btn_send_mail.setText(QCoreApplication.translate("dashboard", u"Send mail", None))
        self.image_less.setText(QCoreApplication.translate("dashboard", u"Image-less", None))
        self.reg_cap_frame.setText("")
        self.btn_camera_reg_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_camera_reg_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.reg_camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.label_41.setText("")
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Image Enhacement", None))
        self.label_3.setText(QCoreApplication.translate("dashboard", u"Brightness", None))
        self.reg_bright_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_5.setText(QCoreApplication.translate("dashboard", u"Sharpness", None))
        self.reg_sharpness_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_8.setText(QCoreApplication.translate("dashboard", u"Contrast", None))
        self.reg_contrast_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.change_date_box.setText(QCoreApplication.translate("dashboard", u"Switch  Between Date Fields", None))
        self.email_from.setPlaceholderText(QCoreApplication.translate("dashboard", u"From", None))
        self.email_sender.setPlaceholderText(QCoreApplication.translate("dashboard", u"Email", None))
        self.sender_password.setPlaceholderText(QCoreApplication.translate("dashboard", u"Password", None))
        self.label_9.setText(QCoreApplication.translate("dashboard", u"Sender details", None))
        self.email_subject.setPlaceholderText(QCoreApplication.translate("dashboard", u"Subject", None))
        self.plot_area.setText(QCoreApplication.translate("dashboard", u"Graph", None))
        self.plot_area_2.setText(QCoreApplication.translate("dashboard", u"Graph", None))
        self.report_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.label_23.setText("")
        self.report_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_24.setText("")
        self.file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.label_20.setText("")
        self.btn_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.btn_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Reload", None))
        self.btn_remove_combox_item.setText(QCoreApplication.translate("dashboard", u"Date", None))
        self.pie_chart.setText(QCoreApplication.translate("dashboard", u"Piechart", None))
        self.bar_chart.setText(QCoreApplication.translate("dashboard", u"Barchart", None))
        self.line_graph.setText(QCoreApplication.translate("dashboard", u"Line graph", None))
        self.textEdit.setHtml(QCoreApplication.translate("dashboard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Getting Started</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">This page seeks to introduce the user on how to use most components of this software and how to get some of the various components working since it tend to give the end user more flexibility due to it loose coupling nature. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Camera</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The system by default is not configured to run on any camera whether inbuilt or online camera. You would need to scan for all available camera's connected to the system. This can be achieved by providing a number for the range of camera's you want to scan for and pressing the scan button provided. The software would only return list of available open camera's connected to the system. It also gives you the flexibility to connect to networked cameras. In other to achieve this, you need to provide the Ip address of the camera on the network.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-se"
                        "rif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Camera Connection</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">In other to connect any of the active camera's, first you need to make sure that the camera is not in use or if in use </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">make sure to disconnect</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> it before connecting it to different view or frame.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">e.g.,</span><span style=\" font-famil"
                        "y:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> if camera 0 is connected to </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">check in</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> view and you try to connect that same camera to </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">check out</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> view then, the system would automatically release the camera for </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">check out</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> view to use. This behavior is been utilized throughout the system design.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Image Enhancement</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The system provides some image enhancement capabilities to process the image based on weather conditions. It currently provides full support for increasing. This would only work for camera's that supports these features. Some camera's do not give support fine tuning these features.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1] Brightness	 [2] Sharpness 	[3] Contrast</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Surveillance</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The system supports four additional cameras to help monitor the surroundings as well. To use this either provide </span><span st"
                        "yle=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">camera IP</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> address or if is attached to system provide the </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">camera Id</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> in order to establish connection. If the default view provided is small and you would have a larger view then you can use the cast feature to open a wider screen and connect to such camera. The normal view doesn't support image enhancement but you can use this feature when you cast it to a wider screen. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Databases</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The system currently is providing full support for three (3) databases. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1] SQLite	 [2] MySQL	 [3] PostgreSQL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">By default, the system is configured to run on embedded database (SQLite) and you don't need to provide any connection details. If you desire to configure the system to run on either </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">MySQL or PostgreSQL</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> then you would need to provide your connection details and would also need to test the connection status to check whether you have a working connection or not. You don't need create the database tables as the system is able to detect and create the tables it needs in other to function. This is achieved by using the </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">initialize tables button</span><span style=\" font-family:'MS Sh"
                        "ell Dlg 2','sans-serif'; font-size:11pt;\">. This should be done once.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Database properties</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">To prevent you from re-typing the database properties (MySQL or PostgreSQL) all the time attached to the application is</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-"
                        "size:11pt; font-weight:600; font-style:italic;\"> properties.txt</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> file where you can provide the database connection details to save you time. Anytime you load the application, these properties are also loaded. Please follow the format as seen in the text file or below is an example:</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\"> </span><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Username, Password, Hostname, Port, Database</span><span style=\" font-size:11pt;\"> this</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> file located in the </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span"
                        " style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\database_properties</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> directory.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Backup</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">To backup create backup whe"
                        "n the embedded database is used as main data source. Head to the advanced search page and use the backup button provided to back the database up. The backup location for the backup is in</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\"> C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\backup</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> directory.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Searching</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">In other to retrieve student details along with all the entries made by that student, they are various combinations or criteria\u2019s you can use to achieve this and get results. When the switch date between date fields is checked the date picked from the calendar widget would be placed in the start date field and if unchecked then it would be placed in the end date field.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1]. If the search box is empty and the search button is pressed then it's going to fetch all the records present in the database table and render it inside the table view.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[2]. If a reference number is provided then it's going to fetch that student details along with all the entries made by that student. The student details would be rendered on a card-view liked UI and the entries would also be rendered in"
                        " a table view.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[3]. If a reference number is provided as well as start date then it would fetch all entries from that date down to the last appeared date and render the data to the UI.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'"
                        "; font-size:11pt;\">[4] if a reference number is provided as well as start and end date then it would fetch the details from based on the date range provided and render the data to UI.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[5]. If the search by program box is checked then you can fetch data based on the various programs. The search comes with autocompletion feature with the programs available.</span><span style=\" font-size:11pt;\"> </span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("dashboard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">\u00a0</span><span style=\" font-size:11pt;\"> </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Exporting Data</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The sys"
                        "tem provides two solid ways of exporting data in either Json or CVS format based on your need. Data can only be exported when the table view is not empty or data is not been rendered. The default naming format is student_data_[date]_[time]. Where the date and time is the date and time stamp of the day the file was exported.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1]. When data is exported in csv format the default location for the saved file is at </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; fon"
                        "t-style:italic;\">\\data\\csv_export</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[2]. When data is exported in Json format the default location for the saved file is at </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\json_export</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-ser"
                        "if'; font-size:11pt; font-weight:600; text-decoration: underline;\">Reports</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The system provides support for generating reports in three different ways based on the user\u2019s preference. By default, the application won\u2019t display any report data unless it is hot reloaded. On hot reload, it is going to display pie chart and any other type of chart or graph based on the one which is checked. The pie chart side of this view is only used to render only pie charts. The other view is dynamic and hence display plots for either bar chart or line graph.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell "
                        "Dlg 2','sans-serif'; font-size:11pt;\">[1] Pie chart\u00a0\u00a0\u00a0 [2] Bar chart\u00a0 [3] Line graph</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Generating charts</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">This case applies to pie chart and bar chart</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','s"
                        "ans-serif'; font-size:11pt;\">In other to retrieve data for analysis, these are various combinations or criteria\u2019s you can use to achieve this and get results.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1]. If either of these radio buttons is checked with start date provided and load button is pressed, then it is going to read all the data available based on such date, from the database and display a chart with such data.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[2]. If either of these radio buttons is checked with start and end date provided and load button is pressed, then it is going t"
                        "o read all the data available based on the dates provided, from the database and display a chart with such data.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Line Graph</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The line graph/plot is only used to visualize trends in data. To be able to plot trends in data. There is an additional combo box provided to keep all the dates been selected for the line graph. Only dates from the first calendar would be added to list.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-to"
                        "p:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1]. First you would to select the program to plot or visualize their trend.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[2]. Pick dates from the first calendar and it would automatically be added to the combo box available.</span><span style=\" font-size:11pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[3]. To remove any unwanted date from the list of dates to be used, select that date and use the </span><span style=\" font-family:'MS Shell Dlg 2','sans-seri"
                        "f'; font-size:11pt; font-weight:600;\">date button</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> to remove it.</span><span style=\" font-size:11pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[4]. After all the dates for the line graphs are selected, pressed the load button to plot the graph.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">Saving Charts</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The only support provided for saving files is pdf format and this can't be set from the user end as it is provided from the application end. The saving format is as follows, the </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">filename</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> provided appended with this </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">[date]_[time]</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> where date and time is the current values on the machine running the application.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[1]. If you want to save pie c"
                        "harts, make sure that radio button checked and provide a filename, the saved file would be found in this directory. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\piechart</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[2]. If you want to save bar charts, make sure that radio button checked and provide a filename, the saved file would be found in "
                        "this directory. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\barchart</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">[3]. If you want to save line graph, make sure that radio button checked and provide a filename, the saved file would be found in this directory.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p style=\" margin-top:12px;"
                        " margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\linechart</span><span style=\" font-size:11pt;\"> </span><span style=\" font-family:'Times New Roman','serif'; font-size:11pt;\">\u00a0</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; text-decoration: underline;\">E-mail properties</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style"
                        "=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The properties of the sender details can be place in a text file located within the directory below with the name </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">detail.txt</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\email_details</sp"
                        "an><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> to prevent you from re-writing them anytime you want to send e-mail. The application on start-up would automatically search for the file and load details from there. Please follow the exact format provided in the file.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">The content of your mail can be typed in the content.txt located in the same directory. This content is attached mails sent as attendance code. To send reports or data from the content_report.txt should be edited as per your need or requirement.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">Please take note the '</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">Hello name,</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">' section, you can change the 'Hello' but please keep the name as it is since the name part would be provided from the user interface end.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\">To prevent you from re-typing the e-mails all the time attached to the application is </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">detail.txt</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> file where you c"
                        "an provide the mail details to save you time. Anytime you load the application, these properties are also loaded. Please follow the format as seen in the text file or below is an example: </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">subject, example@gmail.com, sender name, password,</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> this file located in the </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\email_details</span><span"
                        " style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> directory.</span><span style=\" font-size:11pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">College programs</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">To it make easier to added new programs to the existing ones been offered by the college in the near future, the application provides a way to handle this situation. You just need to edit the </span><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">CoS_programs.txt</span><span style=\" font-size:11pt;\"> file  located in the </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\""
                        ">C:\\ProgramData\\</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:600; font-style:italic;\">iAttend</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\">\\data\\programs </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt;\"> directory. Any new program added should be seperated by a comma to allow the application read it. </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\"> </span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600;\">e.g.,</span><span style=\" font-family:'MS Shell Dlg 2','sans-serif'; font-size:11pt; font-weight:600; font-style:italic;\"> BSc. Chemistry, BSc. Physics, new program,new program</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size"
                        ":8pt;\"><br /></p></body></html>", None))
        self.btn_backup.setText("")
    # retranslateUi

