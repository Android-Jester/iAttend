from packages.pyqt import *
from utils.sql import *
from data.ui_data_view import Ui_DataView

class DataView(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_view = Ui_DataView()
        self.ui_view.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_view.btn_close.clicked.connect(self.close)
        self.ui_view.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_view.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_view.frame.setGraphicsEffect(self.shadow)

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def set_data(self,data:list):
        self.ui_view.textEdit.clear()
        self.ui_view.textEdit.append(data)

        
