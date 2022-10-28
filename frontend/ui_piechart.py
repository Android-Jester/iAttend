# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'piechart.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1098, 872)
        Dialog.setMinimumSize(QSize(1098, 819))
        Dialog.setMaximumSize(QSize(1098, 880))
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
        self.label.setPixmap(QPixmap(u":/icons/asset/pie-chart.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
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
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.plot = QFrame(self.frame_4)
        self.plot.setObjectName(u"plot")
        self.plot.setMinimumSize(QSize(0, 400))
        self.plot.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.plot.setFrameShape(QFrame.NoFrame)
        self.plot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.plot)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.plot_area = QVBoxLayout()
        self.plot_area.setObjectName(u"plot_area")

        self.verticalLayout_5.addLayout(self.plot_area)


        self.verticalLayout_3.addWidget(self.plot)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 10, 421, 181))
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
        self.calendarWidget_report.setNavigationBarVisible(True)

        self.verticalLayout_16.addWidget(self.calendarWidget_report)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(870, 20, 31, 31))
        self.label_20.setStyleSheet(u"background-color:rgb(45, 45, 45);")
        self.label_20.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.file_name = QLineEdit(self.frame_5)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(860, 10, 211, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.file_name.setFont(font1)
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
        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(450, 20, 31, 31))
        self.label_23.setStyleSheet(u"background-color:rgb(45, 45, 45);")
        self.label_23.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.report_start_date = QLineEdit(self.frame_5)
        self.report_start_date.setObjectName(u"report_start_date")
        self.report_start_date.setGeometry(QRect(440, 10, 201, 51))
        self.report_start_date.setFont(font1)
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
        self.report_end_date = QLineEdit(self.frame_5)
        self.report_end_date.setObjectName(u"report_end_date")
        self.report_end_date.setGeometry(QRect(650, 10, 201, 51))
        self.report_end_date.setFont(font1)
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
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(660, 20, 31, 31))
        self.label_21.setStyleSheet(u"background-color:rgb(45, 45, 45);")
        self.label_21.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.btn_load = QPushButton(self.frame_5)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(690, 80, 121, 41))
        self.btn_load.setFont(font1)
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
        icon = QIcon()
        icon.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load.setIcon(icon)
        self.btn_load.setIconSize(QSize(30, 30))
        self.btn_load.setFlat(True)
        self.btn_save = QPushButton(self.frame_5)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(820, 80, 121, 41))
        self.btn_save.setFont(font1)
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QSize(30, 30))
        self.btn_save.setFlat(True)
        self.btn_refresh = QPushButton(self.frame_5)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(950, 80, 121, 41))
        self.btn_refresh.setFont(font1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.date_frame = QFrame(self.frame_5)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setGeometry(QRect(440, 80, 241, 43))
        self.date_frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.date_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.start_date_3 = QRadioButton(self.date_frame)
        self.start_date_3.setObjectName(u"start_date_3")
        self.start_date_3.setFont(font)
        self.start_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.start_date_3.setChecked(True)

        self.horizontalLayout_11.addWidget(self.start_date_3)

        self.end_date_3 = QRadioButton(self.date_frame)
        self.end_date_3.setObjectName(u"end_date_3")
        self.end_date_3.setFont(font)
        self.end_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.end_date_3)

        self.college_courses = QComboBox(self.frame_5)
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.setObjectName(u"college_courses")
        self.college_courses.setGeometry(QRect(700, 140, 371, 50))
        self.college_courses.setMinimumSize(QSize(0, 50))
        self.college_courses.setMaximumSize(QSize(16777215, 50))
        self.college_courses.setFont(font1)
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
        self.college_comboBox = QComboBox(self.frame_5)
        self.college_comboBox.addItem("")
        self.college_comboBox.addItem("")
        self.college_comboBox.addItem("")
        self.college_comboBox.setObjectName(u"college_comboBox")
        self.college_comboBox.setGeometry(QRect(440, 140, 221, 50))
        self.college_comboBox.setMinimumSize(QSize(0, 50))
        self.college_comboBox.setMaximumSize(QSize(16777215, 50))
        self.college_comboBox.setFont(font1)
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
        self.file_name.raise_()
        self.report_start_date.raise_()
        self.frame_12.raise_()
        self.label_20.raise_()
        self.label_23.raise_()
        self.report_end_date.raise_()
        self.label_21.raise_()
        self.btn_load.raise_()
        self.btn_save.raise_()
        self.btn_refresh.raise_()
        self.date_frame.raise_()
        self.college_courses.raise_()
        self.college_comboBox.raise_()

        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Piechart", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.label_20.setText("")
        self.file_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"File name?", None))
        self.label_23.setText("")
        self.report_start_date.setPlaceholderText(QCoreApplication.translate("Dialog", u"Start date?", None))
        self.report_end_date.setPlaceholderText(QCoreApplication.translate("Dialog", u"End date?", None))
        self.label_21.setText("")
        self.btn_load.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.btn_refresh.setText(QCoreApplication.translate("Dialog", u"Reload", None))
        self.start_date_3.setText(QCoreApplication.translate("Dialog", u"Start Date", None))
        self.end_date_3.setText(QCoreApplication.translate("Dialog", u"End Date", None))
        self.college_courses.setItemText(0, QCoreApplication.translate("Dialog", u"BSc. Computer Science", None))
        self.college_courses.setItemText(1, QCoreApplication.translate("Dialog", u"BSc. Mathematics", None))
        self.college_courses.setItemText(2, QCoreApplication.translate("Dialog", u"BSc. Chemistry", None))
        self.college_courses.setItemText(3, QCoreApplication.translate("Dialog", u"BSc. Biology Science", None))

        self.college_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"CoS", None))
        self.college_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"CoE", None))
        self.college_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"HESSA", None))

    # retranslateUi

