from packages.pyqt import *
from packages.date import *
from httplogs.ui_http_response import Ui_ServerResponse

class HTTPResponse(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_view = Ui_ServerResponse()
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
        self.ui_view.btn_clear_error_area.clicked.connect(self.ui_view.textEdit.clear)

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def set_response(self, response: str):
        time_out =current.now().time().strftime('%I:%M:%S %p')
        date_stamp=current.now().date().strftime('%d-%m-%Y')
        stamp = str(date_stamp+' '+time_out)
        self.ui_view.textEdit.append(f'\n[{stamp}]\n\t{response}')

        
