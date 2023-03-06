# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import asset_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(966, 625)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 600))
        self.frame.setStyleSheet(u"\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:30px;\n"
"	background-color: rgb(45, 45, 45);\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 400))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:12px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(445, 0))
        self.frame_5.setMaximumSize(QSize(300, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.label_notification = QLabel(self.frame_5)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(30, 200, 381, 51))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(26)
        font.setBold(True)
        self.label_notification.setFont(font)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.label_notification_2 = QLabel(self.frame_5)
        self.label_notification_2.setObjectName(u"label_notification_2")
        self.label_notification_2.setGeometry(QRect(30, 270, 381, 51))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_notification_2.setFont(font1)
        self.label_notification_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	\n"
"}")
        self.label_notification_2.setAlignment(Qt.AlignCenter)
        self.label_notification_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 15px;\n"
"	\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.frame_6)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(30, 250, 441, 60))
        self.username.setMinimumSize(QSize(0, 60))
        self.username.setMaximumSize(QSize(16777215, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.username.setFont(font2)
        self.username.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	background-color: rgb(35, 35, 35);\n"
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
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.username.setReadOnly(False)
        self.username.setClearButtonEnabled(True)
        self.password = QLineEdit(self.frame_6)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 390, 441, 60))
        self.password.setMinimumSize(QSize(0, 60))
        self.password.setMaximumSize(QSize(16777215, 41))
        self.password.setFont(font2)
        self.password.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	background-color: rgb(35, 35, 35);\n"
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
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setReadOnly(False)
        self.password.setClearButtonEnabled(True)
        self.btn_login = QPushButton(self.frame_6)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(30, 470, 441, 50))
        self.btn_login.setMinimumSize(QSize(0, 50))
        self.btn_login.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        self.btn_login.setFont(font3)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/icons/asset/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QSize(30, 30))
        self.btn_login.setFlat(True)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 260, 35, 41))
        self.label_3.setMinimumSize(QSize(35, 0))
        self.label_3.setMaximumSize(QSize(35, 16777215))
        self.label_3.setStyleSheet(u"	background-color: rgb(35, 35, 35);")
        self.label_3.setPixmap(QPixmap(u":/icons/asset/user.svg"))
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 400, 35, 41))
        self.label_4.setMinimumSize(QSize(35, 0))
        self.label_4.setMaximumSize(QSize(35, 16777215))
        self.label_4.setStyleSheet(u"	background-color: rgb(35, 35, 35);")
        self.label_4.setPixmap(QPixmap(u":/icons/asset/lock.svg"))
        self.btn_minimize = QPushButton(self.frame_6)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(424, 10, 17, 17))
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
        self.btn_maximize = QPushButton(self.frame_6)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(447, 10, 17, 17))
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
        self.btn_close = QPushButton(self.frame_6)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(470, 10, 17, 17))
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
        self.btn_forgot_pass = QPushButton(self.frame_6)
        self.btn_forgot_pass.setObjectName(u"btn_forgot_pass")
        self.btn_forgot_pass.setGeometry(QRect(310, 540, 161, 20))
        self.btn_forgot_pass.setMinimumSize(QSize(0, 20))
        self.btn_forgot_pass.setMaximumSize(QSize(16777215, 20))
        self.btn_forgot_pass.setFont(font2)
        self.btn_forgot_pass.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_forgot_pass.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(0, 119, 202);\n"
"}\n"
"")
        self.btn_forgot_pass.setIconSize(QSize(30, 30))
        self.btn_forgot_pass.setFlat(True)
        self.avater = QPushButton(self.frame_6)
        self.avater.setObjectName(u"avater")
        self.avater.setGeometry(QRect(190, 100, 121, 91))
        self.avater.setMinimumSize(QSize(0, 0))
        self.avater.setMaximumSize(QSize(16777215, 16777215))
        self.avater.setFont(font3)
        self.avater.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/icons/asset/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.avater.setIcon(icon1)
        self.avater.setIconSize(QSize(100, 100))
        self.avater.setCheckable(False)
        self.avater.setFlat(True)
        self.student_id = QLineEdit(self.frame_6)
        self.student_id.setObjectName(u"student_id")
        self.student_id.setGeometry(QRect(30, 320, 441, 60))
        self.student_id.setMinimumSize(QSize(0, 60))
        self.student_id.setMaximumSize(QSize(16777215, 41))
        self.student_id.setFont(font2)
        self.student_id.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	background-color: rgb(35, 35, 35);\n"
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
        self.student_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.student_id.setReadOnly(False)
        self.student_id.setClearButtonEnabled(True)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 330, 35, 41))
        self.label_5.setMinimumSize(QSize(35, 0))
        self.label_5.setMaximumSize(QSize(35, 16777215))
        self.label_5.setStyleSheet(u"	background-color: rgb(35, 35, 35);")
        self.label_5.setPixmap(QPixmap(u":/icons/asset/user.svg"))

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_notification.setText(QCoreApplication.translate("Login", u"Welcome Back!", None))
        self.label_notification_2.setText(QCoreApplication.translate("Login", u"To keep connected,please login with your credentials", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_forgot_pass.setText(QCoreApplication.translate("Login", u"Forgot Password?", None))
        self.avater.setText("")
        self.student_id.setPlaceholderText(QCoreApplication.translate("Login", u"Reference", None))
        self.label_5.setText("")
    # retranslateUi

