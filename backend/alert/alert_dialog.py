from packages.pyqt import *
from alert.ui_alert_dialog import Ui_AlertDialog

class AlertDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_alert = Ui_AlertDialog()
        self.ui_alert.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_alert.btn_close.clicked.connect(self.close)
        self.ui_alert.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_alert.btn_close_alert.clicked.connect(self.close)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui_alert.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_alert.frame.setGraphicsEffect(self.shadow)
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def content(self, content: str):
        return self.ui_alert.content.setText(content)