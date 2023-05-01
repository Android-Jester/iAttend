

from packages.pyqt import *
from utils.structure import *
from packages.computing import *
from packages.connection import *
from database.ui_database import Ui_Database

class Database(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_database = Ui_Database()
        self.ui_database.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_database.btn_close.clicked.connect(self.close)
        self.ui_database.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_database.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_database.frame.setGraphicsEffect(self.shadow)
        self.ui_database.btn_connect_test.clicked.connect(self.test_connection)
        self.ui_database.btn_connect.clicked.connect(self.my_cursor)
        self.set_database_properties()
        self.ui_database.comboBox.activated.connect(self.get_database_properties)  
        self.ui_database.btn_update_properties.clicked.connect(self.update_connection_properties)

    def get_database_properties(self):
        properties=load_database_properties(self.get_properties(),self.ui_database.comboBox.currentText())
        self.ui_database.username.setText(properties[0])
        self.ui_database.password.setText(properties[1])
        self.ui_database.hostname.setText(properties[2])
        self.ui_database.port.setText(properties[3])
        self.ui_database.database_name.setText(properties[4])

    def get_properties(self):
        return 'C:\\ProgramData\\iAttend\\data\\properties\\database_properties.json'

    def get_fields_values(self):
        username=self.ui_database.username.text()
        password=self.ui_database.password.text()
        hostname=self.ui_database.hostname.text()
        port=self.ui_database.port.text()
        database_name=self.ui_database.database_name.text()
        return username,password,hostname,port,database_name

    def validate_database_fields(self):
        properties_list =  self.get_fields_values()
        data_list = []
        empty_list = []
        for field in properties_list:
            if field:
                data_list.append(field)
            else:
                empty_list.append(field)
        return data_list,empty_list

    def connection_properties(self,path,Key_name,properties):
        with open(path,'r') as content:
            data = json.load(content) 
            index = -1
            for key in range(len(data)):
                if Key_name in data[key]:
                    index = key
                    break
            update=data[index][Key_name]
            update['username'] = properties[0]
            update['password'] = properties[1]
            update['hostname'] = properties[2]
            update['port'] = properties[3]
            update['database'] = properties[4]
            with open(path,'w') as content:
                json.dump(data, content, indent=4)
            content.close()

    def update_connection_properties(self):
        path = self.get_properties()
        key_name=self.ui_database.comboBox.currentText()
        data_list,empty_list=self.validate_database_fields()
        if len(empty_list) == 0:
            self.connection_properties(path,key_name,data_list)
            self.ui_database.label_notification.setText("Hey! database properties updated...")
        else:
            self.ui_database.label_notification.setText("Oops! empty  values not allowed...")

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path

    def set_colleges(self, colleges: list):
        self.ui_database.comboBox.addItems(colleges)

    def get_details(self):
        with open('C:\\ProgramData\\iAttend\\data\\properties\\connection_properties.json','r') as f:
            data = f.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass
    
    def set_database_properties(self):
        details = self.get_details()
        self.ui_database.username.setText(details['username'])
        self.ui_database.password.setText(details['password'])
        self.ui_database.hostname.setText(details['hostname'])
        self.ui_database.port.setText(details['port'])
        self.ui_database.database_name.setText(details['database'])
        if str(details['servername'])=='mysql':
            self.ui_database.mysql.setChecked(True)
        
    def check_state(self):
        if self.ui_database.sqlite.isChecked():
            return True
        return False

    def get_field_text(self):
        username=self.ui_database.username.text()
        password=self.ui_database.password.text()
        hostname=self.ui_database.hostname.text()
        port=self.ui_database.port.text()
        database=self.ui_database.database_name.text()
        return username,password,hostname,port,database

    def my_cursor(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]
        if self.ui_database.mysql.isChecked() and self.ui_database.database_name.text() and self.ui_database.password.text():
            try:
                connection_status:str =("Connected to MySQL...")
                db=connector.connect(host=host,port=port,user=user,password=password,database=database)
                self.ui_database.label_notification.setText(connection_status) 
                return db,db.cursor(),connection_status 
            except Exception as e:
                return str(e)
        else:
            try:
                connection_status:str =("Connected to SQLite3...")
                db = sqlite3.connect(self.get_path())
                self.ui_database.label_notification.setText(connection_status)
                return db, db.cursor(), connection_status
            except Exception as e:
               return str(e) 

    def get_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\database\\attendance.db'     
         
    def test_connection(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]      
        if self.ui_database.mysql.isChecked():
            if self.ui_database.database_name.text() and self.ui_database.password.text():
                try:
                    db=connector.connect(host=host,port=port,user=user,password=password)
                    cursor = db.cursor()
                    cursor.execute(create_database(database))
                    cursor.execute(user_database(database))
                    cursor.execute(create_tb_students())
                    cursor.execute(create_tb_student_study_details())
                    cursor.execute(create_tb_cameras())
                    cursor.execute(create_tb_user_details())
                    cursor.execute(create_tb_user_credentials())
                    cursor.execute(create_tb_user_profile())
                    db.commit()
                    self.ui_database.label_notification.setText("Hey! you have MySQL working connection...")
                    return db,db.cursor() 
                except Exception as e:
                    self.ui_database.label_notification.setText(str(e))
                    return str(e)
        else: 
            try:
                db = sqlite3.connect(self.get_path())
                cursor = db.cursor()
                cursor.execute(create_tb_cameras_sqlite())
                cursor.execute(create_tb_user_details_sqlite())
                cursor.execute(create_tb_user_credentials_sqlite())
                cursor.execute(create_tb_user_profile_sqlite())
                cursor.execute(create_tb_user_sessions_sqlite())
                db.commit()
                self.ui_database.label_notification.setText("Hey! you have SQLite3 working connection...")
                return db,db.cursor()
            except Exception as e:
                self.ui_database.label_notification.setText(str(e))
                return str(e)
              
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
