# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_details.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(499, 759)
        Profile.setMinimumSize(QSize(0, 740))
        self.verticalLayout = QVBoxLayout(Profile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(Profile)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 400))
        self.frame.setStyleSheet(u"\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:30px;\n"
"background-color: rgb(45, 45, 45);\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 400))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.profile = QLabel(self.frame_4)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(20, 50, 231, 221))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(False)
        self.profile.setFont(font)
        self.profile.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.profile.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton(self.frame_4)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(450, 10, 17, 17))
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
        self.btn_maximize = QPushButton(self.frame_4)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(427, 10, 17, 17))
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
        self.btn_minimize = QPushButton(self.frame_4)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(404, 10, 17, 17))
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
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 40, 40))
        self.label_5.setMinimumSize(QSize(40, 0))
        self.label_5.setMaximumSize(QSize(40, 16777215))
        self.label_5.setPixmap(QPixmap(u":/icons/asset/user-check.svg"))
        self.middlename = QLabel(self.frame_4)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(270, 110, 191, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.middlename.setFont(font1)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.contact = QLabel(self.frame_4)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(270, 230, 191, 41))
        self.contact.setFont(font1)
        self.contact.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.contact.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.firstname = QLabel(self.frame_4)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(270, 50, 191, 41))
        self.firstname.setFont(font1)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 350, 40, 40))
        self.label_7.setMinimumSize(QSize(40, 0))
        self.label_7.setMaximumSize(QSize(40, 16777215))
        self.label_7.setPixmap(QPixmap(u":/icons/asset/tag.svg"))
        self.role = QLabel(self.frame_4)
        self.role.setObjectName(u"role")
        self.role.setGeometry(QRect(220, 350, 91, 41))
        self.role.setFont(font1)
        self.role.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.role.setAlignment(Qt.AlignCenter)
        self.lastname = QLabel(self.frame_4)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(270, 170, 191, 41))
        self.lastname.setFont(font1)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.email = QLabel(self.frame_4)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(20, 290, 301, 41))
        self.email.setFont(font1)
        self.email.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.email.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.visits_count = QLabel(self.frame_4)
        self.visits_count.setObjectName(u"visits_count")
        self.visits_count.setGeometry(QRect(370, 350, 91, 41))
        self.visits_count.setFont(font1)
        self.visits_count.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.visits_count.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 350, 40, 40))
        self.label_8.setMinimumSize(QSize(40, 0))
        self.label_8.setMaximumSize(QSize(40, 16777215))
        self.label_8.setPixmap(QPixmap(u":/icons/asset/activity.svg"))
        self.last_seen = QLabel(self.frame_4)
        self.last_seen.setObjectName(u"last_seen")
        self.last_seen.setGeometry(QRect(20, 410, 311, 41))
        self.last_seen.setFont(font1)
        self.last_seen.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.last_seen.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.duration = QLabel(self.frame_4)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(340, 410, 121, 41))
        self.duration.setFont(font1)
        self.duration.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.duration.setAlignment(Qt.AlignCenter)
        self.status = QLabel(self.frame_4)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(20, 350, 151, 41))
        self.status.setFont(font1)
        self.status.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.status.setAlignment(Qt.AlignCenter)
        self.firstname_2 = QLabel(self.frame_4)
        self.firstname_2.setObjectName(u"firstname_2")
        self.firstname_2.setGeometry(QRect(140, 0, 191, 31))
        self.firstname_2.setFont(font1)
        self.firstname_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname_2.setAlignment(Qt.AlignCenter)
        self.update_username = QLineEdit(self.frame_4)
        self.update_username.setObjectName(u"update_username")
        self.update_username.setGeometry(QRect(20, 530, 321, 47))
        self.update_username.setMinimumSize(QSize(0, 47))
        self.update_username.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setPointSize(10)
        self.update_username.setFont(font2)
        self.update_username.setStyleSheet(u"QLineEdit{\n"
"    background-color: rgb(45,45,45);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.update_username.setClearButtonEnabled(True)
        self.update_password = QLineEdit(self.frame_4)
        self.update_password.setObjectName(u"update_password")
        self.update_password.setGeometry(QRect(20, 590, 321, 47))
        self.update_password.setMinimumSize(QSize(0, 47))
        self.update_password.setMaximumSize(QSize(16777215, 45))
        self.update_password.setFont(font2)
        self.update_password.setStyleSheet(u"QLineEdit{\n"
"    background-color: rgb(45,45,45);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.update_password.setClearButtonEnabled(True)
        self.btn_update_profile = QPushButton(self.frame_4)
        self.btn_update_profile.setObjectName(u"btn_update_profile")
        self.btn_update_profile.setGeometry(QRect(350, 530, 111, 45))
        self.btn_update_profile.setMinimumSize(QSize(0, 45))
        self.btn_update_profile.setMaximumSize(QSize(16777215, 45))
        self.btn_update_profile.setFont(font2)
        self.btn_update_profile.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/asset/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_profile.setIcon(icon)
        self.btn_update_profile.setIconSize(QSize(30, 30))
        self.btn_update_profile.setFlat(True)
        self.update_profile = QLineEdit(self.frame_4)
        self.update_profile.setObjectName(u"update_profile")
        self.update_profile.setGeometry(QRect(20, 470, 321, 45))
        self.update_profile.setMinimumSize(QSize(0, 45))
        self.update_profile.setMaximumSize(QSize(16777215, 45))
        self.update_profile.setFont(font2)
        self.update_profile.setStyleSheet(u"QLineEdit{\n"
"    background-color: rgb(45,45,45);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.update_profile.setClearButtonEnabled(True)
        self.btn_update_user = QPushButton(self.frame_4)
        self.btn_update_user.setObjectName(u"btn_update_user")
        self.btn_update_user.setGeometry(QRect(350, 590, 111, 47))
        self.btn_update_user.setMinimumSize(QSize(0, 47))
        self.btn_update_user.setFont(font2)
        self.btn_update_user.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_user.setIcon(icon1)
        self.btn_update_user.setIconSize(QSize(30, 30))
        self.btn_update_user.setFlat(True)
        self.reference = QLabel(self.frame_4)
        self.reference.setObjectName(u"reference")
        self.reference.setGeometry(QRect(330, 290, 131, 41))
        self.reference.setFont(font1)
        self.reference.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.reference.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_browse = QPushButton(self.frame_4)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setGeometry(QRect(350, 470, 111, 45))
        self.btn_browse.setMinimumSize(QSize(0, 45))
        self.btn_browse.setMaximumSize(QSize(16777215, 45))
        self.btn_browse.setFont(font2)
        self.btn_browse.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse.setIcon(icon2)
        self.btn_browse.setIconSize(QSize(30, 30))
        self.btn_browse.setFlat(True)
        self.notification = QLabel(self.frame_4)
        self.notification.setObjectName(u"notification")
        self.notification.setGeometry(QRect(20, 660, 441, 61))
        self.notification.setFont(font)
        self.notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.notification.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Dialog", None))
        self.profile.setText(QCoreApplication.translate("Profile", u"Image", None))
        self.btn_close.setText("")
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.label_5.setText("")
        self.middlename.setText(QCoreApplication.translate("Profile", u"Othername", None))
        self.contact.setText(QCoreApplication.translate("Profile", u"Contact", None))
        self.firstname.setText(QCoreApplication.translate("Profile", u"Firstname", None))
        self.label_7.setText("")
        self.role.setText(QCoreApplication.translate("Profile", u"Role", None))
        self.lastname.setText(QCoreApplication.translate("Profile", u"Lastname", None))
        self.email.setText(QCoreApplication.translate("Profile", u"example@example.com", None))
        self.visits_count.setText(QCoreApplication.translate("Profile", u"Visits", None))
        self.label_8.setText("")
        self.last_seen.setText(QCoreApplication.translate("Profile", u"Last seen", None))
        self.duration.setText(QCoreApplication.translate("Profile", u"Duration", None))
        self.status.setText(QCoreApplication.translate("Profile", u"Status", None))
        self.firstname_2.setText(QCoreApplication.translate("Profile", u"Profile", None))
        self.update_username.setPlaceholderText(QCoreApplication.translate("Profile", u"Username", None))
        self.update_password.setPlaceholderText(QCoreApplication.translate("Profile", u"Password", None))
        self.btn_update_profile.setText(QCoreApplication.translate("Profile", u"Update", None))
        self.update_profile.setPlaceholderText(QCoreApplication.translate("Profile", u"Profile image path", None))
        self.btn_update_user.setText(QCoreApplication.translate("Profile", u"Update", None))
        self.reference.setText(QCoreApplication.translate("Profile", u"Reference", None))
        self.btn_browse.setText(QCoreApplication.translate("Profile", u"Browse", None))
        self.notification.setText(QCoreApplication.translate("Profile", u"Notification", None))
    # retranslateUi

