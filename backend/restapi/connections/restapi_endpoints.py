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
        self.ui_rest.btn_update_properties_2.clicked.connect(self.update_properties)
        self.set_database_properties()

        self.ui_rest.comboBox.activated.connect(self.get_database_properties)  
        self.ui_rest.btn_update_properties.clicked.connect(self.update_connection_properties)

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
            update['images'] = properties[1]
            with open(path,'w') as content:
                json.dump(data, content, indent=4)
            content.close()

    def database_properties_default(self,path,properties):
        with open(path,'r') as content:
            update = json.load(content) 
            update['details'] = properties[0]
            update['images'] = properties[1]
            update['endpoint'] = self.ui_rest.type.text()
            with open(path,'w') as content:
                json.dump(update, content, indent=4)
            content.close()

    def update_connection_properties(self):
        path = self.get_properties()
        key_name=self.ui_rest.comboBox.currentText()
        data_list,empty_list=self.validate_database_fields()
        if len(empty_list) == 0:
            self.connection_properties_colleges(path,key_name,data_list)
            self.ui_rest.label_notification.setText("Hey! endpoints properties updated...")
        else:
            self.ui_rest.label_notification.setText("Oops! empty  values not allowed...")

    def update_properties(self):
        path = 'C:\\ProgramData\\iAttend\\data\\properties\\students_restapi_endpoints.json'
        data_list,empty_list=self.validate_database_fields()
        properties = list(self.get_field_text())
        if len(empty_list) == 0 and self.ui_rest.type.text():
            self.database_properties_default(path,properties)
            self.ui_rest.label_notification.setText("Hey! endpoints properties updated...")
        else:
            self.ui_rest.label_notification.setText("Oops! empty  values not allowed...")   

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

    # def my_cursor(self):
    #     details = self.get_field_text()
    #     user = details[0]
    #     password = details[1]
    #     host=details[2]
    #     port=details[3]
    #     database = details[4]
    #     if self.ui_rest.API.isChecked() and self.ui_rest.details_url.text() and self.ui_rest.password.text():
    #         try:
    #             connection_status:str =("Connected to MySQL...")
    #             db=connector.connect(host=host,port=port,user=user,password=password,database=database)
    #             self.ui_rest.label_notification.setText(connection_status) 
    #             return db,db.cursor(),connection_status 
    #         except Exception as e:
    #             return str(e)
    #     else:
    #         try:
    #             connection_status:str =("Connected to SQLite3...")
    #             db = sqlite3.connect(self.get_path())
    #             self.ui_rest.label_notification.setText(connection_status)
    #             return db, db.cursor(), connection_status
    #         except Exception as e:
    #            return str(e) 

    def get_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\database\\attendance.db'     
         
    # def test_connection(self):
    #     details = self.get_field_text()
    #     user = details[0]
    #     password = details[1]
    #     host=details[2]
    #     port=details[3]
    #     database = details[4]      
    #     if self.ui_rest.mysql.isChecked():
    #         if self.ui_rest.database_name.text() and self.ui_rest.password.text():
    #             try:
    #                 db=connector.connect(host=host,port=port,user=user,password=password)
    #                 cursor = db.cursor()
    #                 cursor.execute(create_database(database))
    #                 cursor.execute(user_database(database))
    #                 cursor.execute(create_tb_students())
    #                 cursor.execute(create_tb_student_study_details())
    #                 cursor.execute(create_tb_cameras())
    #                 cursor.execute(create_tb_user_details())
    #                 cursor.execute(create_tb_user_credentials())
    #                 cursor.execute(create_tb_user_profile())
    #                 db.commit()
    #                 self.ui_rest.label_notification.setText("Hey! you have MySQL working connection...")
    #                 return db,db.cursor() 
    #             except Exception as e:
    #                 self.ui_rest.label_notification.setText(str(e))
    #                 return str(e)
    #     else: 
    #         try:
    #             db = sqlite3.connect(self.get_path())
    #             cursor = db.cursor()
    #             cursor.execute(create_tb_cameras_sqlite())
    #             cursor.execute(create_tb_user_details_sqlite())
    #             cursor.execute(create_tb_user_credentials_sqlite())
    #             cursor.execute(create_tb_user_profile_sqlite())
    #             cursor.execute(create_tb_user_sessions_sqlite())
    #             db.commit()
    #             self.ui_rest.label_notification.setText("Hey! you have SQLite3 working connection...")
    #             return db,db.cursor()
    #         except Exception as e:
    #             self.ui_rest.label_notification.setText(str(e))
    #             return str(e)
              
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
