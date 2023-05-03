from packages.pyqt import *
from utils.structure import *
from packages.computing import *
from packages.connection import *
from merge.ui_database import Ui_Database

class CentralDatabase(QDialog):
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
        self.set_database_properties()
        self.ui_database.btn_update_properties.clicked.connect(self.update_connection_properties)
        self.ui_database.btn_create_central_table.clicked.connect(self.create_table)
        self.ui_database.btn_load_tables.clicked.connect(self.load_database_tables)

    def get_properties(self):
        return 'C:\\ProgramData\\iAttend\\data\\properties\\central_database_connection_propeties.json'

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

    def connection_properties(self,path,properties):
        with open(path,'r') as content:
            update = json.load(content) 
            update['username'] = properties[0]
            update['password'] = properties[1]
            update['hostname'] = properties[2]
            update['port'] = properties[3]
            update['database'] = properties[4]
            with open(path,'w') as content:
                json.dump(update, content, indent=4)
            content.close()

    def update_connection_properties(self):
        path = self.get_properties()
        data_list,empty_list=self.validate_database_fields()
        if len(empty_list) == 0:
            self.connection_properties(path,data_list)
            self.ui_database.label_notification.setText("Hey! database properties updated...")
        else:
            self.ui_database.label_notification.setText("Oops! empty  values not allowed...")

    def get_details(self):
        with open('C:\\ProgramData\\iAttend\\data\\properties\\central_database_connection_propeties.json','r') as f:
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
        
    def get_field_text(self):
        username=self.ui_database.username.text()
        password=self.ui_database.password.text()
        hostname=self.ui_database.hostname.text()
        port=self.ui_database.port.text()
        database=self.ui_database.database_name.text()
        return username,password,hostname,port,database

    def create_table(self):
        table_name = self.ui_database.central_tablenam.text()
        if table_name:
            try:
                sql= f"""
                    CREATE TABLE IF NOT EXISTS {table_name}(
                        generated_id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        student_college varchar(20) NOT NULL,
                        student_faculty varchar(25) NOT NULL,
                        student_program varchar(255) NOT NULL,
                        student_category varchar(255) NOT NULL,
                        student_nationality varchar(80) NOT NULL,
                        student_gender varchar(15) NOT NULL,
                        student_disability varchar(5) NOT NULL,
                        facility_used varchar(30)
                        )
                    """
                db,cursor=self.merge_cursor()
                cursor.execute(sql)
                db.commit()
                db.close()
                cursor.close()
                self.ui_database.label_notification.setText("Hey! table created successfully...")
            except Exception as e:
                 self.ui_database.label_notification.setText(str(e))
        else:
            self.ui_database.label_notification.setText("Oops! provide valid table name...")

    def load_database_tables(self):
        try:
            db,cursor=self.merge_cursor()
            cursor=db.cursor()
            cursor.execute("SHOW TABLES")
            results = cursor.fetchall()
            tables = []
            for row in results:
                tables.append(row[0])
            self.ui_database.database_tables.clear()
            self.ui_database.database_tables.addItems(tables)
        except Exception as e:
            self.ui_database.label_notification.setText(str(e))
          
    def merge_cursor(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]
        try:
            db=connector.connect(host=host,port=port,user=user,password=password,database=database)
            cursor = db.cursor()
            return db,cursor 
        except Exception as e:
            return str(e)

    def get_table_name(self):
        return self.ui_database.database_tables.currentText()

    def test_connection(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]      
        try:
            db=connector.connect(host=host,port=port,user=user,password=password,database=database)
            self.ui_database.label_notification.setText("Hey! you have MySQL working connection...")
            cursor = db.cursor()
            cursor.execute("SHOW TABLES")
            results = cursor.fetchall()
            tables = []
            for row in results:
                tables.append(row[0])
            self.ui_database.database_tables.clear()
            self.ui_database.database_tables.addItems(tables)
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
