
from packages.processing import *
from packages.system import *
from packages.pyqt import *
from packages.computing import *
from configuration.configuration import *

from alert.alert_dialog import *
from camera_4.ui_camera import Ui_Dialog



class Camera_Four(QDialog):
    def __init__(self):
        self.save_timer = QTimer()
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)

        self.ui.btn_exit_cam_connect.clicked.connect(self.start_webcam)
        self.ui.btn_exit_cam_disconect.clicked.connect(self.stop_webcam)
     
        self.ui.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui.sharpness.valueChanged.connect(self.update_sharpnesss)
        self.ui.contrast.valueChanged.connect(self.update_contrast)

        self.ui.brightness_value.setText(str(self.ui.brigthness.value()))
        self.ui.sharpness_value.setText(str(self.ui.sharpness.value()))
        self.ui.contrast_value.setText(str(self.ui.contrast.value()))

        self.ui.frame.mouseMoveEvent = self.MoveWindow
        self.configuration = Configuration()
        self.ui.frame.mouseMoveEvent = self.MoveWindow
        self.ui.comboBox.addItems(self.configuration.delegate())
        self.ui.comboBox.activated.connect(self.update_combo)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.ui.frame.setGraphicsEffect(self.shadow)

    
    def update_combo(self):
        id_index = self.ui.comboBox.currentIndex()
        url_list = self.configuration.update_comboBox()
        url=url_list[id_index]
        self.ui.exit_cam_ip.setText(url)
             
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
   
    def update_brigthness(self, value):
        self.ui.brightness_value.setText(str(value))
    
    def update_sharpnesss(self, value):
        self.ui.sharpness_value.setText(str(value))
        
    def update_contrast(self, value):
        self.ui.contrast_value.setText(str(value))


    def start_webcam(self):
        if self.ui.exit_cam_ip.text():
            self.show_alert = AlertDialog()
            self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
            self.show_alert.show()
            ip_address = self.ui.exit_cam_ip.text()
            self.network_capture = VideoCapture(ip_address)
            if ip_address:
                if self.network_capture is None or not self.network_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                    self.show_alert.show()
                else:
                    self.capture = VideoCapture(ip_address)
            
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(3)
        else:
            self.show_alert = AlertDialog()
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()
    
    def update_frame(self):
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.beta = int(self.ui.brightness_value.text())
        self.apha = int(self.ui.contrast_value.text())*0.01
        self.kernel = (int(self.ui.sharpness_value.text())*0.01, int(self.ui.sharpness_value.text())*0.01)
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.zeros(self.frame.shape, self.frame.dtype), 0, self.beta)
        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.date = datetime.now() 
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
            self.ui.camera_feeds.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_feeds.setScaledContents(True)
    
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\nrelease camera")  
        self.show_alert.show()
        self.ui.camera_feeds.setPixmap(QPixmap())
        self.ui.camera_feeds.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
    
                     

    