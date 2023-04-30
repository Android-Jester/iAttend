
import os
import requests

from mail.thread import MailThread
from mail.thread import MailThreadPDF

from utils.sql import *
from packages.pyqt import *
from utils.structure import *
from mail.ui_mail import Ui_Mail

class Mail(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui_mail = Ui_Mail()
        self.ui_mail.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_mail.btn_close.clicked.connect(self.close)
        self.ui_mail.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_mail.frame.mouseMoveEvent = self.MoveWindow

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_mail.frame.setGraphicsEffect(self.shadow)
        self.ui_mail.btn_send_mail.clicked.connect(self.send_email)
        self.ui_mail.btn_browse_reg.clicked.connect(self.browse_files)
        self.set_sender_details()
       
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def browse_files(self): 
        file_type = "PDF Files(*.pdf);;CSV Files(*.csv);;JSON Files(*.json)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\ProgramData\\iAttend\\data",file_type)
        if path:
            self.ui_mail.image_file_reg.setText(path[0])
            return path[0]

    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False

    def get_email_details(self):
        from_ = self.ui_mail.email_from.text()
        from_email = self.ui_mail.email_sender.text()
        subject = self.ui_mail.email_subject.text()
        password = self.ui_mail.sender_password.text()
        to_address = self.ui_mail.reg_email.text()
        return to_address, subject, from_email, from_, password

    def set_sender_details(self):
        details=self.get_details()
        self.ui_mail.email_from.setText(details[0])
        self.ui_mail.email_sender.setText(details[2])
        self.ui_mail.email_subject.setText(details[1])
        self.ui_mail.sender_password.setText(details[3])
    
    def get_details(self):
        data=load_data('C:\\ProgramData\\iAttend\\data\\email_details\\details.json')
        return data['sender'],data['subject'],data['mail'],data['password']
    
    def get_mail_content(self):
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\content_report.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
            return details.replace('name',self.ui_mail.rep_name.text())
    
    def send_pdf_mail(self):
        details = self.get_email_details()
        content = self.get_mail_content()
        file_path__ = self.ui_mail.image_file_reg.text()
        file_path= file_path__.split('.')[0]
        directory=os.path.dirname(file_path__)
        directory = directory.replace(os.path.sep,'/')
        self.mail_thread_pdf = MailThreadPDF(details,content,file_path,directory)
        self.mail_thread_pdf.start()

    def prepare_email(self):
        details = self.get_email_details()
        content = self.get_mail_content()
        file_path=self.ui_mail.image_file_reg.text()
        self.mail_thread = MailThread(details,content,file_path)
        self.mail_thread.start()

    def prepare_email_to_send(self):
        if self.connected_to_internet()==True and self.ui_mail.reg_email.text() and self.ui_mail.image_file_reg.text():
            try:
                resolve_path = os.path.basename(self.ui_mail.image_file_reg.text())
                resolve_path = resolve_path.split('.')[1]
                if resolve_path == 'pdf':
                    self.send_pdf_mail()
                    self.ui_mail.label_notification.setText("Hey! mail sent successfully...")
                else:
                    self.prepare_email()
                    self.ui_mail.label_notification.setText("Hey! mail sent successfully...")
            except Exception as e:
                self.ui_mail.label_notification.setText(str(e))
        else:
            self.ui_mail.label_notification.setText("Oops! something went wrong mail\nnot sent...")
      
    def send_email(self):
        self.ui_mail.label_notification.setText("Notification")
        self.prepare_email_to_send()
