

from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import (QColor)
from user_details.ui_user_details import Ui_Profile
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class User(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_profile = Ui_Profile()
        self.ui_profile.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_profile.btn_close.clicked.connect(self.close)
        self.ui_profile.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_profile.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_profile.frame.setGraphicsEffect(self.shadow)
        self.setProfile()

    def mask_image(self,imgdata, imgtype ='jpeg', size = 220):
        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)
        imgsize = min(image.width(), image.height())
        rect = QRect((image.width() - imgsize) / 2,(image.height() - imgsize) / 2,imgsize,imgsize,)
        image = image.copy(rect)
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)
        brush = QBrush(image)
        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio,Qt.SmoothTransformation)
        return pm
    

    def profileImage(self, imgpath):
        imgdata = open(imgpath, 'rb').read()
        pixmap =self. mask_image(imgdata)
        self.ui_profile.profile.setPixmap(pixmap)

    def profileInfo(self):
        pass

    def setProfile(self):
        self.profileImage("D:\\Targets\\Commons\\test_code\\images\\redolf.png")
        self.ui_profile.firstname.setText("Asamaning")
        self.ui_profile.lastname.setText("Redolf")
        self.ui_profile.contact.setText("+233552588647")
        self.ui_profile.email.setText("redolfkendrick@gmail.com")
        self.ui_profile.visits.setText("")
        self.ui_profile.middlename.setText("")
        self.ui_profile.awards.setText("2")
        self.ui_profile.role.setText("ADMIN")
        self.ui_profile.visits_count.setText("20")
        self.ui_profile.last_seen.setText("Thur 23 Feb 2023@11:23:45 AM")
        self.ui_profile.duration.setText("2:45:34")
        self.ui_profile.program.setText("BSc. Computer Science")
             
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()