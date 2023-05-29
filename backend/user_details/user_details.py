from packages.pyqt import *
from packages.hasher import *
from packages.system import os
from packages.globals import *
from packages.connection import sqlite3
from user_details.ui_user_details import Ui_Profile

class User(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_profile = Ui_Profile()
        self.ui_profile.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_profile.btn_close.clicked.connect(self.close)
        self.ui_profile.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_profile.frame.mouseMoveEvent = self.MoveWindow 
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.move(1200, 100)
        self.ui_profile.frame.setGraphicsEffect(self.shadow)
        self.ui_profile.btn_update_profile.clicked.connect(self.update_profile_picture)
        self.ui_profile.btn_browse.clicked.connect(self.browse_image_files)
        self.ui_profile.btn_update_user.clicked.connect(self.update_username_password)

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
    
    def update_profile_picture(self):
        path=f'C:\\ProgramData\\iAttend\\data\\cache\\images\\administrators\\{self.ui_profile.reference.text()}.png'
        if self.ui_profile.update_profile.text():
            with open(self.ui_profile.update_profile.text(),'rb') as file:
                img_data=file.read()
                with open(path,'wb') as out_put:
                    out_put.write(img_data)
                out_put.close()
            file.close()
            self.ui_profile.notification.setText(f"Profile picture updated successfully,\nImage: {os.path.basename(self.ui_profile.update_profile.text())}")
        else:
             self.ui_profile.notification.setText("Oops! invalid image path.")

    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'
       
    def update_username_password(self):
        user_id = self.ui_profile.reference.text()
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        name = self.ui_profile.update_username.text()
        if self.ui_profile.update_username.text():
            cursor.execute("UPDATE tb_user_credentials SET user_username=? WHERE user_reference=?",(name,user_id))
            db.commit()
            cursor.close()
            self.ui_profile.notification.setText("Username updated successfully")
        elif self.ui_profile.update_password.text():
            hash=hash_password(self.ui_profile.update_password.text())
            cursor.execute("UPDATE tb_user_credentials SET user_password=? WHERE user_reference=?",(hash,user_id))
            db.commit()
            cursor.close()
            self.ui_profile.notification.setText("Password updated successfully")
        else:
            self.ui_profile.notification.setText("Oops! empty field not allowed,you can either update\nyour username or password but not both at the\nsame time.")
    
    def browse_image_files(self):  
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
        if path:
            self.ui_profile.update_profile.setText(path[0])
            self.profileImage(str(self.ui_profile.update_profile.text()),'')
        pass     

    def profileImage(self,filePath,path):
        if os.path.exists(filePath):
            imagePath = filePath
        else:
            imagePath = path
        imgdata = open(imagePath,'rb').read()
        pixmap =self.mask_image(imgdata)
        self.ui_profile.profile.setPixmap(pixmap)

    def setProfile(self,firstname,lastname,contact,mail,status,role,visit,last_seen,duration,reference):
        name = str(firstname).split(" ")
        self.ui_profile.firstname.setText(name[0])
        self.ui_profile.middlename.setText(name[1])
        self.ui_profile.lastname.setText(lastname)
        self.ui_profile.contact.setText(contact)
        self.ui_profile.email.setText(mail)
        self.ui_profile.status.setText(status)
        self.ui_profile.role.setText(role)
        self.ui_profile.visits_count.setText(str(visit))
        self.ui_profile.last_seen.setText(str(last_seen))
        self.ui_profile.duration.setText(str(duration))
        self.ui_profile.reference.setText(reference)
                  
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()