
from PySide2.QtCore import (QThread)
from PySide2.QtGui import (QImage)
from PySide2.QtCore import *
from PyQt5.QtCore import pyqtSignal
from cv2 import VideoCapture, VideoWriter, VideoWriter_fourcc, cvtColor
import cv2
path = 'C:\\Users\\BTC OMEN\\Videos\\opencv\\asamaning--45.avi'


class VideoThread(QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self) -> None:
        super().__init__()
    
    def run(self):
        self.capture = VideoCapture(0)
        while True:
            ret, frame = self.capture.read()
            if ret:
                image = cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channels = image.shape
                step = channels * width
                qImage = QImage(image.data, width, height, step, QImage.Format_RGB888)
                self.changePixmap.emit(qImage)

class Video(QThread):
    def __init__(self):
        super(Video, self).__init__()
        self.active = True
        
    def run(self):
        if self.active:
            self.fourcc = VideoWriter_fourcc(*'XVID')
            self.output = VideoWriter(path, self.fourcc, 30,(640,480))
            self.capture = VideoCapture(0)
            while self.active:
                ret, image_frame = self.capture.read()
                if ret:
                    self.output.write(image_frame)
                else:
                    pass
    def stop(self):
        self.output.release()
