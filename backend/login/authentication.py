from packages.pyqt import *
from login.ui_login import Ui_Login

class Authentication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.avater.setDisabled(True)
        # self.ui_alert.frame.mouseMoveEvent = self.MoveWindow

        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(230, 230, 230, 50))
        # self.ui_alert.frame.setGraphicsEffect(self.shadow)
    
    # def MoveWindow(self, event):
    #     if self.isMaximized() == False:
    #         self.move(self.pos() + event.globalPos() - self.clickPosition)
    #         self.clickPosition = event.globalPos()
    #         event.accept()

    # def mousePressEvent(self, event):
    #     self.clickPosition = event.globalPos()

    # def content(self, content: str):
    #     return self.ui_alert.content.setText(content)