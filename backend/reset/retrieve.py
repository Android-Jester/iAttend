
from packages.hasher import *
from database.database import  *
from packages.pyqt import *
from reset.ui_password import Ui_Forgot

class ForgotPassword(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_reset = Ui_Forgot()
        self.ui_reset.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_reset.btn_close.clicked.connect(self.close)
        self.ui_reset.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_reset.btn_close.clicked.connect(self.close)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui_reset.frame.mouseMoveEvent = self.MoveWindow

        self.database = Database()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_reset.frame.setGraphicsEffect(self.shadow)
        self.ui_reset.btn_send.clicked.connect(self.reset)

    def clear_fields(self):
        self.ui_reset.password.clear()
        self.ui_reset.username.clear()
        self.ui_reset.reference.clear()

    def reset(self):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        check_state = self.database.check_state()
        username = self.ui_reset.username.text()
        reference = self.ui_reset.reference.text()
        password = self.ui_reset.password.text() 
        if reference and username and password:
            if check_state == True:
                details=self.query_database("SELECT * FROM tb_user_credentials WHERE user_reference="+"\'{}\'".format(reference))
                if details:
                    if username==str(details[0][2]) and reference==str(details[0][1]):
                        hash = hash_password(password)
                        my_cursor.execute("UPDATE tb_user_credentials SET user_password=? WHERE user_reference=?",(hash,reference))
                        db.commit()
                        my_cursor.close()
                        self.clear_fields()
                        self.content("User password updated successfully")
                    else:
                        self.content(f"{username}, {reference} not found")
                else:
                    self.content("User not found for such combination")      
            else:
                details=self.query_database("SELECT * FROM tb_user_credentials WHERE user_reference="+"\'{}\'".format(reference))
                if details:
                    if username==str(details[0][2]) and reference==str(details[0][1]):
                        hash = hash_password(password)
                        my_cursor.execute("UPDATE tb_user_credentials SET user_password=%s WHERE user_reference=%s",(hash,reference))
                        db.commit()
                        my_cursor.close()
                        self.clear_fields()
                        self.content("User password updated successfully")
                    else:
                        self.content(f"{username}, {reference} not found")
                else:
                    self.content("User not found for such combination") 
        else: 
            self.content("Empty fields not permitted!")
            
    def query_database(self, query: str):
        db,my_cursor,connection_status = self.database.my_cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details    
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def content(self, content: str):
        return self.ui_reset.info_label.setText(content)