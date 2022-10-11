import cv2
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import (Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)
from PySide2.QtWidgets import *
from cv2 import VideoCapture

from alert.alert_dialog import *
from exit_camera.ui_exit_camera import Ui_Dialog

class ExitCameraFeed(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_exit_camera = Ui_Dialog()
        self.ui_exit_camera.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_exit_camera.btn_close.clicked.connect(self.close)
        self.ui_exit_camera.btn_minimize.clicked.connect(self.showMinimized)

        ##########################################################################################
        # self.ui_exit_camera.exit_comboBox.addItems([str(x) for x in return_active_cameras(3)])
        self.ui_exit_camera.btn_exit_cam_connect.clicked.connect(self.start_webcam)
        self.ui_exit_camera.btn_exit_cam_disconect.clicked.connect(self.stop_webcam)
        ##########################################################################################

        ############################################################################################
        self.ui_exit_camera.dilation.valueChanged.connect(self.update_dilation)
        self.ui_exit_camera.erosion.valueChanged.connect(self.update_erosion)
        self.ui_exit_camera.hsv.valueChanged.connect(self.update_hsv)
        self.ui_exit_camera.blur.valueChanged.connect(self.update_average_blurring)
        ###########################################################################################

        self.ui_exit_camera.frame.mouseMoveEvent = self.MoveWindow

        ##########################################################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.ui_exit_camera.frame.setGraphicsEffect(self.shadow)
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
        self.ui_exit_camera.dilation_value.setText(str(value))
    
    def update_erosion(self, value):
        self.ui_exit_camera.erosion_value.setText(str(value))
        
    def update_hsv(self, value):
        self.ui_exit_camera.hsv_value.setText(str(value))

    def update_average_blurring(self, value):
        self.ui_exit_camera.blur_value.setText(str(value))
    ###################################################################################
 #############################################################################################
    def start_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui_exit_camera.exit_cam_ip.text()
        system_attached_camera = self.ui_exit_camera.exit_comboBox.currentText()
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

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)

    def create_alert(self):
        self.stop_webcam
        self.show_alert = AlertDialog() 
        self.show_alert.show()

    def update_frame(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        if self.ui_exit_camera.face_auth.isChecked():
            self.display_feed(self.frame,1)
        elif self.ui_exit_camera.qr_code_auth.isChecked():
            print("Starting QR code authentication!")
        elif self.ui_exit_camera.biometric_auth.isChecked():
            print("Starting biometric authentication!")

    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui_exit_camera.camera_feeds.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui_exit_camera.camera_feeds.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui_exit_camera.camera_feeds.setPixmap(QPixmap())
        self.ui_exit_camera.camera_feeds.setAlignment(Qt.AlignCenter)
        self.timer.stop()
    #############################################################################################