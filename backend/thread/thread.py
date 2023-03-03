from packages.pyqt import *

class ImageThread(QRunnable):
    def __init__(self,function):
        super(ImageThread,self).__init__()
        self.function = function

    def run(self):
        self.function()