
from database.database import  *
from packages.pyqt import *
from reset.ui_password import Ui_Forgot

class ForgotPassword(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_reset = Ui_Forgot()
        self.ui_reset.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_reset.btn_close.clicked.connect(self.close)
        self.ui_reset.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_reset.btn_close.clicked.connect(self.close)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui_reset.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_reset.frame.setGraphicsEffect(self.shadow)
        self.ui_reset.btn_send.clicked.connect(self.reset)

    def reset(self):
        username = self.ui_reset.username.text()
        reference = self.ui_reset.reference.text()
        password = self.ui_reset.password.text()
        
        if reference:
            print(username, reference, password)
        pass
        
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def content(self, content: str):
        return self.ui_reset.info_label.setText(content)