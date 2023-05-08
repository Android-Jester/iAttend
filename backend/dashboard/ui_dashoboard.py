# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardXfrGjZ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt,QDateTime,QDate,QTime)
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
        dashboard.resize(1520, 1029)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setGeometry(QRect(0, 0, 1540, 1030))
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
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
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
        self.horizontalLayout_19.setSpacing(9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.options)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(870, 0))
        self.label_4.setMaximumSize(QSize(900, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")

        self.horizontalLayout_19.addWidget(self.label_4)

        self.label_6 = QLabel(self.options)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(370, 34))
        self.label_6.setMaximumSize(QSize(350, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding-bottom:-5px;\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_6)

        self.btn_help_link = QPushButton(self.options)
        self.btn_help_link.setObjectName(u"btn_help_link")
        self.btn_help_link.setMinimumSize(QSize(40, 35))
        self.btn_help_link.setMaximumSize(QSize(50, 30))
        self.btn_help_link.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"    background-color: rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 16px;\n"
" background-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help_link.setIcon(icon)
        self.btn_help_link.setIconSize(QSize(30, 30))
        self.btn_help_link.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_help_link)

        self.btn_login_user = QPushButton(self.options)
        self.btn_login_user.setObjectName(u"btn_login_user")
        self.btn_login_user.setMinimumSize(QSize(40, 35))
        self.btn_login_user.setMaximumSize(QSize(50, 30))
        self.btn_login_user.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"    background-color: rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 16px;\n"
" background-color: rgb(45, 45, 45);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login_user.setIcon(icon1)
        self.btn_login_user.setIconSize(QSize(30, 30))
        self.btn_login_user.setFlat(True)

        self.horizontalLayout_19.addWidget(self.btn_login_user)


        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(80, 0))
        self.controls_frame.setMaximumSize(QSize(70, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.controls_frame)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_minimize = QPushButton(self.controls_frame)
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

        self.horizontalLayout_13.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.controls_frame)
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

        self.horizontalLayout_13.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.controls_frame)
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

        self.horizontalLayout_13.addWidget(self.btn_close)


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
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 4)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 630))
        self.frame.setMaximumSize(QSize(16777215, 600))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QSize(32, 40))
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
"\n"
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon3)
        self.btn_database.setIconSize(QSize(35, 45))
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
"}\n"
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon4)
        self.btn_search.setIconSize(QSize(35, 42))
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
"}\n"
"\n"
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch.setIcon(icon5)
        self.btn_batch.setIconSize(QSize(35, 40))
        self.btn_batch.setFlat(True)

        self.verticalLayout.addWidget(self.btn_batch)

        self.btn_sink_data = QPushButton(self.frame)
        self.btn_sink_data.setObjectName(u"btn_sink_data")
        self.btn_sink_data.setMinimumSize(QSize(0, 70))
        self.btn_sink_data.setMaximumSize(QSize(16777215, 70))
        self.btn_sink_data.setStyleSheet(u"QPushButton{\n"
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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sink_data.setIcon(icon6)
        self.btn_sink_data.setIconSize(QSize(32, 40))
        self.btn_sink_data.setFlat(True)

        self.verticalLayout.addWidget(self.btn_sink_data)

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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon7)
        self.btn_report.setIconSize(QSize(35, 43))
        self.btn_report.setFlat(True)

        self.verticalLayout.addWidget(self.btn_report)

        self.btn_consolidation_report = QPushButton(self.frame)
        self.btn_consolidation_report.setObjectName(u"btn_consolidation_report")
        self.btn_consolidation_report.setMinimumSize(QSize(0, 70))
        self.btn_consolidation_report.setMaximumSize(QSize(16777215, 70))
        self.btn_consolidation_report.setStyleSheet(u"QPushButton{\n"
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
"	border-left-color: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consolidation_report.setIcon(icon8)
        self.btn_consolidation_report.setIconSize(QSize(35, 40))
        self.btn_consolidation_report.setFlat(True)

        self.verticalLayout.addWidget(self.btn_consolidation_report)

        self.btn_admin = QPushButton(self.frame)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setMinimumSize(QSize(0, 70))
        self.btn_admin.setMaximumSize(QSize(16777215, 70))
        self.btn_admin.setStyleSheet(u"QPushButton{\n"
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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_admin.setIcon(icon9)
        self.btn_admin.setIconSize(QSize(35, 40))
        self.btn_admin.setFlat(True)

        self.verticalLayout.addWidget(self.btn_admin)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.btn_camera = QPushButton(self.menu_frame)
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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon10)
        self.btn_camera.setIconSize(QSize(35, 40))
        self.btn_camera.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_camera)

        self.btn_mail_report_or_data = QPushButton(self.menu_frame)
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
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mail_report_or_data.setIcon(icon11)
        self.btn_mail_report_or_data.setIconSize(QSize(32, 40))
        self.btn_mail_report_or_data.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_mail_report_or_data)

        self.btn_logout = QPushButton(self.menu_frame)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 70))
        self.btn_logout.setMaximumSize(QSize(16777215, 70))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"background-color: rgb(35, 35, 35);\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
" QPushButton:focus{\n"
"            color: rgb(255, 255, 255);\n"
"            border-left: 3px solid rgb(255, 255, 255);\n"
"            padding-left:5px;\n"
"  }\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon12)
        self.btn_logout.setIconSize(QSize(35, 40))
        self.btn_logout.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_logout)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 5, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setMaximumSize(QSize(1445, 980))
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
        self.info_frame.setMinimumSize(QSize(0, 560))
        self.info_frame.setMaximumSize(QSize(16777215, 570))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 30, 261, 291))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.image.setFont(font3)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.image.setScaledContents(False)
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 30, 191, 41))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.firstname.setFont(font4)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.othername = QLabel(self.info_frame)
        self.othername.setObjectName(u"othername")
        self.othername.setGeometry(QRect(290, 80, 191, 41))
        self.othername.setFont(font4)
        self.othername.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.othername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 130, 191, 41))
        self.lastname.setFont(font4)
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
        self.reference = QLabel(self.info_frame)
        self.reference.setObjectName(u"reference")
        self.reference.setGeometry(QRect(290, 180, 191, 41))
        self.reference.setFont(font4)
        self.reference.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.reference.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(290, 230, 191, 41))
        self.index.setFont(font4)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.college = QLabel(self.info_frame)
        self.college.setObjectName(u"college")
        self.college.setGeometry(QRect(290, 280, 191, 41))
        self.college.setFont(font4)
        self.college.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.college.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.validity = QLabel(self.info_frame)
        self.validity.setObjectName(u"validity")
        self.validity.setGeometry(QRect(20, 330, 261, 41))
        self.validity.setFont(font4)
        self.validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nationality = QLabel(self.info_frame)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setGeometry(QRect(20, 380, 261, 41))
        self.nationality.setFont(font4)
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
        self.year.setGeometry(QRect(390, 380, 91, 41))
        self.year.setFont(font4)
        self.year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.year.setAlignment(Qt.AlignCenter)
        self.last_out = QLabel(self.info_frame)
        self.last_out.setObjectName(u"last_out")
        self.last_out.setGeometry(QRect(110, 430, 261, 41))
        self.last_out.setFont(font4)
        self.last_out.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.last_out.setAlignment(Qt.AlignCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 10, 481, 541))
        self.image_2.setFont(font3)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.last_in = QLabel(self.info_frame)
        self.last_in.setObjectName(u"last_in")
        self.last_in.setGeometry(QRect(380, 430, 101, 41))
        self.last_in.setFont(font4)
        self.last_in.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.last_in.setAlignment(Qt.AlignCenter)
        self.program = QLabel(self.info_frame)
        self.program.setObjectName(u"program")
        self.program.setGeometry(QRect(20, 480, 461, 51))
        self.program.setFont(font4)
        self.program.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.program.setAlignment(Qt.AlignCenter)
        self.program.setWordWrap(True)
        self.gender = QLabel(self.info_frame)
        self.gender.setObjectName(u"gender")
        self.gender.setGeometry(QRect(290, 380, 91, 41))
        self.gender.setFont(font4)
        self.gender.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.gender.setAlignment(Qt.AlignCenter)
        self.type = QLabel(self.info_frame)
        self.type.setObjectName(u"type")
        self.type.setGeometry(QRect(290, 330, 191, 41))
        self.type.setFont(font4)
        self.type.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.type.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.faculty = QLabel(self.info_frame)
        self.faculty.setObjectName(u"faculty")
        self.faculty.setGeometry(QRect(20, 430, 81, 41))
        self.faculty.setFont(font4)
        self.faculty.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.faculty.setAlignment(Qt.AlignCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.othername.raise_()
        self.lastname.raise_()
        self.reference.raise_()
        self.index.raise_()
        self.college.raise_()
        self.validity.raise_()
        self.nationality.raise_()
        self.year.raise_()
        self.last_out.raise_()
        self.last_in.raise_()
        self.program.raise_()
        self.gender.raise_()
        self.type.raise_()
        self.faculty.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 420))
        self.frame_3.setMaximumSize(QSize(16777215, 400))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 300, 481, 100))
        self.label_notification.setMinimumSize(QSize(0, 100))
        self.label_notification.setMaximumSize(QSize(16777215, 100))
        self.label_notification.setFont(font4)
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
        self.camera_ip.setFont(font2)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.btn_connect_detect.setGeometry(QRect(20, 120, 171, 41))
        self.btn_connect_detect.setFont(font2)
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
        self.btn_connect_detect.setIcon(icon10)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, 60, 41, 31))
        self.label_27.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(210, 120, 171, 41))
        self.btn_disconnect.setFont(font2)
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
        icon13 = QIcon()
        icon13.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon13)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(400, 120, 81, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font2)
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
        self.firstname_24.setGeometry(QRect(10, 200, 481, 81))
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
        self.btn_open_exit_camera_ui.setGeometry(QRect(180, 220, 141, 41))
        self.btn_open_exit_camera_ui.setFont(font2)
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
        self.btn_open_exit_camera_ui.setIcon(icon10)
        self.btn_open_exit_camera_ui.setIconSize(QSize(30, 30))
        self.btn_open_exit_camera_ui.setFlat(True)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(340, 220, 141, 41))
        self.btn_clear_label.setFont(font2)
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
        icon14 = QIcon()
        icon14.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon14)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_open_database = QPushButton(self.frame_3)
        self.btn_open_database.setObjectName(u"btn_open_database")
        self.btn_open_database.setGeometry(QRect(20, 220, 141, 41))
        self.btn_open_database.setFont(font2)
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
        icon15 = QIcon()
        icon15.addFile(u":/icons/asset/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_database.setIcon(icon15)
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
        self.verticalLayout_8.setContentsMargins(-1, -1, 5, -1)
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font3)
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
        self.horizontalLayout_10.setSpacing(9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 5, 9)
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
        self.gridLayout_2.setContentsMargins(20, -1, -1, 9)
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
        self.brigthness.setInvertedAppearance(False)
        self.brigthness.setInvertedControls(False)

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
        self.scan_range_label.setGeometry(QRect(20, 160, 430, 51))
        self.scan_range_label.setMinimumSize(QSize(430, 0))
        self.scan_range_label.setMaximumSize(QSize(420, 16777215))
        self.scan_range_label.setFont(font4)
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
        self.btn_scan_range.setGeometry(QRect(310, 80, 140, 51))
        self.btn_scan_range.setMinimumSize(QSize(140, 0))
        self.btn_scan_range.setMaximumSize(QSize(135, 16777215))
        self.btn_scan_range.setFont(font2)
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
        self.btn_scan_range.setIcon(icon4)
        self.btn_scan_range.setIconSize(QSize(30, 30))
        self.btn_scan_range.setFlat(True)
        self.scan_range = QLineEdit(self.frame_5)
        self.scan_range.setObjectName(u"scan_range")
        self.scan_range.setGeometry(QRect(20, 80, 271, 51))
        self.scan_range.setFont(font2)
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
        self.left_frame_2.setMinimumSize(QSize(520, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 0, 9, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 610))
        self.top.setMaximumSize(QSize(500, 620))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_validity = QLabel(self.top)
        self.db_validity.setObjectName(u"db_validity")
        self.db_validity.setGeometry(QRect(20, 440, 271, 41))
        self.db_validity.setFont(font4)
        self.db_validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"}")
        self.db_validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(300, 290, 191, 41))
        self.db_refrence.setFont(font4)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_year = QLabel(self.top)
        self.db_year.setObjectName(u"db_year")
        self.db_year.setGeometry(QRect(20, 490, 101, 41))
        self.db_year.setFont(font4)
        self.db_year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_nationality = QLabel(self.top)
        self.db_nationality.setObjectName(u"db_nationality")
        self.db_nationality.setGeometry(QRect(230, 490, 261, 41))
        self.db_nationality.setFont(font4)
        self.db_nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 140, 271, 291))
        self.db_image_data.setFont(font3)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.db_image_data.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(300, 240, 191, 41))
        self.db_lastname.setFont(font4)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(300, 190, 191, 41))
        self.db_middlename.setFont(font4)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(300, 140, 191, 41))
        self.db_firstname.setFont(font4)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_index = QLabel(self.top)
        self.db_index.setObjectName(u"db_index")
        self.db_index.setGeometry(QRect(300, 340, 191, 41))
        self.db_index.setFont(font4)
        self.db_index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_college = QLabel(self.top)
        self.db_college.setObjectName(u"db_college")
        self.db_college.setGeometry(QRect(300, 390, 91, 41))
        self.db_college.setFont(font4)
        self.db_college.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_college.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_box = QLineEdit(self.top)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(20, 30, 321, 51))
        self.search_box.setFont(font2)
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
        self.btn_search_page.setGeometry(QRect(360, 30, 131, 51))
        self.btn_search_page.setFont(font2)
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
        self.btn_search_page.setIcon(icon4)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_29 = QLabel(self.top)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 491, 91))
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
        self.image_3.setGeometry(QRect(10, 120, 491, 501))
        self.image_3.setMinimumSize(QSize(0, 408))
        self.image_3.setFont(font3)
        self.image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_3.setAlignment(Qt.AlignCenter)
        self.db_type = QLabel(self.top)
        self.db_type.setObjectName(u"db_type")
        self.db_type.setGeometry(QRect(300, 440, 191, 41))
        self.db_type.setFont(font4)
        self.db_type.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.db_type.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_faculty = QLabel(self.top)
        self.db_faculty.setObjectName(u"db_faculty")
        self.db_faculty.setGeometry(QRect(400, 390, 91, 41))
        self.db_faculty.setFont(font4)
        self.db_faculty.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.db_faculty.setAlignment(Qt.AlignCenter)
        self.dbgender = QLabel(self.top)
        self.dbgender.setObjectName(u"dbgender")
        self.dbgender.setGeometry(QRect(130, 490, 91, 41))
        self.dbgender.setFont(font4)
        self.dbgender.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.dbgender.setAlignment(Qt.AlignCenter)
        self.db_programe = QLabel(self.top)
        self.db_programe.setObjectName(u"db_programe")
        self.db_programe.setGeometry(QRect(20, 540, 471, 55))
        self.db_programe.setMinimumSize(QSize(0, 55))
        self.db_programe.setFont(font4)
        self.db_programe.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_programe.setAlignment(Qt.AlignCenter)
        self.db_programe.setWordWrap(True)
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
        self.db_college.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()
        self.db_type.raise_()
        self.db_faculty.raise_()
        self.dbgender.raise_()
        self.db_programe.raise_()

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 200))
        self.bottom.setMaximumSize(QSize(16777215, 350))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.start_date = QRadioButton(self.bottom)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(20, 180, 261, 20))
        self.start_date.setFont(font6)
        self.start_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.start_date.setIcon(icon6)
        self.start_date.setChecked(False)
        self.start_date.setAutoExclusive(False)
        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(20, 220, 221, 51))
        self.db_start_date.setFont(font2)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
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
        self.db_end_date.setGeometry(QRect(260, 220, 231, 51))
        self.db_end_date.setFont(font2)
        self.db_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
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
        self.label_25.setGeometry(QRect(30, 230, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 170, 491, 171))
        self.label_30.setMinimumSize(QSize(0, 0))
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
        self.btn_reload.setGeometry(QRect(350, 90, 141, 41))
        self.btn_reload.setFont(font2)
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
        self.btn_reload.setIcon(icon14)
        self.btn_reload.setIconSize(QSize(30, 30))
        self.btn_reload.setFlat(True)
        self.btn_csv = QPushButton(self.bottom)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setGeometry(QRect(20, 90, 131, 41))
        self.btn_csv.setFont(font2)
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
        icon16 = QIcon()
        icon16.addFile(u":/icons/asset/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_csv.setIcon(icon16)
        self.btn_csv.setIconSize(QSize(30, 30))
        self.btn_csv.setFlat(True)
        self.label_26 = QLabel(self.bottom)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 230, 31, 31))
        self.label_26.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_40 = QLabel(self.bottom)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 20, 491, 131))
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
        self.checkBox.setGeometry(QRect(300, 180, 181, 20))
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/asset/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon17)
        self.btn_json = QPushButton(self.bottom)
        self.btn_json.setObjectName(u"btn_json")
        self.btn_json.setGeometry(QRect(170, 90, 161, 41))
        self.btn_json.setFont(font2)
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
        icon18 = QIcon()
        icon18.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_json.setIcon(icon18)
        self.btn_json.setIconSize(QSize(30, 30))
        self.btn_json.setFlat(True)
        self.search_page_date = QDateEdit(self.bottom)
        self.search_page_date.setObjectName(u"search_page_date")
        self.search_page_date.setGeometry(QRect(20, 280, 151, 41))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        self.search_page_date.setFont(font8)
        self.search_page_date.setStyleSheet(u"QDateEdit{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border: 2px solid rgb(45, 45, 45);\n"
"padding-left:10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.search_page_date.setFrame(False)
        self.search_page_date.setReadOnly(False)
        self.search_page_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.search_page_date.setAccelerated(True)
        self.search_page_date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.search_page_date.setProperty("showGroupSeparator", False)
        self.search_page_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.search_page_date.setMinimumDate(QDate(2023, 1, 1))
        self.search_page_date.setCalendarPopup(True)
        self.search_page_date.setTimeSpec(Qt.LocalTime)
        self.search_page_date.setDate(QDate(2023, 1, 1))
        self.db_current_session = QRadioButton(self.bottom)
        self.db_current_session.setObjectName(u"db_current_session")
        self.db_current_session.setGeometry(QRect(200, 280, 291, 41))
        self.db_current_session.setFont(font6)
        self.db_current_session.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"border-radius: 10px;\n"
"}")
        self.db_current_session.setIcon(icon9)
        self.db_current_session.setCheckable(True)
        self.db_current_session.setChecked(False)
        self.db_current_session.setAutoRepeat(False)
        self.db_current_session.setAutoExclusive(False)
        self.search_page_filename = QLineEdit(self.bottom)
        self.search_page_filename.setObjectName(u"search_page_filename")
        self.search_page_filename.setGeometry(QRect(20, 40, 471, 41))
        self.search_page_filename.setFont(font2)
        self.search_page_filename.setStyleSheet(u"QLineEdit{\n"
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
        self.search_page_filename.setClearButtonEnabled(True)
        self.label_40.raise_()
        self.label_30.raise_()
        self.start_date.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.db_end_date.raise_()
        self.btn_reload.raise_()
        self.btn_csv.raise_()
        self.label_26.raise_()
        self.checkBox.raise_()
        self.btn_json.raise_()
        self.search_page_date.raise_()
        self.db_current_session.raise_()
        self.search_page_filename.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.NoFrame)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 5, 9)
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 5, -1)
        self.frame_27 = QFrame(self.batch)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 100))
        self.frame_27.setMaximumSize(QSize(16777215, 100))
        self.frame_27.setFrameShape(QFrame.NoFrame)
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
        font9 = QFont()
        font9.setFamily(u"Microsoft Sans Serif")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.batch_notification.setFont(font9)
        self.batch_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	\n"
