import os
import smtplib
from pathlib import Path
from pdf_mail import sendpdf
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

from packages.pyqt import *

class MailThread(QThread):
    def __init__(self,details:list,mail_content,file_path):
        self.details = details
        self.mail_content = mail_content
        self.file_path = file_path
        super().__init__()
 
    def run(self):
        message = EmailMessage()
        message['from']= self.details[3]
        message['to']= self.details[0]
        message['subject']= self.details[1]
        message.attach(MIMEText(self.mail_content,'plain'))
        message.add_attachment(open(self.file_path).read(),filename=Path(self.file_path).name)
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login(self.details[2],self.details[4])
            server.send_message(message)
        server.close()

class MailThreadPDF(QThread):
    def __init__(self,details:list,mail_content,file_path,directory):
        self.details = details
        self.mail_content = mail_content
        self.file_path = file_path
        self.directory = directory
        super().__init__()
 
    def run(self):
        mail = sendpdf(self.details[2],self.details[0],self.details[4],self.details[1],
        self.mail_content,os.path.basename(self.file_path),self.directory) 
        mail.email_send()

class QRCodeMailThread(QThread):
    def __init__(self,details:list,mail_content,file_path):
        self.details = details
        self.mail_content = mail_content
        self.file_path = file_path
        super().__init__()
 
    def run(self):
        message = MIMEMultipart()
        message['from']= self.details[3]
        message['to']= self.details[0]
        message['subject']= self.details[1]
        message.attach(MIMEText(self.mail_content,'plain'))
        message.attach(MIMEImage(Path(self.file_path).read_bytes()))
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login(self.details[2],self.details[4])
            server.send_message(message)
        server.close()

class BatchQRCodeMailThread(QRunnable):
    def __init__(self,details:list,mail_content,file_path,receiver):
        self.details = details
        self.mail_content = mail_content
        self.file_path = file_path
        self.receiver = receiver
        super().__init__()
 
    def run(self):
        message = MIMEMultipart()
        message['from']= self.details[3]
        message['to']= self.receiver
        message['subject']= self.details[1]
        message.attach(MIMEText(self.mail_content,'plain'))
        message.attach(MIMEImage(Path(self.file_path).read_bytes()))
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.starttls()
            server.login(self.details[2],self.details[4])
            server.send_message(message)
        server.close()