
import time
import requests
from time import strptime
from mail.send import *
from mail.thread import *
from packages.date import *
from mail.user_mail import *
from packages.hasher import *
from database.database import  *
from packages.pyqt import *
from packages.globals import *
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
        self.ui_reset.btn_send.clicked.connect(self.reset_threads)

    def clear_fields(self):
        self.ui_reset.password.clear()
        self.ui_reset.username.clear()
        self.ui_reset.reference.clear()
        
    def reset_threads(self):
        self.pool = QThreadPool()
        self.work = SendThread(self.reset)
        self.pool.start(self.work)

    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False 

    def get_mail_content(self,lastname,username):
        date = current.now().strftime("%a %b %d, %Y")
        stamp = time.strftime("%I:%M:%S %p")
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\credential_mail.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
                details = str(details).replace('Name',lastname).replace('account_name',username).replace('date_stamp',date).replace('time_stamp',stamp).replace('College_name','CoS Team')
            return details

    def get_details(self):
        data=load_data('C:\\ProgramData\\iAttend\\data\\email_details\\reset_password.json')
        return data['sender'],data['subject'],data['mail'],data['password']

    def send_mail(self,reference,username): 
        account_mail=self.query_database("SELECT user_mail,user_lastname FROM tb_user_details WHERE user_reference="+"\'{}\'".format(reference))
        if self.connected_to_internet()==True:
            self.mail=UserMailThread(details=self.get_details(),mail_content=self.get_mail_content(str(account_mail[0][1]),username),receiver=str(account_mail[0][0]))
            self.mail.start()
        else:
            pass

    def reset(self):
        check_state = self.database.check_state()
        username = self.ui_reset.username.text()
        reference = self.ui_reset.reference.text()
        password = self.ui_reset.password.text()
        if reference and username and password:
                (db,my_cursor,connection_status) = self.database.my_cursor()
                if check_state == True:
                    self.content("Oops! not connected to database..") 
                else:
                    try:
                        details=self.query_database("SELECT * FROM tb_user_credentials WHERE user_reference="+"\'{}\'".format(reference))
                        if details:
                            if username==str(details[0][2]) and reference==str(details[0][1]):
                                hash = hash_password(password)
                                my_cursor.execute("UPDATE tb_user_credentials SET user_password=%s WHERE user_reference=%s",(hash,reference))
                                db.commit()
                                my_cursor.close()
                                self.clear_fields()
                                self.send_mail(reference,username)
                                self.content("User password updated successfully")
                            else:
                                self.content(f"{username}, {reference} not found")
                        else:
                            self.content("User not found for such combination")
                    except:
                        self.content("Oops! Something went wrong")  
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