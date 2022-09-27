# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardrKibWn.ui'
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

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1280, 820)
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 820))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.logo.setMaximumSize(QSize(100, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)

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
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(40, 40))
        self.btn_search.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_search)

        self.btn_camera = QPushButton(self.frame)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(0, 70))
        self.btn_camera.setMaximumSize(QSize(16777215, 70))
        self.btn_camera.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon2)
        self.btn_camera.setIconSize(QSize(40, 40))
        self.btn_camera.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_camera)

        self.btn_database = QPushButton(self.frame)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setMinimumSize(QSize(0, 70))
        self.btn_database.setMaximumSize(QSize(16777215, 70))
        self.btn_database.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon3)
        self.btn_database.setIconSize(QSize(40, 40))
        self.btn_database.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_database)

        self.btn_report = QPushButton(self.frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(0, 70))
        self.btn_report.setMaximumSize(QSize(16777215, 70))
        self.btn_report.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon4)
        self.btn_report.setIconSize(QSize(40, 40))
        self.btn_report.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_report)

        self.btn_settings = QPushButton(self.frame)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 70))
        self.btn_settings.setMaximumSize(QSize(16777215, 70))
        self.btn_settings.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QSize(40, 40))
        self.btn_settings.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.label_4 = QLabel(self.search)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 310, 251, 141))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.search)
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.label_5 = QLabel(self.camera)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(530, 330, 251, 141))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.camera)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.label_6 = QLabel(self.database)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(560, 340, 251, 141))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.database)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.label_2 = QLabel(self.report)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 310, 251, 141))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.report)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_7 = QLabel(self.settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 300, 251, 141))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settings)
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
        self.info_frame.setMinimumSize(QSize(0, 500))
        self.info_frame.setMaximumSize(QSize(16777215, 600))
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 261, 291))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 20, 201, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.firstname.setFont(font3)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.firstname.setAlignment(Qt.AlignCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(290, 70, 201, 41))
        self.middlename.setFont(font3)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.middlename.setAlignment(Qt.AlignCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 120, 201, 41))
        self.lastname.setFont(font3)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.lastname.setAlignment(Qt.AlignCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(290, 170, 201, 41))
        self.refrence.setFont(font3)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.refrence.setAlignment(Qt.AlignCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(290, 220, 201, 41))
        self.index.setFont(font3)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.index.setAlignment(Qt.AlignCenter)
        self.coledge = QLabel(self.info_frame)
        self.coledge.setObjectName(u"coledge")
        self.coledge.setGeometry(QRect(290, 270, 201, 41))
        self.coledge.setFont(font3)
        self.coledge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.coledge.setAlignment(Qt.AlignCenter)
        self.validy = QLabel(self.info_frame)
        self.validy.setObjectName(u"validy")
        self.validy.setGeometry(QRect(20, 320, 261, 41))
        self.validy.setFont(font3)
        self.validy.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.validy.setAlignment(Qt.AlignCenter)
        self.nationality = QLabel(self.info_frame)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setGeometry(QRect(290, 320, 201, 41))
        self.nationality.setFont(font3)
        self.nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.info_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 440, 231, 41))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.info_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 370, 151, 41))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.info_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 370, 311, 41))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.info_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 440, 231, 41))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 500))
        self.camera_frame.setMaximumSize(QSize(16777215, 500))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 480))
        self.camera_view.setMaximumSize(QSize(16777215, 480))
        self.camera_view.setFont(font2)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.dilation = QSlider(self.properties_frame)
        self.dilation.setObjectName(u"dilation")
        self.dilation.setGeometry(QRect(10, 20, 311, 22))
        self.dilation.setMaximum(500)
        self.dilation.setOrientation(Qt.Horizontal)
        self.erosion = QSlider(self.properties_frame)
        self.erosion.setObjectName(u"erosion")
        self.erosion.setGeometry(QRect(10, 80, 311, 22))
        self.erosion.setMaximum(500)
        self.erosion.setOrientation(Qt.Horizontal)
        self.blur = QSlider(self.properties_frame)
        self.blur.setObjectName(u"blur")
        self.blur.setGeometry(QRect(10, 140, 311, 22))
        self.blur.setMaximum(500)
        self.blur.setOrientation(Qt.Horizontal)
        self.horizontalSlider_4 = QSlider(self.properties_frame)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setGeometry(QRect(10, 200, 311, 22))
        self.horizontalSlider_4.setMaximum(500)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5 = QSlider(self.properties_frame)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setGeometry(QRect(370, 80, 331, 22))
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6 = QSlider(self.properties_frame)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setGeometry(QRect(370, 200, 331, 22))
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_7 = QSlider(self.properties_frame)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setGeometry(QRect(370, 140, 331, 22))
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)
        self.horizontalSlider_8 = QSlider(self.properties_frame)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        self.horizontalSlider_8.setGeometry(QRect(370, 20, 331, 22))
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)
        self.nationality_2 = QLabel(self.properties_frame)
        self.nationality_2.setObjectName(u"nationality_2")
        self.nationality_2.setGeometry(QRect(110, 40, 91, 21))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setWeight(50)
        self.nationality_2.setFont(font4)
        self.nationality_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_2.setAlignment(Qt.AlignCenter)
        self.nationality_3 = QLabel(self.properties_frame)
        self.nationality_3.setObjectName(u"nationality_3")
        self.nationality_3.setGeometry(QRect(110, 100, 91, 21))
        self.nationality_3.setFont(font4)
        self.nationality_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_3.setAlignment(Qt.AlignCenter)
        self.nationality_4 = QLabel(self.properties_frame)
        self.nationality_4.setObjectName(u"nationality_4")
        self.nationality_4.setGeometry(QRect(100, 160, 91, 21))
        self.nationality_4.setFont(font4)
        self.nationality_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_4.setAlignment(Qt.AlignCenter)
        self.nationality_5 = QLabel(self.properties_frame)
        self.nationality_5.setObjectName(u"nationality_5")
        self.nationality_5.setGeometry(QRect(100, 220, 91, 21))
        self.nationality_5.setFont(font4)
        self.nationality_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_5.setAlignment(Qt.AlignCenter)
        self.nationality_6 = QLabel(self.properties_frame)
        self.nationality_6.setObjectName(u"nationality_6")
        self.nationality_6.setGeometry(QRect(480, 100, 91, 21))
        self.nationality_6.setFont(font4)
        self.nationality_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_6.setAlignment(Qt.AlignCenter)
        self.nationality_7 = QLabel(self.properties_frame)
        self.nationality_7.setObjectName(u"nationality_7")
        self.nationality_7.setGeometry(QRect(480, 40, 91, 21))
        self.nationality_7.setFont(font4)
        self.nationality_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_7.setAlignment(Qt.AlignCenter)
        self.nationality_8 = QLabel(self.properties_frame)
        self.nationality_8.setObjectName(u"nationality_8")
        self.nationality_8.setGeometry(QRect(470, 220, 91, 21))
        self.nationality_8.setFont(font4)
        self.nationality_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_8.setAlignment(Qt.AlignCenter)
        self.nationality_9 = QLabel(self.properties_frame)
        self.nationality_9.setObjectName(u"nationality_9")
        self.nationality_9.setGeometry(QRect(470, 160, 91, 21))
        self.nationality_9.setFont(font4)
        self.nationality_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.nationality_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)


        self.verticalLayout.addWidget(self.drop_shadow_layout)

        dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"iVision", None))
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_search.setText("")
        self.btn_camera.setText("")
        self.btn_database.setText("")
        self.btn_report.setText("")
        self.btn_settings.setText("")
        self.label_4.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_5.setText(QCoreApplication.translate("dashboard", u"Camera", None))
        self.label_6.setText(QCoreApplication.translate("dashboard", u"Database", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Report", None))
        self.label_7.setText(QCoreApplication.translate("dashboard", u"Settings", None))
        self.image.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lasttname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Student No", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.coledge.setText(QCoreApplication.translate("dashboard", u"Colledge", None))
        self.validy.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.label_8.setText(QCoreApplication.translate("dashboard", u"Last In", None))
        self.label_10.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.label_11.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.label_9.setText(QCoreApplication.translate("dashboard", u"Last Out", None))
        self.camera_view.setText(QCoreApplication.translate("dashboard", u"Image", None))
#if QT_CONFIG(tooltip)
        self.dilation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.nationality_2.setText(QCoreApplication.translate("dashboard", u"Dilation", None))
        self.nationality_3.setText(QCoreApplication.translate("dashboard", u"Erosion", None))
        self.nationality_4.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.nationality_5.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.nationality_6.setText(QCoreApplication.translate("dashboard", u"Erosion", None))
        self.nationality_7.setText(QCoreApplication.translate("dashboard", u"Dilation", None))
        self.nationality_8.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.nationality_9.setText(QCoreApplication.translate("dashboard", u"Blur", None))
    # retranslateUi

