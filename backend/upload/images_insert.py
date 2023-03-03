import os
from packages.pyqt import *
from utils.sql import *
from upload.ui_images import Ui_Images

class Images(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_image = Ui_Images()
        self.ui_image.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_image.btn_close.clicked.connect(self.close)
        self.ui_image.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_image.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_image.frame.setGraphicsEffect(self.shadow)
        self.ui_image.btn_batch_browse.clicked.connect(self.browse_directory)
        self.ui_image.btn_clear_area.clicked.connect(self.clear_area)

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def browse_directory(self):
        path = QFileDialog.getExistingDirectory(self,"Select images folder")
        self.ui_image.batch_browse.setText(path)
        image_count = 0
        self.ui_image.textEdit.clear()
        for item in os.listdir(path):
            image_count +=1
            os.path.join(path,item)
            self.ui_image.textEdit.append(item)
        self.ui_image.label_notification.setText("Total number of images: %d" %image_count)

    def clear_area(self):
        self.ui_image.textEdit.clear()
        self.ui_image.label_notification.setText("Notification")
        self.ui_image.batch_browse.clear()

    def directory_path(self):
        return self.ui_image.batch_browse.text()