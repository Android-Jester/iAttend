from database.database import Database
from packages.hasher import *
from packages.pyqt import *
from packages.globals import *
from restapi.user_profile.ui_user_profile import Ui_Profile

class Profile(QDialog):
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