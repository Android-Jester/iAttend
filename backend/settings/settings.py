from packages.pyqt import *
from utils.structure import *
from packages.computing import *
from packages.connection import *
from settings.ui_settings import Ui_Settings

class Settings(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_rest = Ui_Settings()
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
        self.ui_rest.btn_update_properties.clicked.connect(self.update_endpoints_urls)
        self.ui_rest.current.toggled.connect(self.current_toggled)
        self.ui_rest.colleges.toggled.connect(self.colleges_toggled)

    def get_database_properties(self):
        properties=load_database_properties(self.get_properties(),self.ui_rest.comboBox.currentText())
        self.ui_rest.details_url.setText(properties[0])
        self.ui_rest.image_url.setText(properties[1])

    def validate_database_fields(self):
        properties_list =  self.get_field_text()
        data_list = []
        empty_list = []
        for field in properties_list:
            if field:
                data_list.append(field)
            else:
                empty_list.append(field)
        return data_list,empty_list

    def get_properties(self):
        return 'C:\\ProgramData\\iAttend\\data\\properties\\restapi_endpoints.json'

    def current_toggled(self):
        with open('C:\\ProgramData\\iAttend\\data\\properties\\students_restapi_endpoints.json','r') as file:
            data = file.read()
            try:
                details=json.loads(data)
                self.ui_rest.details_url.setText(details['details'])
            except Exception as e:
                pass
        file.close()

    def colleges_toggled(self): 
        details=load_database_properties(self.get_properties(),self.ui_rest.comboBox.currentText())
        self.ui_rest.details_url.setText(details[0])
           
    def connection_properties_colleges(self,path,Key_name,properties):
        with open(path,'r') as content:
            data = json.load(content) 
            index = -1
            for key in range(len(data)):
                if Key_name in data[key]:
                    index = key
                    break
            update=data[index][Key_name]
            update['details'] = properties[0]
            with open(path,'w') as content:
                json.dump(data, content, indent=4)
            content.close()

    def database_properties_default(self,path,properties):
        with open(path,'r') as content:
            update = json.load(content) 
            update['details'] = properties[0]
            update['endpoint'] = self.ui_rest.type.text()
            with open(path,'w') as content:
                json.dump(update, content, indent=4)
            content.close()

    def update_endpoints_urls(self):
        if self.ui_rest.colleges.isChecked():
            path = self.get_properties()
            key_name=self.ui_rest.comboBox.currentText()
            data_list,empty_list=self.validate_database_fields()
            if len(empty_list) == 0:
                try:
                    self.connection_properties_colleges(path,key_name,data_list)
                    self.ui_rest.label_notification.setText(f"Hey! {key_name} endpoints properties updated...")
                except Exception as e:
                    self.ui_rest.label_notification.setText(str(e))
            else:
                self.ui_rest.label_notification.setText("Oops! empty  values not allowed...")
        elif self.ui_rest.current.isChecked():
            path = 'C:\\ProgramData\\iAttend\\data\\properties\\students_restapi_endpoints.json'
            data_list,empty_list=self.validate_database_fields()
            properties = list(self.get_field_text())
            if len(empty_list) == 0 and self.ui_rest.type.text():
                self.database_properties_default(path,properties)
                self.ui_rest.label_notification.setText("Hey! current endpoints properties updated...")
            else:
                self.ui_rest.label_notification.setText("Oops! empty  values not allowed...") 

    def set_colleges_settings(self, colleges: list):
        self.ui_rest.comboBox.addItems(colleges)

    def get_details(self):
        with open('C:\\ProgramData\\iAttend\\data\\properties\\students_restapi_endpoints.json','r') as file:
            data = file.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass
        file.close()
    
    def set_database_properties(self):
        details = self.get_details()
        self.ui_rest.details_url.setText(details['details'])
        self.ui_rest.type.setText(details['endpoint'])
        
    def get_field_text(self):
        details=self.ui_rest.details_url.text()
        return details    
              
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
