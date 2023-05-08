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

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_login.frame.setGraphicsEffect(self.shadow)