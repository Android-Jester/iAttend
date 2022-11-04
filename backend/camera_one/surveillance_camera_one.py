import cv2
import time
import datetime
import numpy as np
import pyshine as ps
from cv2 import VideoCapture

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import (Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)   
from PySide2.QtWidgets import *

from alert.alert_dialog import *
from camera_one.ui_surveillance_cam_one import Ui_Dialog

class Surveilliance_One(QtWidgets.QDialog):
    def __init__(self):
        self.save_timer = QTimer()
        QtWidgets.QDialog.__init__(self)
        self.surveillance_one = Ui_Dialog()
        self.surveillance_one.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.surveillance_one.btn_close.clicked.connect(self.close)
        self.surveillance_one.btn_minimize.clicked.connect(self.showMinimized)

        self.surveillance_one.btn_exit_cam_connect.clicked.connect(self.start_webcam)
        self.surveillance_one.btn_exit_cam_disconect.clicked.connect(self.stop_webcam)
     
        self.surveillance_one.brigthness.valueChanged.connect(self.update_brigthness)
        self.surveillance_one.sharpness.valueChanged.connect(self.update_sharpnesss)
        self.surveillance_one.contrast.valueChanged.connect(self.update_contrast)

        self.surveillance_one.brightness_value.setText(str(self.surveillance_one.brigthness.value()))
        self.surveillance_one.sharpness_value.setText(str(self.surveillance_one.sharpness.value()))
        self.surveillance_one.contrast_value.setText(str(self.surveillance_one.contrast.value()))

        self.surveillance_one.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.surveillance_one.frame.setGraphicsEffect(self.shadow)

    def set_combo_items(self,active_cameras:list):
        self.surveillance_one.exit_comboBox.addItems(active_cameras)        
        
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            pass

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass
   
    def update_brigthness(self, value):
        self.surveillance_one.brightness_value.setText(str(value))
    
    def update_sharpnesss(self, value):
        self.surveillance_one.sharpness_value.setText(str(value))
        
    def update_contrast(self, value):
        self.surveillance_one.contrast_value.setText(str(value))

    def start_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.surveillance_one.exit_cam_ip.text()
        system_attached_camera = self.surveillance_one.exit_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)
    
    def update_frame(self):   
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.beta = int(self.surveillance_one.brightness_value.text())
        self.apha = int(self.surveillance_one.contrast_value.text())*0.01
        self.kernel = (int(self.surveillance_one.sharpness_value.text())*0.01, int(self.surveillance_one.sharpness_value.text())*0.01)
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.zeros(self.frame.shape, self.frame.dtype), 0, self.beta)
        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.date = datetime.datetime.now() 
        self.date = self.date.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.date,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.display_feed(self.result,1)
        
    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.surveillance_one.camera_feeds.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.surveillance_one.camera_feeds.setScaledContents(True)
    
    def stop_webcam(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.surveillance_one.camera_feeds.setPixmap(QPixmap())
        self.surveillance_one.camera_feeds.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
                

    