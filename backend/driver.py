################################################################################
##
## BY: Asamani Redolf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################


import cv2
import sys
import time
from PySide2 import QtCore
from PySide2.QtCore import (QPoint,
    Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)
from PySide2.QtWidgets import *

from exit_camera.exit_camera import ExitCameraFeed
from camera_one.surveillance_camera_one import Surveilliance_One
from launcher.ui_launcher import Ui_MainWindow
from dashboard.ui_dashoboard import Ui_dashboard
from camera_one.ui_surveillance_cam_one import *
from camera_two.surveillance_camera_two import * 
from camera_three.surveillance_camera_three import * 
from camera_four.surveillance_camera_four import *

## ==> GLOBALS
GLOBAL_STATE = 0
counter = 0

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #########################################################################################

        #########################################################################################
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_camera.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        self.ui.btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
        ##########################################################################################################

        #########################################################################################
        self.open_exit_camera = ExitCameraFeed()
        self.ui.btn_open_exit_camera_ui.clicked.connect(lambda: self.open_exit_camera.show())
        ############################################################################################

        ############################################################################################
        self.open_surveillance_camera_one = Surveilliance_One()
        self.ui.btn_cast_cam_one.clicked.connect(lambda: self.open_surveillance_camera_one.show())

        self.surveillance_camera_two = Surveilliance_Two()
        self.ui.btn_cast_cam_one_2.clicked.connect(lambda: self.surveillance_camera_two.show())

        self.surveillance_camera_three = Surveilliance_Three()
        self.ui.btn_cast_cam_three.clicked.connect(lambda: self.surveillance_camera_three.show())

        self.surveillance_camera_four = Surveilliance_Four()
        self.ui.btn_cast_cam_four.clicked.connect(lambda: self.surveillance_camera_four.show())
        ############################################################################################

        ##########################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_webcam)
        self.ui.btn_disconnect.clicked.connect(self.stop_webcam)
        # self.ui.comboBox.addItems(return_active_cameras(3))
        ##########################################################################################

        ##########################################################################################
        self.ui.dilation.valueChanged.connect(self.update_dilation)
        self.ui.erosion.valueChanged.connect(self.update_erosion)
        self.ui.threshold.valueChanged.connect(self.update_threshold)
        self.ui.hsv.valueChanged.connect(self.update_hsv)
        self.ui.average_blur.valueChanged.connect(self.update_average_blurring)
        self.ui.guassian_blur.valueChanged.connect(self.update_guassian_blurring)
        self.ui.bilateral_blur.valueChanged.connect(self.update_bilateral)
        self.ui.kernel.valueChanged.connect(self.update_kernel)
        ###########################################################################################

        qtRectangle = self.frameGeometry()
        centerPoint =QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_camera.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        self.ui.btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))

        ###########################################################################################
        self.ui.btn_camera_one_connect.clicked.connect(self.start_webcam_cam_one)
        self.ui.btn_camera_one_disconnect.clicked.connect(self.stop_webcam_cam_one)
        # self.ui.camera_one_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_two_connect.clicked.connect(self.start_webcam_cam_two)
        self.ui.btn_camera_two_disconnect.clicked.connect(self.stop_webcam_cam_two)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_three_connect.clicked.connect(self.start_webcam_cam_three)
        self.ui.btn_camera_three_disconnect.clicked.connect(self.stop_webcam_cam_three)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_four_connect.clicked.connect(self.start_webcam_cam_four)
        self.ui.btn_camera_four_disconnect.clicked.connect(self.stop_webcam_cam_four)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))
        ###########################################################################################
        for w in self.ui.frame.findChildren(QPushButton):
            w.clicked.connect(self.applyStyle)

    ###############################################################################################
    def get_save_file(self):
        return self.ui.savefile_path.text()
    
    def start_recording(self):
        time.sleep(1)
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! recording in progress.")  
        self.show_alert.show()

        
        if not self.saveTimer.isActive(): 
            self.saveTimer.start()
            self.start_vidoe = Video()
            self.start_vidoe.active = True
            #self.start_vidoe.run(path,20,0)
        self.start_vidoe.start()
        pass

    def stop_recording(self):
        time.sleep(1)
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! recording stopped, file saved.")  
        self.show_alert.show()
        self.output.release()
        pass

    ###############################################################################################


    ###############################################################################
    def loadUi_file(self):
        self.ui.firstname.setText("")
        self.ui.middlename.setText("")
        self.ui.lastname.setText("")
        self.ui.refrence.setText("")
        self.ui.index.setText("")
        self.ui.coledge.setText("")
        self.ui.nationality.setText("")
        self.ui.validity.setText("")
        self.ui.program.setText("")
        self.ui.year.setText("")
        self.ui.last_in.setText("")
        self.ui.last_out.setText("")
    
    def update_dilation(self, value):
        self.ui.dilation_value.setText(str(value))
    
    def update_erosion(self, value):
        self.ui.erosion_value.setText(str(value))

    def update_threshold(self, value):
        self.ui.thresh_value.setText(str(value))

    def update_hsv(self, value):
        self.ui.hsv_value.setText(str(value))

    def update_average_blurring(self, value):
        self.ui.avg_blur_value.setText(str(value))

    def update_guassian_blurring(self, value):
        self.ui.gb_blur_value.setText(str(value))

    def update_bilateral(self, value):
        self.ui.bb_blur_value.setText(str(value))

    def update_kernel(self, value):
        self.ui.kernel_value.setText(str(value))
    
    ###############################################################################################
         ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.centralwidget)
        # self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")
    
    ##############################################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()    
    ############################################################################################# 
    def applyStyle(self):
        for w in self.ui.frame.findChildren(QPushButton):
            if w.objectName()!= self.sender().objectName():
                defaultStyle = w.styleSheet().replace("border-left:3px solid rgb(35, 35, 35) ;","")
                w.setStyleSheet(defaultStyle)
        newStytle = self.sender().styleSheet()+("border-left:3px solid rgb(255, 255, 255);")
        self.sender().setStyleSheet(newStytle)
        return

    #############################################################################################
    def start_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_ip.text()
        system_attached_camera = self.ui.comboBox.currentText()
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

        self.stop_webcam
        self.show_alert = AlertDialog() 
        self.show_alert.show()

    def update_frame(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        if self.ui.face_auth.isChecked():
            self.display_feed(self.frame,1)
        elif self.ui.qr_code_auth.isChecked():
            print("Starting QR code authentication!")
        elif self.ui.biometric_auth.isChecked():
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
            self.ui.camera_view.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.camera_view.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_view.setPixmap(QPixmap())
        self.ui.camera_view.setAlignment(Qt.AlignCenter)
        self.timer.stop()
    #############################################################################################

    #############################################################################################
    def start_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_one_id_ip.text()
        system_attached_camera = self.ui.camera_one_comboBox.currentText()
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
        self.display_feed_cam_one(self.frame,1)
        
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
            self.ui.camera_1.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_1.setScaledContents(True)
    
    def stop_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_1.setPixmap(QPixmap())
        self.ui.camera_1.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
                
    ##############################################################################################

    ##############################################################################################
    def start_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_two_id_ip.text()
        system_attached_camera = self.ui.camera_two_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_two)
        self.timer.start(3)

    def update_frame_cam_two(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_two(self.frame,2)
        
    def display_feed_cam_two(self, image, window=2):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 2:
            self.ui.camera_2.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_2.setScaledContents(True)
    
    def stop_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_2.setPixmap(QPixmap())
        self.ui.camera_2.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
    ##############################################################################################

    ##############################################################################################
    def start_webcam_cam_three(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_three_id_ip.text()
        system_attached_camera = self.ui.camera_three_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_three)
        self.timer.start(3) 
    
    def update_frame_cam_three(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_three(self.frame,window=1)
        
    def display_feed_cam_three(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_3.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_3.setScaledContents(True)
    
    def stop_webcam_cam_three(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_3.setPixmap(QPixmap())
        self.ui.camera_3.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
    #############################################################################################

    #############################################################################################
    def start_webcam_cam_four(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_four_id_ip.text()
        system_attached_camera = self.ui.camera_four_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_four)
        self.timer.start(3) 
    
    def update_frame_cam_four(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_four(self.frame,window=1)
        
    def display_feed_cam_four(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_4.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_4.setScaledContents(True)
    
    def stop_webcam_cam_four(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_4.setPixmap(QPixmap())
        self.ui.camera_4.setAlignment(Qt.AlignCenter)
        self.timer.stop()    

    #############################################################################################

class Splash_screen(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui.main.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter +=1

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Splash_screen()  
    sys.exit(application.exec_()) 