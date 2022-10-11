import cv2
from cv2 import VideoCapture

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import (Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage) 
from PySide2.QtWidgets import *

from alert.alert_dialog import *
from camera_two.ui_surveillance_cam_two import Ui_Dialog

class Surveilliance_Two(QtWidgets.QDialog):
    def __init__(self):
        self.save_timer = QTimer()
        QtWidgets.QDialog.__init__(self)
        self.surveillance_two = Ui_Dialog()
        self.surveillance_two.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.surveillance_two.btn_close.clicked.connect(self.close)
        self.surveillance_two.btn_minimize.clicked.connect(self.showMinimized)

        ###################################################################################
        self.surveillance_two.btn_exit_cam_connect.clicked.connect(self.start_webcam_cam_one)
        self.surveillance_two.btn_exit_cam_disconect.clicked.connect(self.stop_webcam_cam_one)
        # self.surveillance_two.exit_comboBox.addItems(return_active_cameras(3)) 
        ###################################################################################

        ############################################################################################
        self.surveillance_two.dilation.valueChanged.connect(self.update_dilation)
        self.surveillance_two.erosion.valueChanged.connect(self.update_erosion)
        self.surveillance_two.hsv.valueChanged.connect(self.update_hsv)
        self.surveillance_two.blur.valueChanged.connect(self.update_average_blurring)
        ###########################################################################################

        self.surveillance_two.frame.mouseMoveEvent = self.MoveWindow

        ##########################################################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.surveillance_two.frame.setGraphicsEffect(self.shadow)
        ##########################################################################################
        
    #################################################################################
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            pass

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass
    ###################################################################################

    ###################################################################################
    def update_dilation(self, value):
        self.surveillance_two.dilation_value.setText(str(value))
    
    def update_erosion(self, value):
        self.surveillance_two.erosion_value.setText(str(value))
        
    def update_hsv(self, value):
        self.surveillance_two.hsv_value.setText(str(value))

    def update_average_blurring(self, value):
        self.surveillance_two.blur_value.setText(str(value))
    ###################################################################################


    ####################################################################################
    def start_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.surveillance_two.exit_cam_ip.text()
        system_attached_camera = self.surveillance_two.exit_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_one)
        self.timer.start(3) 
    
    def update_frame_cam_one(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_one(self.frame,window=1)
        
    def display_feed_cam_one(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.surveillance_two.camera_feeds.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.surveillance_two.camera_feeds.setScaledContents(True)
    
    def stop_webcam_cam_one(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.surveillance_two.camera_feeds.setPixmap(QPixmap())
        self.surveillance_two.camera_feeds.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
                
    ####################################################################################

    