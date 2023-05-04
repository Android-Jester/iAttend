import datetime
from packages.pyqt import *
from packages.date import *
from packages.system import *
from packages.computing import *
from alert.alert_dialog import *
from packages.processing import *
from packages.connection import *
from database.database import Database
from exit_camera.ui_exit_camera import Ui_Dialog

class ExitCameraFeed(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_exit_camera = Ui_Dialog()
        self.ui_exit_camera.setupUi(self)
        self.timer = QTimer()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_exit_camera.btn_close.clicked.connect(self.close)
        self.ui_exit_camera.btn_minimize.clicked.connect(self.showMinimized)

        self.ui_exit_camera.btn_exit_cam_connect.clicked.connect(self.start_webcam)
        self.ui_exit_camera.btn_exit_cam_connect.pressed.connect(self.connect_to_camera)
        self.ui_exit_camera.btn_exit_cam_disconect.clicked.connect(self.stop_webcam)
  
        self.ui_exit_camera.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui_exit_camera.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui_exit_camera.contrast.valueChanged.connect(self.update_contrast)

        self.ui_exit_camera.brigthness_value.setText(str(self.ui_exit_camera.brigthness.value()))
        self.ui_exit_camera.sharpness_value.setText(str(self.ui_exit_camera.sharpness.value()))
        self.ui_exit_camera.contrast_value.setText(str(self.ui_exit_camera.contrast.value()))

        self.ui_exit_camera.frame.mouseMoveEvent = self.MoveWindow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.ui_exit_camera.frame.setGraphicsEffect(self.shadow)
        self.database = Database()

    def set_combo_items(self,active_cameras:list):
        self.ui_exit_camera.exit_comboBox.addItems(active_cameras)
      
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
  
    def update_brigthness(self, value):
        self.ui_exit_camera.brigthness_value.setText(str(value))
    
    def update_sharpness(self, value):
        self.ui_exit_camera.sharpness_value.setText(str(value))
        
    def update_contrast(self, value):
        self.ui_exit_camera.contrast_value.setText(str(value))
    
    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'

    def value_formater(self,value):
        return "\'{}\'".format(value)

    def compute_duration(self,time_in: str, time_out: str):
        from datetime import date,time
        time_in = time_in.split(':')
        seconds = str(time_in[2]).split(' ')[0]
        time_in = time(hour=int(time_in[0]),minute=int(time_in[1]),second=int(seconds))
        time_out =time_out.split(':')
        seconds = str(time_out[2]).split(' ')[0]
        time_out = time(int(time_out[0]),int(time_out[1]),int(seconds))
        date_ = date(1,1,1)
        duration=current.combine(date_,time_out)-current.combine(date_,time_in)
        return str(duration)

    def query_cache_database(self,qr_code_data):
        db = sqlite3.connect(self.get_cache_path())
        my_cursor = db.cursor()
        my_cursor.execute("SELECT generated_id,student_reference FROM tb_students WHERE student_reference= " +self.value_formater(qr_code_data))
        cursor= my_cursor.fetchone()
        db.commit()
        results = []
        date="\'{}\'".format(current.now().date().strftime("%Y-%m-%d"))
        if cursor is not None:
            for data in cursor:
                results.append(data)
            cursor=my_cursor.execute("SELECT time_in,duration FROM tb_attendance_temp WHERE student_reference="+self.value_formater(results[1])+" and date_stamp="+date)
            cursor=my_cursor.fetchall()
            db.commit()
            details = []
            if cursor is not None:
                for data in cursor:
                    details.append(data)
                db.commit()
                if len(details)>0:
                    time_out =current.now().time().strftime('%H:%M:%S %p')
                    date_stamp=current.now().date().strftime('%Y-%m-%d')
                    new_duration = self.compute_duration(time_in=str(details[0][0]),time_out=time_out)
                    student_reference=self.value_formater(results[1])
                    if str(details[0][1]) == "00:00:00":
                        my_cursor.execute("UPDATE tb_attendance_temp SET time_out= ?, duration= ?  WHERE student_reference=? and date_stamp= ? ",(time_out,new_duration,student_reference,date_stamp))
                        db.commit()
                        winsound.Beep(1000,100)
                        details = my_cursor.execute("SELECT * FROM tb_attendance_temp where student_reference="+student_reference)
                        details=my_cursor.fetchone()
                        my_cursor.execute("INSERT INTO tb_attendance (student_reference,student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,date_stamp,time_in,time_out,duration) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10],time_out,new_duration))
                        db.commit()
                        my_cursor.execute("DELETE FROM tb_attendance_temp where student_reference="+student_reference)
                        my_cursor.execute("DELETE FROM tb_attendance_last_seen WHERE student_reference="+student_reference)
                        db.commit()
                        winsound.Beep(1000,100)
                        my_cursor.execute("INSERT INTO tb_attendance_last_seen (student_reference,date_stamp,time_in,time_out,duration) VALUES (?,?,?,?,?)",
                        (details[1],details[9],details[10],time_out,new_duration))
                        db.commit()
                        winsound.Beep(1000,100)
                        return "Hey! your have successfully logged out"
                    else:
                        winsound.Beep(1000,100)
                        return "Hey! your have successfully logged out"
                else:
                    return f"Oops! {qr_code_data} you are already logged out!"
        else:
             return "Oops! student details not found."

    def log_student_out(self,qr_code_data:str):
        if self.database.check_state():
            winsound.Beep(1000,100)
            return 'Oops! no database configured...'
        else:
            return self.query_cache_database(qr_code_data)

    def connect_to_camera(self):
        if self.ui_exit_camera.exit_comboBox.currentText():
            self.show_info("Connecting to selected device\nthis may take some few seconds...")
        pass
    
    def show_info(self, content:str):
        self.ui_exit_camera.label_notification.setText(content) 

    def start_webcam(self):
        if  self.ui_exit_camera.exit_cam_ip.text() or self.ui_exit_camera.exit_comboBox.currentText():
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
                self.capture = VideoCapture(camera_id)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(3)
            self.show_info("Connected to selected device\nsuccessfully...") 
        else:
            self.show_alert = AlertDialog()
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()

    def update_frame(self): 
        thickness = 2
        rect_thickness = 1
        color = (255,255,0)
        
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.beta = int(self.ui_exit_camera.brigthness_value.text())
        self.apha = int(self.ui_exit_camera.contrast_value.text())*0.01
        self.kernel = (int(self.ui_exit_camera.sharpness_value.text())*0.01, int(self.ui_exit_camera.sharpness_value.text())*0.01)
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.zeros(self.frame.shape, self.frame.dtype), 0, self.beta)
        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.date = datetime.datetime.now() 
        self.date = self.date.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.date,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)

        for qr_code in decode(self.result):
            qr_code_data  = qr_code.data.decode('utf-8')
            pts = np.array([qr_code.polygon], np.int)
            rect = np.array([qr_code.rect], np.int)
            pts = pts.reshape((-1, 1, 2)) 
            data = str(qr_code_data)
            # cv2.polylines(frame, [pts], True,color,1)
            for x,y,w,h in rect:
                w , h =x+w, y+h
                cv2.rectangle(self.result, (x,y), (w,h), color, rect_thickness)
                cv2.line(self.result,(x,y),(x+15,y),color,thickness)
                cv2.line(self.result,(x,y),(x,y+15),color,thickness)
                cv2.line(self.result,(w,y),(w-15,y),color,thickness)
                cv2.line(self.result,(w,y),(w,y+15),color,thickness)
                cv2.line(self.result,(x,h),(x+15,h),color,thickness)
                cv2.line(self.result,(x,h),(x,h-15),color,thickness)
                cv2.line(self.result,(w,h),(w-15,h),color,thickness)
                cv2.line(self.result,(w,h),(w,h-15),color,thickness)
            data_json = json.loads(data)
            info=self.log_student_out(data_json['reference'])
            self.ui_exit_camera.label_notification.setText(info)
        self.display_feed(self.result,1)          

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
        if self.timer.isActive():
            self.show_info("Disconnecting from selected device\nthis may take some few seconds...")
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui_exit_camera.camera_feeds.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui_exit_camera.camera_feeds.setScaledContents(False)
            self.timer.stop() 
            self.show_info("Disconnected from device\nsuccessfully...") 
        else:
            self.show_alert.content("Oops! you have no active camera\nto disconnect from.") 
            self.show_alert.show() 
