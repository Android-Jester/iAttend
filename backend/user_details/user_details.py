from database.database import Database
from packages.hasher import *
from packages.pyqt import *
from packages.globals import *
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
        self.ui_profile.frame.setGraphicsEffect(self.shadow)
        self.database = Database()
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
        user_id=self.ui_profile.reference.text()
        check_state = self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        if self.ui_profile.update_profile.text():
            if check_state == True:
                with open(self.ui_profile.update_profile.text(), 'rb') as image_data:
                    data = image_data.read()
                my_cursor.execute("UPDATE tb_user_profile SET user_image =? WHERE user_reference=?",(data,user_id))
                db.commit()
                self.ui_profile.notification.setText("Profile picture updated successfully")
            else:
                with open(self.ui_profile.update_profile.text(), 'rb') as image_data:
                    data = image_data.read()
                my_cursor.execute("UPDATE tb_user_profile SET user_image =%s WHERE user_reference=%s",(data,user_id))
                db.commit()
                self.ui_profile.notification.setText("Profile picture updated successfully")
        else:
             self.ui_profile.notification.setText("Oops! invalid image path.")

    def update_username_password(self):
        user_id = self.ui_profile.reference.text()
        check_state = self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        name = self.ui_profile.update_username.text()
        if self.ui_profile.update_username.text():
            if check_state:
                my_cursor.execute("UPDATE tb_user_credentials SET user_username=? WHERE user_reference=?",(name,user_id))
                db.commit()
                my_cursor.close()
                self.ui_profile.notification.setText("Username updated successfully")
            else:
                my_cursor.execute("UPDATE tb_user_credentials SET user_username=%s WHERE user_reference=%s",(name,user_id))
                db.commit()
                my_cursor.close()
                self.ui_profile.notification.setText("Password updated successfully")
        elif self.ui_profile.update_password.text():
            hash=hash_password(self.ui_profile.update_password.text())
            if check_state:
                my_cursor.execute("UPDATE tb_user_credentials SET user_password=? WHERE user_reference=?",(hash,user_id))
                db.commit()
                my_cursor.close()
                self.ui_profile.notification.setText("Password updated successfully")
            else:
                my_cursor.execute("UPDATE tb_user_credentials SET user_password=%s WHERE user_reference=%s",(hash,user_id))
                db.commit()
                my_cursor.close()
                self.ui_profile.notification.setText("Password updated successfully")
        else:
            self.ui_profile.notification.setText("Oops! invalid field(s) to update")
    
    def browse_image_files(self):  
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
        if path:
            self.ui_profile.update_profile.setText(path[0])
            self.profileImage(str(self.ui_profile.update_profile.text()))
        pass     

    def profileImage(self, imgpath):
        imgdata = open(imgpath, 'rb').read()
        pixmap =self. mask_image(imgdata)
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