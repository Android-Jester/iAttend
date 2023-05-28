
from packages.pyqt import *
from packages.connection import sqlite3

from configuration.ui_camera_config import *
class Configuration(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_cofig = Ui_Configuration()
        self.ui_cofig.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_cofig.btn_close.clicked.connect(self.close)
        self.ui_cofig.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_cofig.btn_close.clicked.connect(self.close)
        self.ui_cofig.frame.mouseMoveEvent = self.MoveWindow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_cofig.frame.setGraphicsEffect(self.shadow)

        self.ui_cofig.btn_insert.clicked.connect(self.insert_camera_details)
        self.ui_cofig.btn_update.clicked.connect(self.update_camera_details)
        self.ui_cofig.btn_delete.clicked.connect(self.delete_camera)
        self.ui_cofig.btn_search.clicked.connect(self.search)

        camera = QCompleter(self.query_database("SELECT camera_id FROM tb_cameras"))
        camera.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui_cofig.camera_reference.setCompleter(camera)

    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'

    def delegate(self):
        return self.query_database("SELECT camera_id FROM tb_cameras ORDER BY camera_id ASC")

    def update_comboBox(self):
        return self.query_database("SELECT camera_url FROM tb_cameras ORDER BY camera_id ASC")
    
    def search(self):
        camera = "\'{}\'".format(self.ui_cofig.camera_reference.text())
        if self.ui_cofig.camera_reference.text():
            result=self.query_database("SELECT camera_url FROM tb_cameras WHERE camera_id="+camera)
            if result:
                self.ui_cofig.camera_ip.setText(result[0])
            else:
                self.ui_cofig.label_notification.setText("Oops! no data found for\nCamera Id: %s" %camera)
        else:
            self.ui_cofig.label_notification.setText("Search cannot be empty\nCamera Id: %s" %camera)
     
    def query_database(self, query: str):
        db = sqlite3.connect(self.get_cache_path())
        my_cursor = db.cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item[0])
        return details

    def value_formater(self,value):
        return "\'{}\'".format(value)

    def insert_camera_details(self):
        db = sqlite3.connect(self.get_cache_path())
        my_cursor = db.cursor()
        camera_reference = self.value_formater(self.ui_cofig.camera_reference.text())
        camera_reference=camera_reference.strip() 
        camera_url = self.ui_cofig.camera_ip.text()
        camera_url=camera_url.strip()
        checker=self.query_database(f"SELECT * FROM tb_cameras where camera_id={camera_reference}")
        if self.ui_cofig.camera_reference.text() and self.ui_cofig.camera_ip.text():
            try:
                if not checker:
                    my_cursor.execute("INSERT INTO tb_cameras(camera_id,camera_url) VALUES(?,?)",(self.ui_cofig.camera_reference.text(),camera_url))
                    db.commit()
                    db.close()
                    self.ui_cofig.label_notification.setText("Camera details saved successfully\nCamera Id: %s" %camera_reference)
                else:
                    self.ui_cofig.label_notification.setText("Oops! camera ID already exist..")
            except Exception as e:
                self.ui_cofig.label_notification.setText(str(e))
        else:
            self.ui_cofig.label_notification.setText("Oops! invalid details provided!")

    def update_camera_details(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        camera_reference = self.ui_cofig.camera_reference.text()
        camera_reference=camera_reference.strip() 
        camera_url = self.ui_cofig.camera_ip.text()
        camera_url=camera_url.strip()
        if self.ui_cofig.camera_reference.text() and self.ui_cofig.camera_ip.text():
            try:
                cursor.execute("UPDATE tb_cameras SET camera_url=? WHERE camera_id=?",(camera_url,camera_reference))
                db.commit()
                db.close()
                self.ui_cofig.label_notification.setText("Camera URL updated successfully\nCamera Id: %s" %camera_reference) 
            except Exception as e:
                self.ui_cofig.label_notification.setText(str(e))
        else:
            self.ui_cofig.label_notification.setText("Oops! invalid details provided!") 

    def delete_camera(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        camera =self.value_formater(self.ui_cofig.camera_reference.text())
        camera = camera.strip()
        if self.ui_cofig.camera_reference.text():
            try:
                cursor.execute(f"DELETE FROM tb_cameras WHERE camera_id={camera}")
                db.commit()
                db.close()
                self.ui_cofig.label_notification.setText("Camera removed successfully\nCamera Id: %s" %self.ui_cofig.camera_reference.text())
            except Exception as e:
                self.ui_cofig.label_notification.setText(str(e))
        else:
            self.ui_cofig.label_notification.setText("Oops! camera Id provided!") 
               
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


    