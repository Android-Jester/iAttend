from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class CustomThread(QRunnable):
    def __init__(self,function):
        super(CustomThread,self).__init__()
        self.function = function

    def run(self):
        self.function()