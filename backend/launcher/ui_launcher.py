# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcherdJsZEh.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 190, 991, 91))
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(40)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 114, 255);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 260, 991, 21))
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(14)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.main)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 570, 991, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{	\n"
"	background-color: rgb(98, 114, 164);\n"
"	border-style:none;\n"
"	text-align:center;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, 	y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"i<strong>Vision", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Your secuirity, Our concern!</p></body></html>", None))
    # retranslateUi

