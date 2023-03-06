# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_out.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        if not CameraWindow.objectName():
            CameraWindow.setObjectName(u"CameraWindow")
        CameraWindow.resize(1098, 880)
        CameraWindow.setMinimumSize(QSize(1098, 819))
        self.centralwidget = QWidget(CameraWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/asset/video.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
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

        self.btn_minimize = QPushButton(self.frame_2)
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

        self.btn_maximize = QPushButton(self.frame_2)
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

        self.btn_close = QPushButton(self.frame_2)
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


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.camera_view = QFrame(self.frame_3)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.camera_view.setFrameShape(QFrame.StyledPanel)
        self.camera_view.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.camera_view)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"\n"
"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:5px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btn_exit_cam_connect = QPushButton(self.frame_5)
        self.btn_exit_cam_connect.setObjectName(u"btn_exit_cam_connect")
        self.btn_exit_cam_connect.setGeometry(QRect(20, 110, 141, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_exit_cam_connect.setFont(font1)
        self.btn_exit_cam_connect.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_cam_connect.setIcon(icon)
        self.btn_exit_cam_connect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_connect.setFlat(True)
        self.btn_exit_cam_disconect = QPushButton(self.frame_5)
        self.btn_exit_cam_disconect.setObjectName(u"btn_exit_cam_disconect")
        self.btn_exit_cam_disconect.setGeometry(QRect(170, 110, 151, 41))
        self.btn_exit_cam_disconect.setFont(font1)
        self.btn_exit_cam_disconect.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_cam_disconect.setIcon(icon1)
        self.btn_exit_cam_disconect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_disconect.setFlat(True)
        self.exit_comboBox = QComboBox(self.frame_5)
        self.exit_comboBox.addItem("")
        self.exit_comboBox.setObjectName(u"exit_comboBox")
        self.exit_comboBox.setGeometry(QRect(330, 110, 181, 38))
        self.exit_comboBox.setMinimumSize(QSize(0, 38))
        self.exit_comboBox.setMaximumSize(QSize(16777215, 38))
        self.exit_comboBox.setFont(font1)
        self.exit_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(45,45,45);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.exit_comboBox.setFrame(False)
        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(30, 50, 41, 31))
        self.label_28.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.firstname_24 = QLabel(self.frame_5)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(10, 10, 511, 161))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.firstname_24.setFont(font2)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_exit_cam_ip = QLineEdit(self.frame_5)
        self.btn_exit_cam_ip.setObjectName(u"btn_exit_cam_ip")
        self.btn_exit_cam_ip.setGeometry(QRect(20, 40, 491, 51))
        self.btn_exit_cam_ip.setFont(font1)
        self.btn_exit_cam_ip.setStyleSheet(u"QLineEdit{\n"
"    background-color: rgb(45,45,45);\n"
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
        self.btn_exit_cam_ip.setClearButtonEnabled(True)
        self.firstname_24.raise_()
        self.btn_exit_cam_connect.raise_()
        self.btn_exit_cam_disconect.raise_()
        self.exit_comboBox.raise_()
        self.btn_exit_cam_ip.raise_()
        self.label_28.raise_()

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(520, 16777215))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius:5px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_6)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_14)

        self.entry_dilation_label = QLabel(self.frame_6)
        self.entry_dilation_label.setObjectName(u"entry_dilation_label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.entry_dilation_label.setFont(font3)
        self.entry_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_dilation_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.entry_dilation_label)

        self.dilation = QSlider(self.frame_6)
        self.dilation.setObjectName(u"dilation")
        self.dilation.setMaximum(500)
        self.dilation.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dilation)

        self.entry_erosion_label = QLabel(self.frame_6)
        self.entry_erosion_label.setObjectName(u"entry_erosion_label")
        self.entry_erosion_label.setFont(font3)
        self.entry_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_erosion_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.entry_erosion_label)

        self.erosion = QSlider(self.frame_6)
        self.erosion.setObjectName(u"erosion")
        self.erosion.setMaximum(500)
        self.erosion.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.erosion)

        self.entry_blur_label = QLabel(self.frame_6)
        self.entry_blur_label.setObjectName(u"entry_blur_label")
        self.entry_blur_label.setFont(font3)
        self.entry_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_blur_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.entry_blur_label)

        self.blur = QSlider(self.frame_6)
        self.blur.setObjectName(u"blur")
        self.blur.setMaximum(500)
        self.blur.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.blur)

        self.entry_unimp_label = QLabel(self.frame_6)
        self.entry_unimp_label.setObjectName(u"entry_unimp_label")
        self.entry_unimp_label.setFont(font3)
        self.entry_unimp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_unimp_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.entry_unimp_label)

        self.horizontalSlider_4 = QSlider(self.frame_6)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setMaximum(500)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.horizontalSlider_4)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        CameraWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CameraWindow)

        QMetaObject.connectSlotsByName(CameraWindow)
    # setupUi

    def retranslateUi(self, CameraWindow):
        CameraWindow.setWindowTitle(QCoreApplication.translate("CameraWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_exit_cam_connect.setText(QCoreApplication.translate("CameraWindow", u"Connect", None))
        self.btn_exit_cam_disconect.setText(QCoreApplication.translate("CameraWindow", u"Disconnect", None))
        self.exit_comboBox.setItemText(0, QCoreApplication.translate("CameraWindow", u"New Item", None))

        self.label_28.setText("")
        self.firstname_24.setText(QCoreApplication.translate("CameraWindow", u"Exit camera", None))
        self.btn_exit_cam_ip.setPlaceholderText(QCoreApplication.translate("CameraWindow", u"Camera Id/IP ?", None))
        self.label_14.setText(QCoreApplication.translate("CameraWindow", u"Entry camera image processing enhancement", None))
        self.entry_dilation_label.setText(QCoreApplication.translate("CameraWindow", u"Dilation", None))
#if QT_CONFIG(tooltip)
        self.dilation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.entry_erosion_label.setText(QCoreApplication.translate("CameraWindow", u"Erosion", None))
        self.entry_blur_label.setText(QCoreApplication.translate("CameraWindow", u"Blur", None))
        self.entry_unimp_label.setText(QCoreApplication.translate("CameraWindow", u"Blur", None))
    # retranslateUi