"}")
        self.batch_notification.setAlignment(Qt.AlignCenter)
        self.batch_notification.setWordWrap(True)
        self.btn_batch_browse = QPushButton(self.frame_27)
        self.btn_batch_browse.setObjectName(u"btn_batch_browse")
        self.btn_batch_browse.setGeometry(QRect(400, 20, 121, 51))
        self.btn_batch_browse.setFont(font2)
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
        self.btn_batch_browse.setIcon(icon18)
        self.btn_batch_browse.setIconSize(QSize(30, 30))
        self.btn_batch_browse.setFlat(True)
        self.batch_browse = QLineEdit(self.frame_27)
        self.batch_browse.setObjectName(u"batch_browse")
        self.batch_browse.setGeometry(QRect(20, 20, 221, 51))
        self.batch_browse.setFont(font2)
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
        self.btn_start_job.setGeometry(QRect(540, 20, 121, 51))
        self.btn_start_job.setFont(font2)
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
        self.btn_start_job.setIcon(icon6)
        self.btn_start_job.setIconSize(QSize(30, 30))
        self.btn_start_job.setFlat(True)
        self.btn_batch_mail = QPushButton(self.frame_27)
        self.btn_batch_mail.setObjectName(u"btn_batch_mail")
        self.btn_batch_mail.setGeometry(QRect(960, 20, 121, 51))
        self.btn_batch_mail.setFont(font2)
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
        self.btn_batch_mail.setIcon(icon11)
        self.btn_batch_mail.setIconSize(QSize(30, 30))
        self.btn_batch_mail.setFlat(True)
        self.btn_batch_folder = QPushButton(self.frame_27)
        self.btn_batch_folder.setObjectName(u"btn_batch_folder")
        self.btn_batch_folder.setGeometry(QRect(680, 20, 121, 51))
        self.btn_batch_folder.setFont(font2)
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
        icon19 = QIcon()
        icon19.addFile(u":/icons/asset/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch_folder.setIcon(icon19)
        self.btn_batch_folder.setIconSize(QSize(30, 30))
        self.btn_batch_folder.setFlat(True)
        self.btn_batch_images = QPushButton(self.frame_27)
        self.btn_batch_images.setObjectName(u"btn_batch_images")
        self.btn_batch_images.setGeometry(QRect(820, 20, 121, 51))
        self.btn_batch_images.setFont(font2)
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
        icon20 = QIcon()
        icon20.addFile(u":/icons/asset/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_batch_images.setIcon(icon20)
        self.btn_batch_images.setIconSize(QSize(30, 30))
        self.btn_batch_images.setFlat(True)
        self.header_check = QRadioButton(self.frame_27)
        self.header_check.setObjectName(u"header_check")
        self.header_check.setGeometry(QRect(260, 20, 121, 51))
        self.header_check.setFont(font2)
        self.header_check.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:5px;")
        self.header_check.setAutoExclusive(False)

        self.verticalLayout_20.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.batch)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_29)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 5, 0)
        self.tableWidget_batch = QTableWidget(self.frame_29)
        if (self.tableWidget_batch.columnCount() < 12):
            self.tableWidget_batch.setColumnCount(12)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.tableWidget_batch.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        self.tableWidget_batch.setObjectName(u"tableWidget_batch")
        self.tableWidget_batch.setFont(font2)
        self.tableWidget_batch.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget_batch.setFrameShape(QFrame.NoFrame)
        self.tableWidget_batch.setFrameShadow(QFrame.Plain)
        self.tableWidget_batch.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_batch.setSortingEnabled(True)
        self.tableWidget_batch.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_batch.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_batch.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.tableWidget_batch)


        self.verticalLayout_20.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.batch)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_7 = QHBoxLayout(self.page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(350, 0))
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.design = QLabel(self.frame_6)
        self.design.setObjectName(u"design")
        self.design.setGeometry(QRect(10, 10, 331, 91))
        self.design.setFont(font5)
        self.design.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.design_2 = QLabel(self.frame_6)
        self.design_2.setObjectName(u"design_2")
        self.design_2.setGeometry(QRect(10, 670, 331, 291))
        self.design_2.setFont(font5)
        self.design_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.db_consolidation_range = QRadioButton(self.frame_6)
        self.db_consolidation_range.setObjectName(u"db_consolidation_range")
        self.db_consolidation_range.setGeometry(QRect(170, 210, 161, 41))
        self.db_consolidation_range.setFont(font2)
        self.db_consolidation_range.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:5px;")
        self.db_consolidation_range.setAutoExclusive(False)
        self.db_consolidation_date = QDateEdit(self.frame_6)
        self.db_consolidation_date.setObjectName(u"db_consolidation_date")
        self.db_consolidation_date.setGeometry(QRect(20, 210, 141, 41))
        self.db_consolidation_date.setFont(font8)
        self.db_consolidation_date.setStyleSheet(u"QDateEdit{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border: 2px solid rgb(45, 45, 45);\n"
"padding-left:10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.db_consolidation_date.setFrame(False)
        self.db_consolidation_date.setReadOnly(False)
        self.db_consolidation_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.db_consolidation_date.setAccelerated(True)
        self.db_consolidation_date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.db_consolidation_date.setProperty("showGroupSeparator", False)
        self.db_consolidation_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.db_consolidation_date.setMinimumDate(QDate(2023, 1, 1))
        self.db_consolidation_date.setCalendarPopup(True)
        self.db_consolidation_date.setTimeSpec(Qt.LocalTime)
        self.db_consolidation_date.setDate(QDate(2023, 1, 1))
        self.db_consolidation_start = QLineEdit(self.frame_6)
        self.db_consolidation_start.setObjectName(u"db_consolidation_start")
        self.db_consolidation_start.setGeometry(QRect(20, 160, 151, 41))
        self.db_consolidation_start.setFont(font2)
        self.db_consolidation_start.setTabletTracking(True)
        self.db_consolidation_start.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_start.setFrame(True)
        self.db_consolidation_start.setReadOnly(True)
        self.db_consolidation_start.setClearButtonEnabled(False)
        self.db_consolidation_stop = QLineEdit(self.frame_6)
        self.db_consolidation_stop.setObjectName(u"db_consolidation_stop")
        self.db_consolidation_stop.setGeometry(QRect(180, 160, 151, 41))
        self.db_consolidation_stop.setFont(font2)
        self.db_consolidation_stop.setTabletTracking(True)
        self.db_consolidation_stop.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_stop.setReadOnly(True)
        self.db_consolidation_stop.setClearButtonEnabled(False)
        self.db_consolidation_notification = QLabel(self.frame_6)
        self.db_consolidation_notification.setObjectName(u"db_consolidation_notification")
        self.db_consolidation_notification.setGeometry(QRect(20, 470, 311, 71))
        self.db_consolidation_notification.setFont(font5)
        self.db_consolidation_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.db_consolidation_notification.setAlignment(Qt.AlignCenter)
        self.db_consolidation_notification.setWordWrap(True)
        self.db_consolidation_partition = QLineEdit(self.frame_6)
        self.db_consolidation_partition.setObjectName(u"db_consolidation_partition")
        self.db_consolidation_partition.setGeometry(QRect(20, 370, 311, 41))
        self.db_consolidation_partition.setFont(font2)
        self.db_consolidation_partition.setTabletTracking(True)
        self.db_consolidation_partition.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_partition.setClearButtonEnabled(True)
        self.btn_consolidation_load = QPushButton(self.frame_6)
        self.btn_consolidation_load.setObjectName(u"btn_consolidation_load")
        self.btn_consolidation_load.setGeometry(QRect(20, 260, 131, 41))
        self.btn_consolidation_load.setFont(font2)
        self.btn_consolidation_load.setStyleSheet(u"QPushButton{\n"
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
        icon21.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consolidation_load.setIcon(icon21)
        self.btn_consolidation_load.setIconSize(QSize(30, 30))
        self.btn_consolidation_load.setFlat(True)
        self.design_4 = QLabel(self.frame_6)
        self.design_4.setObjectName(u"design_4")
        self.design_4.setGeometry(QRect(10, 120, 331, 191))
        self.design_4.setFont(font5)
        self.design_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.design_5 = QLabel(self.frame_6)
        self.design_5.setObjectName(u"design_5")
        self.design_5.setGeometry(QRect(10, 330, 331, 221))
        self.design_5.setFont(font5)
        self.design_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_consolidation_partition = QPushButton(self.frame_6)
        self.btn_consolidation_partition.setObjectName(u"btn_consolidation_partition")
        self.btn_consolidation_partition.setGeometry(QRect(180, 420, 151, 41))
        self.btn_consolidation_partition.setFont(font2)
        self.btn_consolidation_partition.setStyleSheet(u"QPushButton{\n"
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
        icon22.addFile(u":/icons/asset/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consolidation_partition.setIcon(icon22)
        self.btn_consolidation_partition.setIconSize(QSize(30, 30))
        self.btn_consolidation_partition.setFlat(True)
        self.btn_consolidation_upload = QPushButton(self.frame_6)
        self.btn_consolidation_upload.setObjectName(u"btn_consolidation_upload")
        self.btn_consolidation_upload.setGeometry(QRect(20, 420, 151, 41))
        self.btn_consolidation_upload.setFont(font2)
        self.btn_consolidation_upload.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consolidation_upload.setIcon(icon5)
        self.btn_consolidation_upload.setIconSize(QSize(30, 30))
        self.btn_consolidation_upload.setFlat(True)
        self.design_6 = QLabel(self.frame_6)
        self.design_6.setObjectName(u"design_6")
        self.design_6.setGeometry(QRect(10, 570, 331, 81))
        self.design_6.setFont(font5)
        self.design_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.db_consolidation_mail = QLineEdit(self.frame_6)
        self.db_consolidation_mail.setObjectName(u"db_consolidation_mail")
        self.db_consolidation_mail.setGeometry(QRect(20, 600, 311, 41))
        self.db_consolidation_mail.setFont(font2)
        self.db_consolidation_mail.setTabletTracking(True)
        self.db_consolidation_mail.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_mail.setClearButtonEnabled(True)
        self.db_consolidation_username = QLineEdit(self.frame_6)
        self.db_consolidation_username.setObjectName(u"db_consolidation_username")
        self.db_consolidation_username.setGeometry(QRect(20, 760, 141, 41))
        self.db_consolidation_username.setFont(font2)
        self.db_consolidation_username.setTabletTracking(True)
        self.db_consolidation_username.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_username.setClearButtonEnabled(True)
        self.db_consolidation_password = QLineEdit(self.frame_6)
        self.db_consolidation_password.setObjectName(u"db_consolidation_password")
        self.db_consolidation_password.setGeometry(QRect(20, 810, 311, 41))
        self.db_consolidation_password.setFont(font2)
        self.db_consolidation_password.setTabletTracking(True)
        self.db_consolidation_password.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_password.setEchoMode(QLineEdit.Password)
        self.db_consolidation_password.setClearButtonEnabled(True)
        self.db_consolidation_database = QLineEdit(self.frame_6)
        self.db_consolidation_database.setObjectName(u"db_consolidation_database")
        self.db_consolidation_database.setGeometry(QRect(170, 760, 161, 41))
        self.db_consolidation_database.setFont(font2)
        self.db_consolidation_database.setTabletTracking(True)
        self.db_consolidation_database.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_database.setClearButtonEnabled(True)
        self.db_consolidation_hostname = QLineEdit(self.frame_6)
        self.db_consolidation_hostname.setObjectName(u"db_consolidation_hostname")
        self.db_consolidation_hostname.setGeometry(QRect(20, 860, 201, 41))
        self.db_consolidation_hostname.setFont(font2)
        self.db_consolidation_hostname.setTabletTracking(True)
        self.db_consolidation_hostname.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_hostname.setClearButtonEnabled(True)
        self.db_consolidation_port = QLineEdit(self.frame_6)
        self.db_consolidation_port.setObjectName(u"db_consolidation_port")
        self.db_consolidation_port.setGeometry(QRect(230, 860, 101, 41))
        self.db_consolidation_port.setFont(font2)
        self.db_consolidation_port.setTabletTracking(True)
        self.db_consolidation_port.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_port.setClearButtonEnabled(True)
        self.btn_consolidation_test = QPushButton(self.frame_6)
        self.btn_consolidation_test.setObjectName(u"btn_consolidation_test")
        self.btn_consolidation_test.setGeometry(QRect(180, 910, 151, 41))
        self.btn_consolidation_test.setFont(font2)
        self.btn_consolidation_test.setStyleSheet(u"QPushButton{\n"
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
        icon23.addFile(u":/icons/asset/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consolidation_test.setIcon(icon23)
        self.btn_consolidation_test.setIconSize(QSize(30, 30))
        self.btn_consolidation_test.setFlat(True)
        self.db_consolidation_facility = QLineEdit(self.frame_6)
        self.db_consolidation_facility.setObjectName(u"db_consolidation_facility")
        self.db_consolidation_facility.setGeometry(QRect(20, 50, 311, 41))
        self.db_consolidation_facility.setFont(font2)
        self.db_consolidation_facility.setTabletTracking(True)
        self.db_consolidation_facility.setStyleSheet(u"QLineEdit{\n"
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
        self.db_consolidation_facility.setClearButtonEnabled(True)
        self.db_fetch_all = QRadioButton(self.frame_6)
        self.db_fetch_all.setObjectName(u"db_fetch_all")
        self.db_fetch_all.setGeometry(QRect(170, 260, 161, 41))
        self.db_fetch_all.setFont(font2)
        self.db_fetch_all.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:5px;")
        self.db_fetch_all.setAutoExclusive(False)
        self.database_tables = QComboBox(self.frame_6)
        self.database_tables.setObjectName(u"database_tables")
        self.database_tables.setGeometry(QRect(20, 710, 211, 40))
        self.database_tables.setMinimumSize(QSize(0, 40))
        self.database_tables.setMaximumSize(QSize(371, 40))
        self.database_tables.setFont(font2)
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
        self.btn_load_tables = QPushButton(self.frame_6)
        self.btn_load_tables.setObjectName(u"btn_load_tables")
        self.btn_load_tables.setGeometry(QRect(240, 710, 91, 41))
        self.btn_load_tables.setFont(font2)
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
        self.btn_consolidation_update = QPushButton(self.frame_6)
        self.btn_consolidation_update.setObjectName(u"btn_consolidation_update")
        self.btn_consolidation_update.setGeometry(QRect(20, 910, 141, 41))
        self.btn_consolidation_update.setFont(font2)
        self.btn_consolidation_update.setStyleSheet(u"QPushButton{\n"
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
        self.btn_consolidation_update.setIcon(icon6)
        self.btn_consolidation_update.setIconSize(QSize(30, 30))
        self.btn_consolidation_update.setFlat(True)
        self.design_5.raise_()
        self.design_4.raise_()
        self.design.raise_()
        self.design_2.raise_()
        self.db_consolidation_range.raise_()
        self.db_consolidation_date.raise_()
        self.db_consolidation_start.raise_()
        self.db_consolidation_stop.raise_()
        self.db_consolidation_notification.raise_()
        self.db_consolidation_partition.raise_()
        self.btn_consolidation_load.raise_()
        self.btn_consolidation_partition.raise_()
        self.btn_consolidation_upload.raise_()
        self.design_6.raise_()
        self.db_consolidation_mail.raise_()
        self.db_consolidation_username.raise_()
        self.db_consolidation_password.raise_()
        self.db_consolidation_database.raise_()
        self.db_consolidation_hostname.raise_()
        self.db_consolidation_port.raise_()
        self.btn_consolidation_test.raise_()
        self.db_consolidation_facility.raise_()
        self.db_fetch_all.raise_()
        self.database_tables.raise_()
        self.btn_load_tables.raise_()
        self.btn_consolidation_update.raise_()

        self.horizontalLayout_7.addWidget(self.frame_6)

        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 5, 5)
        self.merge_table = QTableWidget(self.frame_15)
        if (self.merge_table.columnCount() < 7):
            self.merge_table.setColumnCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        self.merge_table.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        self.merge_table.setObjectName(u"merge_table")
        self.merge_table.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.merge_table.setFrameShape(QFrame.NoFrame)
        self.merge_table.setFrameShadow(QFrame.Plain)
        self.merge_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.merge_table.setSortingEnabled(True)
        self.merge_table.horizontalHeader().setCascadingSectionResizes(True)
        self.merge_table.horizontalHeader().setDefaultSectionSize(150)
        self.merge_table.horizontalHeader().setStretchLastSection(True)
        self.merge_table.verticalHeader().setProperty("showSortIndicator", False)
        self.merge_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_11.addWidget(self.merge_table)


        self.horizontalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page)
        self.admin = QWidget()
        self.admin.setObjectName(u"admin")
        self.horizontalLayout_6 = QHBoxLayout(self.admin)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 0, 0, 0)
        self.left_child = QFrame(self.admin)
        self.left_child.setObjectName(u"left_child")
        self.left_child.setMinimumSize(QSize(550, 950))
        self.left_child.setMaximumSize(QSize(550, 16777215))
        self.left_child.setFrameShape(QFrame.NoFrame)
        self.left_child.setFrameShadow(QFrame.Plain)
        self.firstname_25 = QLabel(self.left_child)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 10, 531, 91))
        self.firstname_25.setFont(font5)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_26 = QLabel(self.left_child)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 120, 531, 441))
        self.firstname_26.setFont(font5)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.user_search = QLineEdit(self.left_child)
        self.user_search.setObjectName(u"user_search")
        self.user_search.setGeometry(QRect(30, 30, 331, 51))
        self.user_search.setMinimumSize(QSize(0, 47))
        self.user_search.setFont(font2)
        self.user_search.setStyleSheet(u"QLineEdit{\n"
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
        self.user_search.setClearButtonEnabled(True)
        self.btn_user_search = QPushButton(self.left_child)
        self.btn_user_search.setObjectName(u"btn_user_search")
        self.btn_user_search.setGeometry(QRect(370, 30, 151, 51))
        self.btn_user_search.setMinimumSize(QSize(0, 47))
        self.btn_user_search.setFont(font2)
        self.btn_user_search.setStyleSheet(u"QPushButton{\n"
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
        self.btn_user_search.setIcon(icon4)
        self.btn_user_search.setIconSize(QSize(30, 30))
        self.btn_user_search.setFlat(True)
        self.user_image = QLabel(self.left_child)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setGeometry(QRect(30, 140, 241, 261))
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.user_image.setFont(font10)
        self.user_image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.user_image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.user_image.setAlignment(Qt.AlignCenter)
        self.user_middlename = QLineEdit(self.left_child)
        self.user_middlename.setObjectName(u"user_middlename")
        self.user_middlename.setGeometry(QRect(290, 210, 231, 53))
        self.user_middlename.setMinimumSize(QSize(0, 53))
        self.user_middlename.setMaximumSize(QSize(16777215, 53))
        self.user_middlename.setFont(font2)
        self.user_middlename.setStyleSheet(u"QLineEdit{\n"
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
        self.user_middlename.setClearButtonEnabled(True)
        self.user_lastname = QLineEdit(self.left_child)
        self.user_lastname.setObjectName(u"user_lastname")
        self.user_lastname.setGeometry(QRect(290, 280, 231, 53))
        self.user_lastname.setMinimumSize(QSize(0, 53))
        self.user_lastname.setMaximumSize(QSize(16777215, 53))
        self.user_lastname.setFont(font2)
        self.user_lastname.setStyleSheet(u"QLineEdit{\n"
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
        self.user_lastname.setClearButtonEnabled(True)
        self.user_firstname = QLineEdit(self.left_child)
        self.user_firstname.setObjectName(u"user_firstname")
        self.user_firstname.setGeometry(QRect(290, 140, 231, 53))
        self.user_firstname.setMinimumSize(QSize(0, 53))
        self.user_firstname.setMaximumSize(QSize(16777215, 53))
        self.user_firstname.setFont(font2)
        self.user_firstname.setTabletTracking(True)
        self.user_firstname.setStyleSheet(u"QLineEdit{\n"
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
        self.user_firstname.setClearButtonEnabled(True)
        self.user_reference = QLineEdit(self.left_child)
        self.user_reference.setObjectName(u"user_reference")
        self.user_reference.setGeometry(QRect(290, 350, 231, 53))
        self.user_reference.setMinimumSize(QSize(0, 53))
        self.user_reference.setMaximumSize(QSize(16777215, 53))
        self.user_reference.setFont(font2)
        self.user_reference.setStyleSheet(u"QLineEdit{\n"
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
        self.user_reference.setClearButtonEnabled(True)
        self.user_contact = QLineEdit(self.left_child)
        self.user_contact.setObjectName(u"user_contact")
        self.user_contact.setGeometry(QRect(290, 420, 231, 53))
        self.user_contact.setMinimumSize(QSize(0, 53))
        self.user_contact.setMaximumSize(QSize(16777215, 53))
        self.user_contact.setFont(font2)
        self.user_contact.setStyleSheet(u"QLineEdit{\n"
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
        self.user_contact.setClearButtonEnabled(True)
        self.user_role = QComboBox(self.left_child)
        self.user_role.addItem("")
        self.user_role.addItem("")
        self.user_role.addItem("")
        self.user_role.setObjectName(u"user_role")
        self.user_role.setGeometry(QRect(30, 420, 241, 53))
        self.user_role.setMinimumSize(QSize(0, 53))
        self.user_role.setMaximumSize(QSize(16777215, 53))
        self.user_role.setFont(font2)
        self.user_role.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.user_role.setFrame(False)
        self.user_email = QLineEdit(self.left_child)
        self.user_email.setObjectName(u"user_email")
        self.user_email.setGeometry(QRect(30, 490, 301, 53))
        self.user_email.setMinimumSize(QSize(0, 53))
        self.user_email.setMaximumSize(QSize(16777215, 53))
        self.user_email.setFont(font2)
        self.user_email.setStyleSheet(u"QLineEdit{\n"
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
        self.user_email.setClearButtonEnabled(True)
        self.firstname_27 = QLabel(self.left_child)
        self.firstname_27.setObjectName(u"firstname_27")
        self.firstname_27.setGeometry(QRect(10, 580, 531, 81))
        self.firstname_27.setFont(font5)
        self.firstname_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_user_register = QPushButton(self.left_child)
        self.btn_user_register.setObjectName(u"btn_user_register")
        self.btn_user_register.setGeometry(QRect(30, 600, 141, 41))
        self.btn_user_register.setFont(font2)
        self.btn_user_register.setStyleSheet(u"QPushButton{\n"
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
        self.btn_user_register.setIcon(icon3)
        self.btn_user_register.setIconSize(QSize(30, 30))
        self.btn_user_register.setFlat(True)
        self.btn_user_update = QPushButton(self.left_child)
        self.btn_user_update.setObjectName(u"btn_user_update")
        self.btn_user_update.setGeometry(QRect(200, 600, 141, 41))
        self.btn_user_update.setFont(font2)
        self.btn_user_update.setStyleSheet(u"QPushButton{\n"
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
        self.btn_user_update.setIcon(icon1)
        self.btn_user_update.setIconSize(QSize(30, 30))
        self.btn_user_update.setFlat(True)
        self.btn_user_status = QPushButton(self.left_child)
        self.btn_user_status.setObjectName(u"btn_user_status")
        self.btn_user_status.setGeometry(QRect(370, 600, 151, 41))
        self.btn_user_status.setFont(font2)
        self.btn_user_status.setStyleSheet(u"QPushButton{\n"
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
        icon24 = QIcon()
        icon24.addFile(u":/icons/asset/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user_status.setIcon(icon24)
        self.btn_user_status.setIconSize(QSize(30, 30))
        self.btn_user_status.setFlat(True)
        self.firstname_28 = QLabel(self.left_child)
        self.firstname_28.setObjectName(u"firstname_28")
        self.firstname_28.setGeometry(QRect(10, 880, 531, 91))
        self.firstname_28.setFont(font5)
        self.firstname_28.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.user_image_file = QLineEdit(self.left_child)
        self.user_image_file.setObjectName(u"user_image_file")
        self.user_image_file.setGeometry(QRect(30, 900, 351, 50))
        self.user_image_file.setMinimumSize(QSize(0, 50))
        self.user_image_file.setMaximumSize(QSize(16777215, 50))
        self.user_image_file.setFont(font2)
        self.user_image_file.setStyleSheet(u"QLineEdit{\n"
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
        self.user_image_file.setClearButtonEnabled(True)
        self.user_image_browse = QPushButton(self.left_child)
        self.user_image_browse.setObjectName(u"user_image_browse")
        self.user_image_browse.setGeometry(QRect(400, 900, 121, 50))
        self.user_image_browse.setMinimumSize(QSize(0, 50))
        self.user_image_browse.setMaximumSize(QSize(16777215, 50))
        self.user_image_browse.setFont(font2)
        self.user_image_browse.setStyleSheet(u"QPushButton{\n"
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
        self.user_image_browse.setIcon(icon5)
        self.user_image_browse.setIconSize(QSize(30, 30))
        self.user_image_browse.setFlat(True)
        self.firstname_29 = QLabel(self.left_child)
        self.firstname_29.setObjectName(u"firstname_29")
        self.firstname_29.setGeometry(QRect(10, 680, 531, 81))
        self.firstname_29.setFont(font5)
        self.firstname_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_mail_user_details = QPushButton(self.left_child)
        self.btn_mail_user_details.setObjectName(u"btn_mail_user_details")
        self.btn_mail_user_details.setGeometry(QRect(30, 800, 151, 41))
        self.btn_mail_user_details.setMinimumSize(QSize(0, 41))
        self.btn_mail_user_details.setMaximumSize(QSize(16777215, 41))
        self.btn_mail_user_details.setFont(font2)
        self.btn_mail_user_details.setStyleSheet(u"QPushButton{\n"
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
        icon25 = QIcon()
        icon25.addFile(u":/icons/asset/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mail_user_details.setIcon(icon25)
        self.btn_mail_user_details.setIconSize(QSize(30, 30))
        self.btn_mail_user_details.setFlat(True)
        self.btn_user_clear = QPushButton(self.left_child)
        self.btn_user_clear.setObjectName(u"btn_user_clear")
        self.btn_user_clear.setGeometry(QRect(370, 800, 151, 41))
        self.btn_user_clear.setFont(font2)
        self.btn_user_clear.setStyleSheet(u"QPushButton{\n"
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
        self.btn_user_clear.setIcon(icon14)
        self.btn_user_clear.setIconSize(QSize(30, 30))
        self.btn_user_clear.setFlat(True)
        self.user_start_date = QDateEdit(self.left_child)
        self.user_start_date.setObjectName(u"user_start_date")
        self.user_start_date.setGeometry(QRect(80, 700, 141, 41))
        self.user_start_date.setFont(font8)
        self.user_start_date.setStyleSheet(u"QDateEdit{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border: 2px solid rgb(45, 45, 45);\n"
"padding-left:10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.user_start_date.setFrame(False)
        self.user_start_date.setReadOnly(False)
        self.user_start_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.user_start_date.setAccelerated(True)
        self.user_start_date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.user_start_date.setProperty("showGroupSeparator", False)
        self.user_start_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.user_start_date.setMinimumDate(QDate(2023, 1, 1))
        self.user_start_date.setCalendarPopup(True)
        self.user_start_date.setTimeSpec(Qt.LocalTime)
        self.user_start_date.setDate(QDate(2023, 1, 1))
        self.user_status = QComboBox(self.left_child)
        self.user_status.addItem("")
        self.user_status.addItem("")
        self.user_status.setObjectName(u"user_status")
        self.user_status.setGeometry(QRect(340, 490, 181, 53))
        self.user_status.setMinimumSize(QSize(0, 53))
        self.user_status.setMaximumSize(QSize(16777215, 53))
        self.user_status.setFont(font2)
        self.user_status.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.user_status.setFrame(False)
        self.user_range = QRadioButton(self.left_child)
        self.user_range.setObjectName(u"user_range")
        self.user_range.setGeometry(QRect(30, 700, 41, 41))
        self.user_range.setFont(font2)
        self.user_range.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:5px;")
        self.user_range.setAutoExclusive(False)
        self.firstname_30 = QLabel(self.left_child)
        self.firstname_30.setObjectName(u"firstname_30")
        self.firstname_30.setGeometry(QRect(10, 780, 531, 81))
        self.firstname_30.setFont(font5)
        self.firstname_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_export_data = QPushButton(self.left_child)
        self.btn_export_data.setObjectName(u"btn_export_data")
        self.btn_export_data.setGeometry(QRect(200, 800, 151, 41))
        self.btn_export_data.setMinimumSize(QSize(0, 41))
        self.btn_export_data.setMaximumSize(QSize(16777215, 41))
        self.btn_export_data.setFont(font2)
        self.btn_export_data.setStyleSheet(u"QPushButton{\n"
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
        self.btn_export_data.setIcon(icon16)
        self.btn_export_data.setIconSize(QSize(30, 30))
        self.btn_export_data.setFlat(True)
        self.user_end_date = QLineEdit(self.left_child)
        self.user_end_date.setObjectName(u"user_end_date")
        self.user_end_date.setGeometry(QRect(230, 700, 141, 41))
        self.user_end_date.setFont(font2)
        self.user_end_date.setTabletTracking(True)
        self.user_end_date.setStyleSheet(u"QLineEdit{\n"
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
        self.user_end_date.setClearButtonEnabled(True)
        self.user_date = QLineEdit(self.left_child)
        self.user_date.setObjectName(u"user_date")
        self.user_date.setGeometry(QRect(380, 700, 141, 41))
        self.user_date.setFont(font2)
        self.user_date.setTabletTracking(True)
        self.user_date.setStyleSheet(u"QLineEdit{\n"
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
        self.user_date.setClearButtonEnabled(True)
        self.firstname_30.raise_()
        self.firstname_26.raise_()
        self.firstname_25.raise_()
        self.user_search.raise_()
        self.btn_user_search.raise_()
        self.user_image.raise_()
        self.user_middlename.raise_()
        self.user_lastname.raise_()
        self.user_firstname.raise_()
        self.user_reference.raise_()
        self.user_contact.raise_()
        self.user_role.raise_()
        self.user_email.raise_()
        self.firstname_27.raise_()
        self.btn_user_register.raise_()
        self.btn_user_update.raise_()
        self.btn_user_status.raise_()
        self.firstname_28.raise_()
        self.user_image_file.raise_()
        self.user_image_browse.raise_()
        self.firstname_29.raise_()
        self.btn_mail_user_details.raise_()
        self.btn_user_clear.raise_()
        self.user_start_date.raise_()
        self.user_status.raise_()
        self.user_range.raise_()
        self.btn_export_data.raise_()
        self.user_end_date.raise_()
        self.user_date.raise_()

        self.horizontalLayout_6.addWidget(self.left_child)

        self.rignt_child = QFrame(self.admin)
        self.rignt_child.setObjectName(u"rignt_child")
        self.rignt_child.setFrameShape(QFrame.NoFrame)
        self.rignt_child.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.rignt_child)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.camera_top = QFrame(self.rignt_child)
        self.camera_top.setObjectName(u"camera_top")
        self.camera_top.setFrameShape(QFrame.NoFrame)
        self.camera_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.camera_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 5, -1)
        self.admin_table = QTableWidget(self.camera_top)
        if (self.admin_table.columnCount() < 5):
            self.admin_table.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        self.admin_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        font11 = QFont()
        font11.setPointSize(10)
        font11.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font11);
        self.admin_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        self.admin_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font2);
        self.admin_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font2);
        self.admin_table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.admin_table.setObjectName(u"admin_table")
        self.admin_table.setFont(font2)
        self.admin_table.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.admin_table.setFrameShape(QFrame.NoFrame)
        self.admin_table.setFrameShadow(QFrame.Plain)
        self.admin_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_table.setSortingEnabled(True)
        self.admin_table.horizontalHeader().setDefaultSectionSize(170)
        self.admin_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.admin_table.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_8.addWidget(self.admin_table)


        self.verticalLayout_10.addWidget(self.camera_top)


        self.horizontalLayout_6.addWidget(self.rignt_child)

        self.stackedWidget.addWidget(self.admin)
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
        self.reg_image.setGeometry(QRect(30, 140, 291, 261))
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
        self.reg_firstname.setGeometry(QRect(340, 140, 291, 51))
        self.reg_firstname.setFont(font2)
        self.reg_firstname.setTabletTracking(True)
        self.reg_firstname.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_firstname.setClearButtonEnabled(True)
        self.reg_image_2 = QLabel(self.left_fram_reg)
        self.reg_image_2.setObjectName(u"reg_image_2")
        self.reg_image_2.setGeometry(QRect(10, 120, 641, 581))
        self.reg_image_2.setFont(font10)
        self.reg_image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_2.setAlignment(Qt.AlignCenter)
        self.reg_middlename = QLineEdit(self.left_fram_reg)
        self.reg_middlename.setObjectName(u"reg_middlename")
        self.reg_middlename.setGeometry(QRect(340, 210, 291, 51))
        self.reg_middlename.setFont(font2)
        self.reg_middlename.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_middlename.setClearButtonEnabled(True)
        self.reg_lastname = QLineEdit(self.left_fram_reg)
        self.reg_lastname.setObjectName(u"reg_lastname")
        self.reg_lastname.setGeometry(QRect(340, 280, 291, 51))
        self.reg_lastname.setFont(font2)
        self.reg_lastname.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_lastname.setClearButtonEnabled(True)
        self.reg_index = QLineEdit(self.left_fram_reg)
        self.reg_index.setObjectName(u"reg_index")
        self.reg_index.setGeometry(QRect(340, 420, 291, 51))
        self.reg_index.setFont(font2)
        self.reg_index.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_index.setClearButtonEnabled(True)
        self.reg_student_ref = QLineEdit(self.left_fram_reg)
        self.reg_student_ref.setObjectName(u"reg_student_ref")
        self.reg_student_ref.setGeometry(QRect(340, 350, 291, 51))
        self.reg_student_ref.setFont(font2)
        self.reg_student_ref.setStyleSheet(u"QLineEdit{\n"
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
"		border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_student_ref.setClearButtonEnabled(True)
        self.reg_nationality = QLineEdit(self.left_fram_reg)
        self.reg_nationality.setObjectName(u"reg_nationality")
        self.reg_nationality.setGeometry(QRect(30, 420, 291, 51))
        self.reg_nationality.setFont(font2)
        self.reg_nationality.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_nationality.setClearButtonEnabled(True)
        self.reg_start_date = QLineEdit(self.left_fram_reg)
        self.reg_start_date.setObjectName(u"reg_start_date")
        self.reg_start_date.setGeometry(QRect(30, 490, 201, 51))
        self.reg_start_date.setFont(font2)
        self.reg_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.reg_start_date.setReadOnly(True)
        self.reg_start_date.setClearButtonEnabled(True)
        self.reg_end_date = QLineEdit(self.left_fram_reg)
        self.reg_end_date.setObjectName(u"reg_end_date")
        self.reg_end_date.setGeometry(QRect(250, 490, 191, 51))
        self.reg_end_date.setFont(font2)
        self.reg_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
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
        self.reg_end_date.setReadOnly(True)
        self.reg_end_date.setClearButtonEnabled(True)
        self.label_35 = QLabel(self.left_fram_reg)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(40, 500, 31, 31))
        self.label_35.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.reg_programs = QComboBox(self.left_fram_reg)
        self.reg_programs.setObjectName(u"reg_programs")
        self.reg_programs.setGeometry(QRect(30, 630, 491, 50))
        self.reg_programs.setMinimumSize(QSize(0, 50))
        self.reg_programs.setMaximumSize(QSize(16777215, 50))
        self.reg_programs.setFont(font2)
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
        self.btn_search_reg.setGeometry(QRect(510, 30, 121, 50))
        self.btn_search_reg.setMinimumSize(QSize(0, 50))
        self.btn_search_reg.setFont(font2)
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
        self.btn_search_reg.setIcon(icon4)
        self.btn_search_reg.setIconSize(QSize(30, 30))
        self.btn_search_reg.setFlat(True)
        self.label_37 = QLabel(self.left_fram_reg)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 10, 641, 91))
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
        self.search_reg.setGeometry(QRect(30, 30, 461, 50))
        self.search_reg.setMinimumSize(QSize(50, 50))
        self.search_reg.setFont(font2)
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
        self.label_38.setGeometry(QRect(10, 720, 641, 81))
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
        self.btn_register.setGeometry(QRect(30, 740, 131, 41))
        self.btn_register.setFont(font2)
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
        self.btn_register.setIcon(icon3)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.btn_update = QPushButton(self.left_fram_reg)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(190, 740, 131, 41))
        self.btn_update.setFont(font2)
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
        self.btn_update.setIcon(icon20)
        self.btn_update.setIconSize(QSize(30, 30))
        self.btn_update.setFlat(True)
        self.btn_remove = QPushButton(self.left_fram_reg)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(340, 740, 131, 41))
        self.btn_remove.setFont(font2)
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
        icon26 = QIcon()
        icon26.addFile(u":/icons/asset/user-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon26)
        self.btn_remove.setIconSize(QSize(30, 30))
        self.btn_remove.setFlat(True)
        self.btn_clear = QPushButton(self.left_fram_reg)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(500, 740, 131, 41))
        self.btn_clear.setFont(font2)
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
        self.btn_clear.setIcon(icon14)
        self.btn_clear.setIconSize(QSize(30, 30))
        self.btn_clear.setFlat(True)
        self.label_39 = QLabel(self.left_fram_reg)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 880, 641, 91))
        self.label_39.setFont(font4)
        self.label_39.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.image_file_reg = QLineEdit(self.left_fram_reg)
        self.image_file_reg.setObjectName(u"image_file_reg")
        self.image_file_reg.setGeometry(QRect(30, 910, 451, 51))
        self.image_file_reg.setFont(font2)
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
        self.btn_browse_reg.setGeometry(QRect(500, 910, 131, 51))
        self.btn_browse_reg.setFont(font2)
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
        self.btn_browse_reg.setIcon(icon5)
        self.btn_browse_reg.setIconSize(QSize(30, 30))
        self.btn_browse_reg.setFlat(True)
        self.reg_college = QComboBox(self.left_fram_reg)
        self.reg_college.setObjectName(u"reg_college")
        self.reg_college.setGeometry(QRect(30, 560, 171, 50))
        self.reg_college.setMinimumSize(QSize(0, 50))
        self.reg_college.setMaximumSize(QSize(16777215, 50))
        self.reg_college.setFont(font2)
        self.reg_college.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_college.setFrame(False)
        self.label_36 = QLabel(self.left_fram_reg)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(260, 500, 31, 31))
        self.label_36.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.reg_gender = QComboBox(self.left_fram_reg)
        self.reg_gender.addItem("")
        self.reg_gender.addItem("")
        self.reg_gender.addItem("")
        self.reg_gender.setObjectName(u"reg_gender")
        self.reg_gender.setGeometry(QRect(460, 490, 171, 50))
        self.reg_gender.setMinimumSize(QSize(0, 50))
        self.reg_gender.setMaximumSize(QSize(16777215, 50))
        self.reg_gender.setFont(font2)
        self.reg_gender.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_gender.setFrame(False)
        self.reg_type = QComboBox(self.left_fram_reg)
        self.reg_type.setObjectName(u"reg_type")
        self.reg_type.setGeometry(QRect(400, 560, 231, 50))
        self.reg_type.setMinimumSize(QSize(0, 50))
        self.reg_type.setMaximumSize(QSize(16777215, 50))
        self.reg_type.setFont(font2)
        self.reg_type.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_type.setFrame(False)
        self.reg_faculty = QComboBox(self.left_fram_reg)
        self.reg_faculty.setObjectName(u"reg_faculty")
        self.reg_faculty.setGeometry(QRect(220, 560, 161, 50))
        self.reg_faculty.setMinimumSize(QSize(0, 50))
        self.reg_faculty.setMaximumSize(QSize(16777215, 50))
        self.reg_faculty.setFont(font2)
        self.reg_faculty.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_faculty.setFrame(False)
        self.reg_disability = QRadioButton(self.left_fram_reg)
        self.reg_disability.setObjectName(u"reg_disability")
        self.reg_disability.setGeometry(QRect(530, 630, 101, 50))
        self.reg_disability.setMinimumSize(QSize(0, 50))
        self.reg_disability.setMaximumSize(QSize(16777215, 20))
        self.reg_disability.setFont(font2)
        self.reg_disability.setStyleSheet(u"color: rgb(255,255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"padding-left:5px;\n"
"border-radius:7px;")
        self.reg_disability.setAutoExclusive(False)
        self.label_41 = QLabel(self.left_fram_reg)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 820, 641, 41))
        self.label_41.setFont(font7)
        self.label_41.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.file_system = QRadioButton(self.left_fram_reg)
        self.file_system.setObjectName(u"file_system")
        self.file_system.setGeometry(QRect(260, 830, 101, 20))
        self.file_system.setFont(font2)
        self.file_system.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"QRadioButton:hover{\n"
"	border-bottom:1px solid rgb(255, 255, 255);\n"
"}")
        self.file_system.setIcon(icon20)
        self.online_image = QRadioButton(self.left_fram_reg)
        self.online_image.setObjectName(u"online_image")
        self.online_image.setGeometry(QRect(40, 830, 101, 20))
        self.online_image.setFont(font2)
        self.online_image.setStyleSheet(u"\n"
"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"QRadioButton:hover{\n"
"	border-bottom:1px solid rgb(255, 255, 255);\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/icons/asset/download-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.online_image.setIcon(icon27)
        self.image_less = QRadioButton(self.left_fram_reg)
        self.image_less.setObjectName(u"image_less")
        self.image_less.setGeometry(QRect(500, 830, 141, 20))
        self.image_less.setFont(font2)
        self.image_less.setStyleSheet(u"\n"
"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"QRadioButton:hover{\n"
"	border-bottom:1px solid rgb(255, 255, 255);\n"
"}")
        self.image_less.setIcon(icon20)
        self.label_37.raise_()
        self.search_reg.raise_()
        self.reg_image_2.raise_()
        self.reg_image.raise_()
        self.reg_firstname.raise_()
        self.reg_middlename.raise_()
        self.reg_lastname.raise_()
        self.reg_index.raise_()
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
        self.reg_college.raise_()
        self.reg_end_date.raise_()
        self.label_36.raise_()
        self.reg_gender.raise_()
        self.reg_type.raise_()
        self.reg_faculty.raise_()
        self.reg_disability.raise_()
        self.label_41.raise_()
        self.file_system.raise_()
        self.online_image.raise_()
        self.image_less.raise_()

        self.horizontalLayout_14.addWidget(self.left_fram_reg)

        self.right_frame_reg = QFrame(self.database)
        self.right_frame_reg.setObjectName(u"right_frame_reg")
        self.right_frame_reg.setFrameShape(QFrame.NoFrame)
        self.right_frame_reg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.right_frame_reg)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.right_frame_reg)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 9, 2, 0)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.reg_image_3 = QLabel(self.frame_13)
        self.reg_image_3.setObjectName(u"reg_image_3")
        self.reg_image_3.setGeometry(QRect(0, 110, 761, 301))
        self.reg_image_3.setFont(font10)
        self.reg_image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_3.setAlignment(Qt.AlignCenter)
        self.label_43 = QLabel(self.frame_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, 540, 761, 91))
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_send_mail = QPushButton(self.frame_13)
        self.btn_send_mail.setObjectName(u"btn_send_mail")
        self.btn_send_mail.setGeometry(QRect(590, 560, 151, 51))
        self.btn_send_mail.setFont(font2)
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
        self.btn_send_mail.setIcon(icon25)
        self.btn_send_mail.setIconSize(QSize(30, 30))
        self.btn_send_mail.setFlat(True)
        self.reg_email = QLineEdit(self.frame_13)
        self.reg_email.setObjectName(u"reg_email")
        self.reg_email.setGeometry(QRect(20, 560, 551, 51))
        self.reg_email.setFont(font2)
        self.reg_email.setStyleSheet(u"QLineEdit{\n"
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
        self.reg_email.setClearButtonEnabled(True)
        self.label_44 = QLabel(self.frame_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(30, 570, 31, 31))
        self.label_44.setPixmap(QPixmap(u":/icons/asset/mail.svg"))
        self.generate_code_label = QLabel(self.frame_13)
        self.generate_code_label.setObjectName(u"generate_code_label")
        self.generate_code_label.setGeometry(QRect(20, 130, 290, 265))
        self.generate_code_label.setMinimumSize(QSize(290, 265))
        self.generate_code_label.setMaximumSize(QSize(290, 290))
        self.generate_code_label.setFont(font10)
        self.generate_code_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.generate_code_label.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.generate_code_label.setAlignment(Qt.AlignCenter)
        self.find_file = QLineEdit(self.frame_13)
        self.find_file.setObjectName(u"find_file")
        self.find_file.setGeometry(QRect(20, 20, 571, 51))
        self.find_file.setFont(font2)
        self.find_file.setStyleSheet(u"QLineEdit{\n"
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
        self.find_file.setClearButtonEnabled(True)
        self.btn_find_filesearch = QPushButton(self.frame_13)
        self.btn_find_filesearch.setObjectName(u"btn_find_filesearch")
        self.btn_find_filesearch.setGeometry(QRect(610, 20, 131, 51))
        self.btn_find_filesearch.setFont(font2)
        self.btn_find_filesearch.setStyleSheet(u"QPushButton{\n"
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
        self.btn_find_filesearch.setIcon(icon4)
        self.btn_find_filesearch.setIconSize(QSize(30, 30))
        self.btn_find_filesearch.setFlat(True)
        self.find_filename = QLineEdit(self.frame_13)
        self.find_filename.setObjectName(u"find_filename")
        self.find_filename.setGeometry(QRect(330, 130, 411, 51))
        self.find_filename.setFont(font2)
        self.find_filename.setStyleSheet(u"QLineEdit{\n"
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
        self.find_filename.setClearButtonEnabled(True)
        self.btn_generate_code = QPushButton(self.frame_13)
        self.btn_generate_code.setObjectName(u"btn_generate_code")
        self.btn_generate_code.setGeometry(QRect(330, 340, 201, 51))
        self.btn_generate_code.setFont(font2)
        self.btn_generate_code.setStyleSheet(u"QPushButton{\n"
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
        self.btn_generate_code.setIcon(icon5)
        self.btn_generate_code.setIconSize(QSize(30, 30))
        self.btn_generate_code.setFlat(True)
        self.find_filepath = QLineEdit(self.frame_13)
        self.find_filepath.setObjectName(u"find_filepath")
        self.find_filepath.setGeometry(QRect(330, 200, 411, 51))
        self.find_filepath.setFont(font2)
        self.find_filepath.setStyleSheet(u"QLineEdit{\n"
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
        self.find_filepath.setClearButtonEnabled(True)
        self.btn_print_code = QPushButton(self.frame_13)
        self.btn_print_code.setObjectName(u"btn_print_code")
        self.btn_print_code.setGeometry(QRect(550, 340, 191, 51))
        self.btn_print_code.setFont(font2)
        self.btn_print_code.setStyleSheet(u"QPushButton{\n"
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
        icon28 = QIcon()
        icon28.addFile(u":/icons/asset/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print_code.setIcon(icon28)
        self.btn_print_code.setIconSize(QSize(30, 30))
        self.btn_print_code.setFlat(True)
        self.label_46 = QLabel(self.frame_13)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 0, 761, 91))
        self.label_46.setFont(font7)
        self.label_46.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_size = QLineEdit(self.frame_13)
        self.image_size.setObjectName(u"image_size")
        self.image_size.setGeometry(QRect(330, 270, 411, 51))
        self.image_size.setFont(font2)
        self.image_size.setStyleSheet(u"QLineEdit{\n"
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
        self.image_size.setClearButtonEnabled(True)
        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(0, 430, 761, 91))
        self.label_47.setFont(font7)
        self.label_47.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.category_field = QLineEdit(self.frame_13)
        self.category_field.setObjectName(u"category_field")
        self.category_field.setGeometry(QRect(20, 450, 381, 50))
        self.category_field.setMinimumSize(QSize(0, 50))
        self.category_field.setMaximumSize(QSize(16777215, 45))
        self.category_field.setFont(font2)
        self.category_field.setStyleSheet(u"QLineEdit{\n"
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
        self.category_field.setClearButtonEnabled(True)
        self.btn_add_category = QPushButton(self.frame_13)
        self.btn_add_category.setObjectName(u"btn_add_category")
        self.btn_add_category.setGeometry(QRect(420, 450, 151, 51))
        self.btn_add_category.setFont(font2)
        self.btn_add_category.setStyleSheet(u"QPushButton{\n"
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
        icon29 = QIcon()
        icon29.addFile(u":/icons/asset/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_category.setIcon(icon29)
        self.btn_add_category.setIconSize(QSize(30, 30))
        self.btn_add_category.setFlat(True)
        self.btn_refresh_category = QPushButton(self.frame_13)
        self.btn_refresh_category.setObjectName(u"btn_refresh_category")
        self.btn_refresh_category.setGeometry(QRect(590, 450, 151, 51))
        self.btn_refresh_category.setFont(font2)
        self.btn_refresh_category.setStyleSheet(u"QPushButton{\n"
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
        icon30 = QIcon()
        icon30.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_category.setIcon(icon30)
        self.btn_refresh_category.setIconSize(QSize(30, 30))
        self.btn_refresh_category.setFlat(True)
        self.label_46.raise_()
        self.reg_image_3.raise_()
        self.label_43.raise_()
        self.btn_send_mail.raise_()
        self.reg_email.raise_()
        self.label_44.raise_()
        self.generate_code_label.raise_()
        self.find_file.raise_()
        self.btn_find_filesearch.raise_()
        self.find_filename.raise_()
        self.btn_generate_code.raise_()
        self.find_filepath.raise_()
        self.btn_print_code.raise_()
        self.image_size.raise_()
        self.label_47.raise_()
        self.category_field.raise_()
        self.btn_add_category.raise_()
        self.btn_refresh_category.raise_()

        self.verticalLayout_17.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 330))
        self.frame_10.setMaximumSize(QSize(16777215, 330))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setContentsMargins(0, 0, 5, 2)
        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(370, 310))
        self.frame_20.setMaximumSize(QSize(370, 310))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.email_from = QLineEdit(self.frame_20)
        self.email_from.setObjectName(u"email_from")
        self.email_from.setGeometry(QRect(20, 40, 332, 51))
        self.email_from.setMinimumSize(QSize(332, 51))
        self.email_from.setMaximumSize(QSize(332, 16777215))
        self.email_from.setFont(font2)
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
        self.email_from.setClearButtonEnabled(False)
        self.email_sender = QLineEdit(self.frame_20)
        self.email_sender.setObjectName(u"email_sender")
        self.email_sender.setGeometry(QRect(20, 180, 332, 51))
        self.email_sender.setMinimumSize(QSize(332, 51))
        self.email_sender.setMaximumSize(QSize(332, 16777215))
        self.email_sender.setFont(font2)
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
        self.email_sender.setClearButtonEnabled(False)
        self.sender_password = QLineEdit(self.frame_20)
        self.sender_password.setObjectName(u"sender_password")
        self.sender_password.setGeometry(QRect(20, 250, 332, 51))
        self.sender_password.setMinimumSize(QSize(332, 51))
        self.sender_password.setMaximumSize(QSize(332, 16777215))
        self.sender_password.setFont(font2)
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
        self.sender_password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.sender_password.setClearButtonEnabled(False)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 111, 20))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.email_subject = QLineEdit(self.frame_20)
        self.email_subject.setObjectName(u"email_subject")
        self.email_subject.setGeometry(QRect(20, 110, 332, 51))
        self.email_subject.setMinimumSize(QSize(332, 51))
        self.email_subject.setMaximumSize(QSize(332, 16777215))
        self.email_subject.setFont(font2)
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
        self.email_subject.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.frame_20, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(379, 310))
        self.frame_21.setMaximumSize(QSize(370, 310))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 9, 9, -1)
        self.change_date_box = QRadioButton(self.frame_21)
        self.change_date_box.setObjectName(u"change_date_box")
        self.change_date_box.setMinimumSize(QSize(0, 25))
        self.change_date_box.setMaximumSize(QSize(16777215, 20))
        self.change_date_box.setFont(font2)
        self.change_date_box.setStyleSheet(u"color: rgb(255,255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"padding-left:5px;\n"
"border-radius:7px;")
        self.change_date_box.setIcon(icon6)

        self.verticalLayout_21.addWidget(self.change_date_box)

        self.calendarWidget_reg = QCalendarWidget(self.frame_21)
        self.calendarWidget_reg.setObjectName(u"calendarWidget_reg")
        self.calendarWidget_reg.setGridVisible(False)
        self.calendarWidget_reg.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_reg.setNavigationBarVisible(True)

        self.verticalLayout_21.addWidget(self.calendarWidget_reg)


        self.gridLayout_3.addWidget(self.frame_21, 1, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_10)


        self.verticalLayout_15.addWidget(self.frame_11)


        self.horizontalLayout_14.addWidget(self.right_frame_reg)

        self.stackedWidget.addWidget(self.database)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_12 = QVBoxLayout(self.report)
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.report)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 980))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, 5, 11)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(335, 0))
        self.frame_8.setMaximumSize(QSize(330, 16777215))
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.report_date = QDateEdit(self.frame_8)
        self.report_date.setObjectName(u"report_date")
        self.report_date.setGeometry(QRect(10, 180, 141, 38))
        self.report_date.setMinimumSize(QSize(0, 38))
        self.report_date.setMaximumSize(QSize(16777215, 38))
        self.report_date.setFont(font8)
        self.report_date.setStyleSheet(u"QDateEdit{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border: 2px solid rgb(45, 45, 45);\n"
"padding-left:10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.report_date.setFrame(False)
        self.report_date.setReadOnly(False)
        self.report_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.report_date.setAccelerated(True)
        self.report_date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.report_date.setProperty("showGroupSeparator", False)
        self.report_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.report_date.setMinimumDate(QDate(2023, 1, 1))
        self.report_date.setCalendarPopup(True)
        self.report_date.setTimeSpec(Qt.LocalTime)
        self.report_date.setDate(QDate(2023, 1, 1))
        self.report_end_date = QLineEdit(self.frame_8)
        self.report_end_date.setObjectName(u"report_end_date")
        self.report_end_date.setGeometry(QRect(170, 130, 151, 38))
        self.report_end_date.setMinimumSize(QSize(0, 38))
        self.report_end_date.setMaximumSize(QSize(16777215, 38))
        self.report_end_date.setFont(font2)
        self.report_end_date.setTabletTracking(True)
        self.report_end_date.setStyleSheet(u"QLineEdit{\n"
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
        self.report_end_date.setReadOnly(True)
        self.report_end_date.setClearButtonEnabled(True)
        self.design_7 = QLabel(self.frame_8)
        self.design_7.setObjectName(u"design_7")
        self.design_7.setGeometry(QRect(0, 90, 331, 141))
        self.design_7.setFont(font5)
        self.design_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.report_start_date = QLineEdit(self.frame_8)
        self.report_start_date.setObjectName(u"report_start_date")
        self.report_start_date.setGeometry(QRect(10, 130, 151, 38))
        self.report_start_date.setMinimumSize(QSize(0, 38))
        self.report_start_date.setMaximumSize(QSize(16777215, 38))
        self.report_start_date.setFont(font2)
        self.report_start_date.setTabletTracking(True)
        self.report_start_date.setStyleSheet(u"QLineEdit{\n"
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
        self.report_start_date.setFrame(True)
        self.report_start_date.setReadOnly(True)
        self.report_start_date.setClearButtonEnabled(True)
        self.report_date_range = QRadioButton(self.frame_8)
        self.report_date_range.setObjectName(u"report_date_range")
        self.report_date_range.setGeometry(QRect(160, 180, 161, 38))
        self.report_date_range.setMinimumSize(QSize(0, 38))
        self.report_date_range.setMaximumSize(QSize(16777215, 38))
        self.report_date_range.setFont(font2)
        self.report_date_range.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius:5px;")
        self.report_date_range.setAutoExclusive(False)
        self.design_8 = QLabel(self.frame_8)
        self.design_8.setObjectName(u"design_8")
        self.design_8.setGeometry(QRect(0, 0, 331, 81))
        self.design_8.setFont(font5)
        self.design_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:2px;\n"
"	padding-bottom:10px;\n"
"}")
        self.design_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.chart_title = QLineEdit(self.frame_8)
        self.chart_title.setObjectName(u"chart_title")
        self.chart_title.setGeometry(QRect(10, 30, 311, 37))
        self.chart_title.setMinimumSize(QSize(0, 37))
        self.chart_title.setMaximumSize(QSize(16777215, 16777215))
        self.chart_title.setFont(font2)
        self.chart_title.setTabletTracking(True)
        self.chart_title.setStyleSheet(u"QLineEdit{\n"
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
        self.chart_title.setFrame(True)
        self.chart_title.setReadOnly(False)
        self.chart_title.setClearButtonEnabled(True)
        self.design_9 = QLabel(self.frame_8)
        self.design_9.setObjectName(u"design_9")
        self.design_9.setGeometry(QRect(0, 540, 331, 71))
        self.design_9.setFont(font5)
        self.design_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pie_chart = QRadioButton(self.frame_8)
        self.pie_chart.setObjectName(u"pie_chart")
        self.pie_chart.setGeometry(QRect(10, 580, 101, 23))
        self.pie_chart.setFont(font6)
        self.pie_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pie_chart.setChecked(False)
        self.pie_chart.setAutoExclusive(True)
        self.bar_chart = QRadioButton(self.frame_8)
        self.bar_chart.setObjectName(u"bar_chart")
        self.bar_chart.setGeometry(QRect(110, 580, 101, 23))
        self.bar_chart.setFont(font6)
        self.bar_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.bar_chart.setChecked(False)
        self.bar_chart.setAutoExclusive(True)
        self.line_graph = QRadioButton(self.frame_8)
        self.line_graph.setObjectName(u"line_graph")
        self.line_graph.setGeometry(QRect(210, 580, 111, 23))
        self.line_graph.setFont(font6)
        self.line_graph.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.line_graph.setAutoExclusive(True)
        self.design_10 = QLabel(self.frame_8)
        self.design_10.setObjectName(u"design_10")
        self.design_10.setGeometry(QRect(0, 770, 331, 91))
        self.design_10.setFont(font5)
        self.design_10.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_load = QPushButton(self.frame_8)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(10, 810, 151, 38))
        self.btn_load.setMinimumSize(QSize(0, 38))
        self.btn_load.setMaximumSize(QSize(16777215, 38))
        self.btn_load.setFont(font2)
        self.btn_load.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_load.setIcon(icon21)
        self.btn_load.setIconSize(QSize(30, 30))
        self.btn_load.setFlat(True)
        self.btn_refresh = QPushButton(self.frame_8)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(170, 810, 151, 38))
        self.btn_refresh.setMinimumSize(QSize(0, 38))
        self.btn_refresh.setMaximumSize(QSize(16777215, 38))
        self.btn_refresh.setFont(font2)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_refresh.setIcon(icon30)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.design_12 = QLabel(self.frame_8)
        self.design_12.setObjectName(u"design_12")
        self.design_12.setGeometry(QRect(0, 340, 331, 191))
        self.design_12.setFont(font5)
        self.design_12.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.design_13 = QLabel(self.frame_8)
        self.design_13.setObjectName(u"design_13")
        self.design_13.setGeometry(QRect(0, 870, 331, 91))
        self.design_13.setFont(font5)
        self.design_13.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.file_name = QLineEdit(self.frame_8)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(10, 910, 181, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy)
        self.file_name.setMinimumSize(QSize(0, 40))
        self.file_name.setMaximumSize(QSize(16777215, 40))
        self.file_name.setFont(font2)
        self.file_name.setStyleSheet(u"QLineEdit{\n"
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
        self.file_name.setClearButtonEnabled(True)
        self.btn_save = QPushButton(self.frame_8)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(200, 910, 121, 40))
        self.btn_save.setMinimumSize(QSize(0, 40))
        self.btn_save.setMaximumSize(QSize(16777215, 40))
        self.btn_save.setFont(font2)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        icon31 = QIcon()
        icon31.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon31)
        self.btn_save.setIconSize(QSize(30, 30))
        self.btn_save.setFlat(True)
        self.design_14 = QLabel(self.frame_8)
        self.design_14.setObjectName(u"design_14")
        self.design_14.setGeometry(QRect(0, 620, 331, 141))
        self.design_14.setFont(font5)
        self.design_14.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.figure_area = QLineEdit(self.frame_8)
        self.figure_area.setObjectName(u"figure_area")
        self.figure_area.setGeometry(QRect(10, 660, 91, 35))
        self.figure_area.setMinimumSize(QSize(0, 35))
        self.figure_area.setMaximumSize(QSize(16777215, 30))
        self.figure_area.setFont(font2)
        self.figure_area.setTabletTracking(True)
        self.figure_area.setStyleSheet(u"QLineEdit{\n"
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
        self.figure_area.setFrame(True)
        self.figure_area.setReadOnly(False)
        self.figure_area.setClearButtonEnabled(True)
        self.start_angle = QLineEdit(self.frame_8)
        self.start_angle.setObjectName(u"start_angle")
        self.start_angle.setGeometry(QRect(10, 710, 91, 35))
        self.start_angle.setMinimumSize(QSize(0, 35))
        self.start_angle.setMaximumSize(QSize(16777215, 30))
        self.start_angle.setFont(font2)
        self.start_angle.setTabletTracking(True)
        self.start_angle.setStyleSheet(u"QLineEdit{\n"
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
        self.start_angle.setReadOnly(False)
        self.start_angle.setClearButtonEnabled(True)
        self.query_parameter = QComboBox(self.frame_8)
        self.query_parameter.setObjectName(u"query_parameter")
        self.query_parameter.setGeometry(QRect(10, 380, 311, 37))
        self.query_parameter.setMinimumSize(QSize(0, 37))
        self.query_parameter.setMaximumSize(QSize(16777215, 35))
        self.query_parameter.setFont(font2)
        self.query_parameter.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.query_parameter.setEditable(False)
        self.query_parameter.setFrame(False)
        self.bar_width = QLineEdit(self.frame_8)
        self.bar_width.setObjectName(u"bar_width")
        self.bar_width.setGeometry(QRect(120, 660, 91, 35))
        self.bar_width.setMinimumSize(QSize(0, 35))
        self.bar_width.setMaximumSize(QSize(16777215, 35))
        self.bar_width.setFont(font2)
        self.bar_width.setTabletTracking(True)
        self.bar_width.setStyleSheet(u"QLineEdit{\n"
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
        self.bar_width.setReadOnly(False)
        self.bar_width.setClearButtonEnabled(True)
        self.dpi = QLineEdit(self.frame_8)
        self.dpi.setObjectName(u"dpi")
        self.dpi.setGeometry(QRect(230, 660, 91, 35))
        self.dpi.setMinimumSize(QSize(0, 35))
        self.dpi.setMaximumSize(QSize(16777215, 30))
        self.dpi.setFont(font2)
        self.dpi.setTabletTracking(True)
        self.dpi.setStyleSheet(u"QLineEdit{\n"
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
        self.dpi.setReadOnly(False)
        self.dpi.setClearButtonEnabled(True)
        self.pie_ldist = QLineEdit(self.frame_8)
        self.pie_ldist.setObjectName(u"pie_ldist")
        self.pie_ldist.setGeometry(QRect(120, 710, 91, 35))
        self.pie_ldist.setMinimumSize(QSize(0, 35))
        self.pie_ldist.setMaximumSize(QSize(16777215, 30))
        self.pie_ldist.setFont(font2)
        self.pie_ldist.setTabletTracking(True)
        self.pie_ldist.setStyleSheet(u"QLineEdit{\n"
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
        self.pie_ldist.setReadOnly(False)
        self.pie_ldist.setClearButtonEnabled(True)
        self.pctdist = QLineEdit(self.frame_8)
        self.pctdist.setObjectName(u"pctdist")
        self.pctdist.setGeometry(QRect(230, 710, 91, 35))
        self.pctdist.setMinimumSize(QSize(0, 35))
        self.pctdist.setMaximumSize(QSize(16777215, 30))
        self.pctdist.setFont(font2)
        self.pctdist.setTabletTracking(True)
        self.pctdist.setStyleSheet(u"QLineEdit{\n"
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
        self.pctdist.setReadOnly(False)
        self.pctdist.setClearButtonEnabled(True)
        self.report_colleges = QComboBox(self.frame_8)
        self.report_colleges.setObjectName(u"report_colleges")
        self.report_colleges.setGeometry(QRect(10, 430, 141, 37))
        self.report_colleges.setMinimumSize(QSize(0, 37))
        self.report_colleges.setMaximumSize(QSize(16777215, 30))
        self.report_colleges.setFont(font2)
        self.report_colleges.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_colleges.setEditable(False)
        self.report_colleges.setFrame(False)
        self.report_faculties = QComboBox(self.frame_8)
        self.report_faculties.setObjectName(u"report_faculties")
        self.report_faculties.setGeometry(QRect(160, 430, 161, 37))
        self.report_faculties.setMinimumSize(QSize(0, 37))
        self.report_faculties.setMaximumSize(QSize(16777215, 30))
        self.report_faculties.setFont(font2)
        self.report_faculties.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_faculties.setEditable(False)
        self.report_faculties.setFrame(False)
        self.report_departments = QComboBox(self.frame_8)
        self.report_departments.setObjectName(u"report_departments")
        self.report_departments.setGeometry(QRect(10, 480, 311, 37))
        self.report_departments.setMinimumSize(QSize(0, 37))
        self.report_departments.setMaximumSize(QSize(16777215, 30))
        self.report_departments.setFont(font2)
        self.report_departments.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_departments.setEditable(False)
        self.report_departments.setFrame(False)
        self.btn_remove_combox_item = QPushButton(self.frame_8)
        self.btn_remove_combox_item.setObjectName(u"btn_remove_combox_item")
        self.btn_remove_combox_item.setGeometry(QRect(190, 280, 131, 37))
        self.btn_remove_combox_item.setMinimumSize(QSize(0, 37))
        self.btn_remove_combox_item.setMaximumSize(QSize(16777215, 40))
        self.btn_remove_combox_item.setFont(font2)
        self.btn_remove_combox_item.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        icon32 = QIcon()
        icon32.addFile(u":/icons/asset/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_combox_item.setIcon(icon32)
        self.btn_remove_combox_item.setIconSize(QSize(30, 30))
        self.btn_remove_combox_item.setFlat(True)
        self.date_range_comboBox = QComboBox(self.frame_8)
        self.date_range_comboBox.setObjectName(u"date_range_comboBox")
        self.date_range_comboBox.setGeometry(QRect(10, 280, 171, 37))
        self.date_range_comboBox.setMinimumSize(QSize(0, 37))
        self.date_range_comboBox.setMaximumSize(QSize(16777215, 40))
        self.date_range_comboBox.setFont(font2)
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
        self.design_11 = QLabel(self.frame_8)
        self.design_11.setObjectName(u"design_11")
        self.design_11.setGeometry(QRect(0, 240, 331, 91))
        self.design_11.setFont(font5)
        self.design_11.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.design_11.raise_()
        self.design_7.raise_()
        self.report_date.raise_()
        self.report_end_date.raise_()
        self.report_start_date.raise_()
        self.report_date_range.raise_()
        self.design_8.raise_()
        self.chart_title.raise_()
        self.design_9.raise_()
        self.pie_chart.raise_()
        self.bar_chart.raise_()
        self.line_graph.raise_()
        self.design_10.raise_()
        self.btn_load.raise_()
        self.btn_refresh.raise_()
        self.design_12.raise_()
        self.design_13.raise_()
        self.file_name.raise_()
        self.btn_save.raise_()
        self.design_14.raise_()
        self.figure_area.raise_()
        self.start_angle.raise_()
        self.query_parameter.raise_()
        self.bar_width.raise_()
        self.dpi.raise_()
        self.pie_ldist.raise_()
        self.pctdist.raise_()
        self.report_colleges.raise_()
        self.report_faculties.raise_()
        self.report_departments.raise_()
        self.btn_remove_combox_item.raise_()
        self.date_range_comboBox.raise_()

        self.horizontalLayout_16.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.plot_area = QLabel(self.frame_9)
        self.plot_area.setObjectName(u"plot_area")
        self.plot_area.setMinimumSize(QSize(0, 0))
        self.plot_area.setMaximumSize(QSize(16777215, 16777215))
        self.plot_area.setFont(font6)
        self.plot_area.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.plot_area.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.plot_area)


        self.horizontalLayout_16.addWidget(self.frame_9)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.report)
        self.merge_report = QWidget()
        self.merge_report.setObjectName(u"merge_report")
        self.horizontalLayout_12 = QHBoxLayout(self.merge_report)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.merge_report)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(350, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.design_23 = QLabel(self.frame_12)
        self.design_23.setObjectName(u"design_23")
        self.design_23.setGeometry(QRect(10, 10, 331, 101))
        self.design_23.setFont(font5)
        self.design_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:2px;\n"
"	padding-bottom:10px;\n"
"}")
        self.design_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.merge_chart_title = QLineEdit(self.frame_12)
        self.merge_chart_title.setObjectName(u"merge_chart_title")
        self.merge_chart_title.setGeometry(QRect(20, 50, 311, 41))
        self.merge_chart_title.setMinimumSize(QSize(0, 37))
        self.merge_chart_title.setMaximumSize(QSize(16777215, 16777215))
        self.merge_chart_title.setFont(font2)
        self.merge_chart_title.setTabletTracking(True)
        self.merge_chart_title.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_chart_title.setFrame(True)
        self.merge_chart_title.setReadOnly(False)
        self.merge_chart_title.setClearButtonEnabled(True)
        self.report_colleges_3 = QComboBox(self.frame_12)
        self.report_colleges_3.setObjectName(u"report_colleges_3")
        self.report_colleges_3.setGeometry(QRect(20, 230, 141, 37))
        self.report_colleges_3.setMinimumSize(QSize(0, 37))
        self.report_colleges_3.setMaximumSize(QSize(16777215, 30))
        self.report_colleges_3.setFont(font2)
        self.report_colleges_3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_colleges_3.setEditable(False)
        self.report_colleges_3.setFrame(False)
        self.design_24 = QLabel(self.frame_12)
        self.design_24.setObjectName(u"design_24")
        self.design_24.setGeometry(QRect(10, 470, 331, 81))
        self.design_24.setFont(font5)
        self.design_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.merge_bar_chart = QRadioButton(self.frame_12)
        self.merge_bar_chart.setObjectName(u"merge_bar_chart")
        self.merge_bar_chart.setGeometry(QRect(120, 510, 101, 23))
        self.merge_bar_chart.setFont(font6)
        self.merge_bar_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.merge_bar_chart.setChecked(False)
        self.merge_bar_chart.setAutoExclusive(True)
        self.merge_line_graph = QRadioButton(self.frame_12)
        self.merge_line_graph.setObjectName(u"merge_line_graph")
        self.merge_line_graph.setGeometry(QRect(220, 510, 111, 23))
        self.merge_line_graph.setFont(font6)
        self.merge_line_graph.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.merge_line_graph.setAutoExclusive(True)
        self.design_25 = QLabel(self.frame_12)
        self.design_25.setObjectName(u"design_25")
        self.design_25.setGeometry(QRect(10, 130, 331, 201))
        self.design_25.setFont(font5)
        self.design_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.report_faculties_3 = QComboBox(self.frame_12)
        self.report_faculties_3.setObjectName(u"report_faculties_3")
        self.report_faculties_3.setGeometry(QRect(170, 220, 161, 40))
        self.report_faculties_3.setMinimumSize(QSize(0, 40))
        self.report_faculties_3.setMaximumSize(QSize(16777215, 40))
        self.report_faculties_3.setFont(font2)
        self.report_faculties_3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_faculties_3.setEditable(False)
        self.report_faculties_3.setFrame(False)
        self.merge_pie_chart = QRadioButton(self.frame_12)
        self.merge_pie_chart.setObjectName(u"merge_pie_chart")
        self.merge_pie_chart.setGeometry(QRect(20, 510, 101, 23))
        self.merge_pie_chart.setFont(font6)
        self.merge_pie_chart.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.merge_pie_chart.setChecked(False)
        self.merge_pie_chart.setAutoExclusive(True)
        self.report_departments_3 = QComboBox(self.frame_12)
        self.report_departments_3.setObjectName(u"report_departments_3")
        self.report_departments_3.setGeometry(QRect(20, 270, 311, 40))
        self.report_departments_3.setMinimumSize(QSize(0, 40))
        self.report_departments_3.setMaximumSize(QSize(16777215, 40))
        self.report_departments_3.setFont(font2)
        self.report_departments_3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_departments_3.setEditable(False)
        self.report_departments_3.setFrame(False)
        self.merge_query_parameter = QComboBox(self.frame_12)
        self.merge_query_parameter.setObjectName(u"merge_query_parameter")
        self.merge_query_parameter.setGeometry(QRect(20, 170, 191, 40))
        self.merge_query_parameter.setMinimumSize(QSize(0, 40))
        self.merge_query_parameter.setMaximumSize(QSize(16777215, 40))
        self.merge_query_parameter.setFont(font2)
        self.merge_query_parameter.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.merge_query_parameter.setEditable(False)
        self.merge_query_parameter.setFrame(False)
        self.report_colleges_4 = QComboBox(self.frame_12)
        self.report_colleges_4.setObjectName(u"report_colleges_4")
        self.report_colleges_4.setGeometry(QRect(20, 220, 141, 40))
        self.report_colleges_4.setMinimumSize(QSize(0, 40))
        self.report_colleges_4.setMaximumSize(QSize(16777215, 40))
        self.report_colleges_4.setFont(font2)
        self.report_colleges_4.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.report_colleges_4.setEditable(False)
        self.report_colleges_4.setFrame(False)
        self.merge_bar_width = QLineEdit(self.frame_12)
        self.merge_bar_width.setObjectName(u"merge_bar_width")
        self.merge_bar_width.setGeometry(QRect(130, 610, 91, 40))
        self.merge_bar_width.setMinimumSize(QSize(0, 40))
        self.merge_bar_width.setMaximumSize(QSize(16777215, 35))
        self.merge_bar_width.setFont(font2)
        self.merge_bar_width.setTabletTracking(True)
        self.merge_bar_width.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_bar_width.setReadOnly(False)
        self.merge_bar_width.setClearButtonEnabled(True)
        self.merge_start_angle = QLineEdit(self.frame_12)
        self.merge_start_angle.setObjectName(u"merge_start_angle")
        self.merge_start_angle.setGeometry(QRect(20, 670, 91, 40))
        self.merge_start_angle.setMinimumSize(QSize(0, 40))
        self.merge_start_angle.setMaximumSize(QSize(16777215, 30))
        self.merge_start_angle.setFont(font2)
        self.merge_start_angle.setTabletTracking(True)
        self.merge_start_angle.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_start_angle.setReadOnly(False)
        self.merge_start_angle.setClearButtonEnabled(True)
        self.design_26 = QLabel(self.frame_12)
        self.design_26.setObjectName(u"design_26")
        self.design_26.setGeometry(QRect(10, 750, 331, 101))
        self.design_26.setFont(font5)
        self.design_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.design_27 = QLabel(self.frame_12)
        self.design_27.setObjectName(u"design_27")
        self.design_27.setGeometry(QRect(10, 870, 331, 101))
        self.design_27.setFont(font5)
        self.design_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.merge_dpi = QLineEdit(self.frame_12)
        self.merge_dpi.setObjectName(u"merge_dpi")
        self.merge_dpi.setGeometry(QRect(240, 610, 91, 40))
        self.merge_dpi.setMinimumSize(QSize(0, 40))
        self.merge_dpi.setMaximumSize(QSize(16777215, 30))
        self.merge_dpi.setFont(font2)
        self.merge_dpi.setTabletTracking(True)
        self.merge_dpi.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_dpi.setReadOnly(False)
        self.merge_dpi.setClearButtonEnabled(True)
        self.btn_merge_load = QPushButton(self.frame_12)
        self.btn_merge_load.setObjectName(u"btn_merge_load")
        self.btn_merge_load.setGeometry(QRect(20, 790, 151, 40))
        self.btn_merge_load.setMinimumSize(QSize(0, 40))
        self.btn_merge_load.setMaximumSize(QSize(16777215, 38))
        self.btn_merge_load.setFont(font2)
        self.btn_merge_load.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_merge_load.setIcon(icon21)
        self.btn_merge_load.setIconSize(QSize(30, 30))
        self.btn_merge_load.setFlat(True)
        self.btn_merge_connection = QPushButton(self.frame_12)
        self.btn_merge_connection.setObjectName(u"btn_merge_connection")
        self.btn_merge_connection.setGeometry(QRect(180, 790, 151, 40))
        self.btn_merge_connection.setMinimumSize(QSize(0, 40))
        self.btn_merge_connection.setMaximumSize(QSize(16777215, 38))
        self.btn_merge_connection.setFont(font2)
        self.btn_merge_connection.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_merge_connection.setIcon(icon15)
        self.btn_merge_connection.setIconSize(QSize(30, 30))
        self.btn_merge_connection.setFlat(True)
        self.btn_merge_save = QPushButton(self.frame_12)
        self.btn_merge_save.setObjectName(u"btn_merge_save")
        self.btn_merge_save.setGeometry(QRect(210, 910, 121, 40))
        self.btn_merge_save.setMinimumSize(QSize(0, 40))
        self.btn_merge_save.setMaximumSize(QSize(16777215, 40))
        self.btn_merge_save.setFont(font2)
        self.btn_merge_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_merge_save.setIcon(icon31)
        self.btn_merge_save.setIconSize(QSize(30, 30))
        self.btn_merge_save.setFlat(True)
        self.design_28 = QLabel(self.frame_12)
        self.design_28.setObjectName(u"design_28")
        self.design_28.setGeometry(QRect(10, 570, 331, 161))
        self.design_28.setFont(font5)
        self.design_28.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.merge_pie_ldist = QLineEdit(self.frame_12)
        self.merge_pie_ldist.setObjectName(u"merge_pie_ldist")
        self.merge_pie_ldist.setGeometry(QRect(130, 670, 91, 40))
        self.merge_pie_ldist.setMinimumSize(QSize(0, 40))
        self.merge_pie_ldist.setMaximumSize(QSize(16777215, 30))
        self.merge_pie_ldist.setFont(font2)
        self.merge_pie_ldist.setTabletTracking(True)
        self.merge_pie_ldist.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_pie_ldist.setReadOnly(False)
        self.merge_pie_ldist.setClearButtonEnabled(True)
        self.merge_file_name = QLineEdit(self.frame_12)
        self.merge_file_name.setObjectName(u"merge_file_name")
        self.merge_file_name.setGeometry(QRect(20, 910, 181, 40))
        sizePolicy.setHeightForWidth(self.merge_file_name.sizePolicy().hasHeightForWidth())
        self.merge_file_name.setSizePolicy(sizePolicy)
        self.merge_file_name.setMinimumSize(QSize(0, 40))
        self.merge_file_name.setMaximumSize(QSize(16777215, 40))
        self.merge_file_name.setFont(font2)
        self.merge_file_name.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_file_name.setClearButtonEnabled(True)
        self.merge_pctdist = QLineEdit(self.frame_12)
        self.merge_pctdist.setObjectName(u"merge_pctdist")
        self.merge_pctdist.setGeometry(QRect(240, 670, 91, 40))
        self.merge_pctdist.setMinimumSize(QSize(0, 40))
        self.merge_pctdist.setMaximumSize(QSize(16777215, 30))
        self.merge_pctdist.setFont(font2)
        self.merge_pctdist.setTabletTracking(True)
        self.merge_pctdist.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_pctdist.setReadOnly(False)
        self.merge_pctdist.setClearButtonEnabled(True)
        self.merge_figure_area = QLineEdit(self.frame_12)
        self.merge_figure_area.setObjectName(u"merge_figure_area")
        self.merge_figure_area.setGeometry(QRect(20, 610, 91, 40))
        self.merge_figure_area.setMinimumSize(QSize(0, 40))
        self.merge_figure_area.setMaximumSize(QSize(16777215, 30))
        self.merge_figure_area.setFont(font2)
        self.merge_figure_area.setTabletTracking(True)
        self.merge_figure_area.setStyleSheet(u"QLineEdit{\n"
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
        self.merge_figure_area.setFrame(True)
        self.merge_figure_area.setReadOnly(False)
        self.merge_figure_area.setClearButtonEnabled(True)
        self.date_range_comboBox_3 = QComboBox(self.frame_12)
        self.date_range_comboBox_3.setObjectName(u"date_range_comboBox_3")
        self.date_range_comboBox_3.setGeometry(QRect(20, 390, 171, 37))
        self.date_range_comboBox_3.setMinimumSize(QSize(0, 37))
        self.date_range_comboBox_3.setMaximumSize(QSize(16777215, 40))
        self.date_range_comboBox_3.setFont(font2)
        self.date_range_comboBox_3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.date_range_comboBox_3.setEditable(False)
        self.date_range_comboBox_3.setFrame(False)
        self.btn_remove_combox_item_3 = QPushButton(self.frame_12)
        self.btn_remove_combox_item_3.setObjectName(u"btn_remove_combox_item_3")
        self.btn_remove_combox_item_3.setGeometry(QRect(200, 390, 131, 37))
        self.btn_remove_combox_item_3.setMinimumSize(QSize(0, 37))
        self.btn_remove_combox_item_3.setMaximumSize(QSize(16777215, 40))
        self.btn_remove_combox_item_3.setFont(font2)
        self.btn_remove_combox_item_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        self.btn_remove_combox_item_3.setIcon(icon32)
        self.btn_remove_combox_item_3.setIconSize(QSize(30, 30))
        self.btn_remove_combox_item_3.setFlat(True)
        self.design_29 = QLabel(self.frame_12)
        self.design_29.setObjectName(u"design_29")
        self.design_29.setGeometry(QRect(10, 350, 331, 101))
        self.design_29.setFont(font5)
        self.design_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.design_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_generated_data = QPushButton(self.frame_12)
        self.btn_generated_data.setObjectName(u"btn_generated_data")
        self.btn_generated_data.setGeometry(QRect(220, 170, 111, 40))
        self.btn_generated_data.setMinimumSize(QSize(0, 40))
        self.btn_generated_data.setMaximumSize(QSize(16777215, 38))
        self.btn_generated_data.setFont(font2)
        self.btn_generated_data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
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
        icon33 = QIcon()
        icon33.addFile(u":/icons/asset/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_generated_data.setIcon(icon33)
        self.btn_generated_data.setIconSize(QSize(30, 30))
        self.btn_generated_data.setFlat(True)
        self.design_29.raise_()
        self.design_28.raise_()
        self.design_23.raise_()
        self.merge_chart_title.raise_()
        self.report_colleges_3.raise_()
        self.design_24.raise_()
        self.merge_bar_chart.raise_()
        self.merge_line_graph.raise_()
        self.design_25.raise_()
        self.report_faculties_3.raise_()
        self.merge_pie_chart.raise_()
        self.report_departments_3.raise_()
        self.merge_query_parameter.raise_()
        self.report_colleges_4.raise_()
        self.merge_bar_width.raise_()
        self.merge_start_angle.raise_()
        self.design_26.raise_()
        self.design_27.raise_()
        self.merge_dpi.raise_()
        self.btn_merge_load.raise_()
        self.btn_merge_connection.raise_()
        self.btn_merge_save.raise_()
        self.merge_pie_ldist.raise_()
        self.merge_file_name.raise_()
        self.merge_pctdist.raise_()
        self.merge_figure_area.raise_()
        self.date_range_comboBox_3.raise_()
        self.btn_remove_combox_item_3.raise_()
        self.btn_generated_data.raise_()

        self.horizontalLayout_12.addWidget(self.frame_12)

        self.frame_17 = QFrame(self.merge_report)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(1089, 980))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_17)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 9, -1)
        self.merge_plot_area = QLabel(self.frame_17)
        self.merge_plot_area.setObjectName(u"merge_plot_area")
        self.merge_plot_area.setMinimumSize(QSize(0, 0))
        self.merge_plot_area.setMaximumSize(QSize(16777215, 16777215))
        self.merge_plot_area.setFont(font6)
        self.merge_plot_area.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.merge_plot_area.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.merge_plot_area)


        self.horizontalLayout_12.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.merge_report)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)

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
        self.label_6.setText(QCoreApplication.translate("dashboard", u"session@username  00:00:00 PM", None))
        self.btn_help_link.setText("")
        self.btn_login_user.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_database.setText("")
        self.btn_search.setText("")
        self.btn_batch.setText("")
        self.btn_sink_data.setText("")
        self.btn_report.setText("")
        self.btn_consolidation_report.setText("")
        self.btn_admin.setText("")
        self.btn_camera.setText("")
        self.btn_mail_report_or_data.setText("")
        self.btn_logout.setText("")
        self.image.setText("")
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.othername.setText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reference.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.college.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.last_out.setText(QCoreApplication.translate("dashboard", u"Last seen", None))
        self.image_2.setText("")
        self.last_in.setText(QCoreApplication.translate("dashboard", u"Duration", None))
        self.program.setText(QCoreApplication.translate("dashboard", u"Department", None))
        self.gender.setText(QCoreApplication.translate("dashboard", u"Gender", None))
        self.type.setText(QCoreApplication.translate("dashboard", u"Type", None))
        self.faculty.setText(QCoreApplication.translate("dashboard", u"Faculty", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
#if QT_CONFIG(shortcut)
        self.btn_connect_detect.setShortcut(QCoreApplication.translate("dashboard", u"Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.label_27.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
#if QT_CONFIG(shortcut)
        self.btn_disconnect.setShortcut(QCoreApplication.translate("dashboard", u"Shift+D", None))
#endif // QT_CONFIG(shortcut)
        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Camera", None))
        self.firstname_24.setText("")
        self.btn_open_exit_camera_ui.setText(QCoreApplication.translate("dashboard", u"Logout", None))
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_open_database.setText(QCoreApplication.translate("dashboard", u"Connection", None))
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
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.db_college.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_29.setText("")
        self.image_3.setText("")
        self.db_type.setText(QCoreApplication.translate("dashboard", u"Type", None))
        self.db_faculty.setText(QCoreApplication.translate("dashboard", u"Faculty", None))
        self.dbgender.setText(QCoreApplication.translate("dashboard", u"Gender", None))
        self.db_programe.setText(QCoreApplication.translate("dashboard", u"Department", None))
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
        self.search_page_date.setDisplayFormat(QCoreApplication.translate("dashboard", u"yyyy-MM-dd", None))
        self.db_current_session.setText(QCoreApplication.translate("dashboard", u"Students in current session", None))
        self.search_page_filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Filename here?", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"College", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Faculty", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Category", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Nationality", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Gender", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("dashboard", u"Disability", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("dashboard", u"Date", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("dashboard", u"Login", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("dashboard", u"Logout", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("dashboard", u"Duration", None));
        self.label_45.setText("")
        self.batch_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_batch_browse.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.batch_browse.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_start_job.setText(QCoreApplication.translate("dashboard", u"Insert", None))
        self.btn_batch_mail.setText(QCoreApplication.translate("dashboard", u"Mail", None))
        self.btn_batch_folder.setText(QCoreApplication.translate("dashboard", u"Images", None))
        self.btn_batch_images.setText(QCoreApplication.translate("dashboard", u"Insert", None))
        self.header_check.setText(QCoreApplication.translate("dashboard", u"File Header", None))
        ___qtablewidgetitem12 = self.tableWidget_batch.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("dashboard", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_batch.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem14 = self.tableWidget_batch.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("dashboard", u"Index", None));
        ___qtablewidgetitem15 = self.tableWidget_batch.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("dashboard", u"Naionality", None));
        ___qtablewidgetitem16 = self.tableWidget_batch.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("dashboard", u"Gender", None));
        ___qtablewidgetitem17 = self.tableWidget_batch.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("dashboard", u"Disability", None));
        ___qtablewidgetitem18 = self.tableWidget_batch.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("dashboard", u"Validity", None));
        ___qtablewidgetitem19 = self.tableWidget_batch.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("dashboard", u"College", None));
        ___qtablewidgetitem20 = self.tableWidget_batch.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("dashboard", u"Faculty", None));
        ___qtablewidgetitem21 = self.tableWidget_batch.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("dashboard", u"Department", None));
        ___qtablewidgetitem22 = self.tableWidget_batch.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("dashboard", u"Category", None));
        ___qtablewidgetitem23 = self.tableWidget_batch.horizontalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("dashboard", u"E-mail", None));
        self.design.setText(QCoreApplication.translate("dashboard", u"Facility", None))
        self.design_2.setText(QCoreApplication.translate("dashboard", u"Datasource", None))
        self.db_consolidation_range.setText(QCoreApplication.translate("dashboard", u"Switch date fields", None))
        self.db_consolidation_date.setDisplayFormat(QCoreApplication.translate("dashboard", u"yyyy-MM-dd", None))
        self.db_consolidation_start.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.db_consolidation_stop.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.db_consolidation_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.db_consolidation_partition.setPlaceholderText(QCoreApplication.translate("dashboard", u"Partition", None))
        self.btn_consolidation_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.design_4.setText(QCoreApplication.translate("dashboard", u"Pull data", None))
        self.design_5.setText(QCoreApplication.translate("dashboard", u"Merge strategy", None))
        self.btn_consolidation_partition.setText(QCoreApplication.translate("dashboard", u"Partition", None))
        self.btn_consolidation_upload.setText(QCoreApplication.translate("dashboard", u"Upload", None))
        self.design_6.setText(QCoreApplication.translate("dashboard", u"E-mail", None))
        self.db_consolidation_mail.setPlaceholderText(QCoreApplication.translate("dashboard", u"Address", None))
        self.db_consolidation_username.setPlaceholderText(QCoreApplication.translate("dashboard", u"Username", None))
        self.db_consolidation_password.setPlaceholderText(QCoreApplication.translate("dashboard", u"Password", None))
        self.db_consolidation_database.setPlaceholderText(QCoreApplication.translate("dashboard", u"Database", None))
        self.db_consolidation_hostname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Hostname", None))
        self.db_consolidation_port.setPlaceholderText(QCoreApplication.translate("dashboard", u"Port", None))
        self.btn_consolidation_test.setText(QCoreApplication.translate("dashboard", u"Test", None))
        self.db_consolidation_facility.setPlaceholderText(QCoreApplication.translate("dashboard", u"Facility name", None))
        self.db_fetch_all.setText(QCoreApplication.translate("dashboard", u"Fetch all records", None))
        self.btn_load_tables.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.btn_consolidation_update.setText(QCoreApplication.translate("dashboard", u"Update", None))
        ___qtablewidgetitem24 = self.merge_table.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("dashboard", u"College", None));
        ___qtablewidgetitem25 = self.merge_table.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("dashboard", u"Faculty", None));
        ___qtablewidgetitem26 = self.merge_table.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem27 = self.merge_table.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("dashboard", u"Category", None));
        ___qtablewidgetitem28 = self.merge_table.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("dashboard", u"Nationality", None));
        ___qtablewidgetitem29 = self.merge_table.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("dashboard", u"Gender", None));
        ___qtablewidgetitem30 = self.merge_table.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("dashboard", u"Disability", None));
        self.firstname_25.setText("")
        self.firstname_26.setText("")
        self.user_search.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_user_search.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.user_image.setText("")
        self.user_middlename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.user_lastname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.user_firstname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.user_reference.setPlaceholderText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.user_contact.setPlaceholderText(QCoreApplication.translate("dashboard", u"Contact", None))
        self.user_role.setItemText(0, QCoreApplication.translate("dashboard", u"ADMIN", None))
        self.user_role.setItemText(1, QCoreApplication.translate("dashboard", u"ANALYST", None))
        self.user_role.setItemText(2, QCoreApplication.translate("dashboard", u"USER", None))

        self.user_email.setPlaceholderText(QCoreApplication.translate("dashboard", u"example@example.com", None))
        self.firstname_27.setText("")
        self.btn_user_register.setText(QCoreApplication.translate("dashboard", u"Register", None))
        self.btn_user_update.setText(QCoreApplication.translate("dashboard", u"Update", None))
        self.btn_user_status.setText(QCoreApplication.translate("dashboard", u"Access", None))
        self.firstname_28.setText("")
        self.user_image_file.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.user_image_browse.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.firstname_29.setText("")
        self.btn_mail_user_details.setText(QCoreApplication.translate("dashboard", u"Mail", None))
        self.btn_user_clear.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.user_start_date.setDisplayFormat(QCoreApplication.translate("dashboard", u"yyyy-MM-dd", None))
        self.user_status.setItemText(0, QCoreApplication.translate("dashboard", u"ACTIVATED", None))
        self.user_status.setItemText(1, QCoreApplication.translate("dashboard", u"DEACTIVATED", None))

        self.user_range.setText(QCoreApplication.translate("dashboard", u"R", None))
        self.firstname_30.setText("")
        self.btn_export_data.setText(QCoreApplication.translate("dashboard", u"Export", None))
        self.user_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.user_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        ___qtablewidgetitem31 = self.admin_table.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("dashboard", u"Username", None));
        ___qtablewidgetitem32 = self.admin_table.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("dashboard", u"Date", None));
        ___qtablewidgetitem33 = self.admin_table.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("dashboard", u"Login", None));
        ___qtablewidgetitem34 = self.admin_table.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("dashboard", u"Logout", None));
        ___qtablewidgetitem35 = self.admin_table.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("dashboard", u"Duration", None));
        self.reg_image.setText("")
        self.reg_firstname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.reg_image_2.setText("")
        self.reg_middlename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Othername", None))
        self.reg_lastname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reg_index.setPlaceholderText(QCoreApplication.translate("dashboard", u"Index", None))
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
        self.reg_gender.setItemText(0, QCoreApplication.translate("dashboard", u"Male", None))
        self.reg_gender.setItemText(1, QCoreApplication.translate("dashboard", u"Female", None))
        self.reg_gender.setItemText(2, QCoreApplication.translate("dashboard", u"Other", None))

        self.reg_disability.setText(QCoreApplication.translate("dashboard", u"Diability", None))
        self.label_41.setText("")
        self.file_system.setText(QCoreApplication.translate("dashboard", u"System", None))
        self.online_image.setText(QCoreApplication.translate("dashboard", u"Online", None))
        self.image_less.setText(QCoreApplication.translate("dashboard", u"Image-less", None))
        self.reg_image_3.setText("")
        self.label_43.setText("")
        self.btn_send_mail.setText(QCoreApplication.translate("dashboard", u"Send mail", None))
        self.reg_email.setPlaceholderText(QCoreApplication.translate("dashboard", u"Email", None))
        self.label_44.setText("")
        self.generate_code_label.setText("")
        self.find_file.setPlaceholderText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.btn_find_filesearch.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.find_filename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Image name", None))
        self.btn_generate_code.setText(QCoreApplication.translate("dashboard", u"Generate", None))
        self.find_filepath.setPlaceholderText(QCoreApplication.translate("dashboard", u"Image path", None))
        self.btn_print_code.setText(QCoreApplication.translate("dashboard", u"Print", None))
        self.label_46.setText("")
        self.image_size.setPlaceholderText(QCoreApplication.translate("dashboard", u"Dimension", None))
        self.label_47.setText("")
        self.category_field.setPlaceholderText(QCoreApplication.translate("dashboard", u"Category", None))
        self.btn_add_category.setText(QCoreApplication.translate("dashboard", u"Add", None))
        self.btn_refresh_category.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        self.email_from.setPlaceholderText(QCoreApplication.translate("dashboard", u"From", None))
        self.email_sender.setPlaceholderText(QCoreApplication.translate("dashboard", u"Email", None))
        self.sender_password.setPlaceholderText(QCoreApplication.translate("dashboard", u"Password", None))
        self.label_9.setText(QCoreApplication.translate("dashboard", u"Sender details", None))
        self.email_subject.setPlaceholderText(QCoreApplication.translate("dashboard", u"Subject", None))
        self.change_date_box.setText(QCoreApplication.translate("dashboard", u"Switch  Between Date Fields", None))
        self.report_date.setDisplayFormat(QCoreApplication.translate("dashboard", u"yyyy-MM-dd", None))
        self.report_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.design_7.setText(QCoreApplication.translate("dashboard", u"Date", None))
        self.report_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Date", None))
        self.report_date_range.setText(QCoreApplication.translate("dashboard", u"Switch date fields", None))
        self.design_8.setText(QCoreApplication.translate("dashboard", u"Plot title", None))
        self.chart_title.setPlaceholderText(QCoreApplication.translate("dashboard", u"Title", None))
        self.design_9.setText(QCoreApplication.translate("dashboard", u"Plot types", None))
        self.pie_chart.setText(QCoreApplication.translate("dashboard", u"Piechart", None))
        self.bar_chart.setText(QCoreApplication.translate("dashboard", u"Barchart", None))
        self.line_graph.setText(QCoreApplication.translate("dashboard", u"Line Graph", None))
        self.design_10.setText(QCoreApplication.translate("dashboard", u"Operation", None))
        self.btn_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Refresh", None))
        self.design_12.setText(QCoreApplication.translate("dashboard", u"Partition", None))
        self.design_13.setText(QCoreApplication.translate("dashboard", u"Save report", None))
        self.file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.btn_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.design_14.setText(QCoreApplication.translate("dashboard", u"Figure properties", None))
        self.figure_area.setPlaceholderText(QCoreApplication.translate("dashboard", u"size", None))
        self.start_angle.setPlaceholderText(QCoreApplication.translate("dashboard", u"angle", None))
        self.bar_width.setPlaceholderText(QCoreApplication.translate("dashboard", u"width", None))
        self.dpi.setPlaceholderText(QCoreApplication.translate("dashboard", u"dpi", None))
        self.pie_ldist.setPlaceholderText(QCoreApplication.translate("dashboard", u"lbdist", None))
        self.pctdist.setPlaceholderText(QCoreApplication.translate("dashboard", u"pctdist", None))
        self.btn_remove_combox_item.setText(QCoreApplication.translate("dashboard", u"Date", None))
        self.design_11.setText(QCoreApplication.translate("dashboard", u"Plot values", None))
        self.plot_area.setText(QCoreApplication.translate("dashboard", u"Graph", None))
        self.design_23.setText(QCoreApplication.translate("dashboard", u"Plot title", None))
        self.merge_chart_title.setPlaceholderText(QCoreApplication.translate("dashboard", u"Title", None))
        self.design_24.setText(QCoreApplication.translate("dashboard", u"Plot types", None))
        self.merge_bar_chart.setText(QCoreApplication.translate("dashboard", u"Barchart", None))
        self.merge_line_graph.setText(QCoreApplication.translate("dashboard", u"Line Graph", None))
        self.design_25.setText(QCoreApplication.translate("dashboard", u"Partition", None))
        self.merge_pie_chart.setText(QCoreApplication.translate("dashboard", u"Piechart", None))
        self.merge_bar_width.setPlaceholderText(QCoreApplication.translate("dashboard", u"width", None))
        self.merge_start_angle.setPlaceholderText(QCoreApplication.translate("dashboard", u"angle", None))
        self.design_26.setText(QCoreApplication.translate("dashboard", u"Operation", None))
        self.design_27.setText(QCoreApplication.translate("dashboard", u"Save report", None))
        self.merge_dpi.setPlaceholderText(QCoreApplication.translate("dashboard", u"dpi", None))
        self.btn_merge_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.btn_merge_connection.setText(QCoreApplication.translate("dashboard", u"Connection", None))
        self.btn_merge_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.design_28.setText(QCoreApplication.translate("dashboard", u"Figure properties", None))
        self.merge_pie_ldist.setPlaceholderText(QCoreApplication.translate("dashboard", u"lbdist", None))
        self.merge_file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.merge_pctdist.setPlaceholderText(QCoreApplication.translate("dashboard", u"pctdist", None))
        self.merge_figure_area.setPlaceholderText(QCoreApplication.translate("dashboard", u"size", None))
        self.btn_remove_combox_item_3.setText(QCoreApplication.translate("dashboard", u"Date", None))
        self.design_29.setText(QCoreApplication.translate("dashboard", u"Plot values", None))
        self.btn_generated_data.setText(QCoreApplication.translate("dashboard", u"View", None))
        self.merge_plot_area.setText(QCoreApplication.translate("dashboard", u"Graph", None))
    # retranslateUi

