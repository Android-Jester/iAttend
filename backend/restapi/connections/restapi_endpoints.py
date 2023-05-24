from packages.pyqt import *
from utils.structure import *
from packages.computing import *
from packages.connection import *
from restapi.connections.ui_restapi_endpoints import Ui_RESTAPI

class RESTAPI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_rest = Ui_RESTAPI()
        self.ui_rest.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_rest.btn_close.clicked.connect(self.close)
        self.ui_rest.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_rest.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_rest.frame.setGraphicsEffect(self.shadow)
        self.set_database_properties()
        self.ui_rest.comboBox.activated.connect(self.get_database_properties)  

    def get_database_properties(self):
        properties=load_database_properties(self.get_properties(),self.ui_rest.comboBox.currentText())
        self.ui_rest.details_url.setText(properties[0])
        self.ui_rest.image_url.setText(properties[1])

    def get_properties(self):
        return 'C:\\ProgramData\\iAttend\\data\\properties\\restapi_endpoints.json'

    def set_colleges(self, colleges: list):
        self.ui_rest.comboBox.addItems(colleges)

    def get_details(self):
        with open('C:\\ProgramData\\iAttend\\data\\properties\\students_restapi_endpoints.json','r') as f:
            data = f.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass
    
    def set_database_properties(self):
        details = self.get_details()
        self.ui_rest.details_url.setText(details['details'])
        self.ui_rest.image_url.setText(details['images'])
        self.ui_rest.type.setText(details['endpoint'])
        if str(details['endpoint'])=='RESTAPI':
            self.ui_rest.API.setChecked(True)
        
    def check_state(self):
        if self.ui_rest.sqlite.isChecked():
            return True
        return False

    def get_field_text(self):
        details=self.ui_rest.details_url.text()
        images=self.ui_rest.image_url.text()
        return details,images    
              
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
