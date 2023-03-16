import smtplib
from packages.pyqt import *
from email.message import EmailMessage

class UserMailThread(QThread):
    def __init__(self,details:list,mail_content,receiver):
        self.details = details
        self.receiver = receiver
        self.mail_content = mail_content
        super().__init__()
    
    def run(self):
        try:
            msg = EmailMessage()
            msg.set_content(self.mail_content)
            msg['Subject'] = str(self.details[0])
            msg['From'] = str(self.details[2])+' <apps.learning.commons@gmail.com>'
            msg['To'] = str(self.receiver)
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.starttls()
            server.login(str(self.details[1]),str(self.details[3]))
            server.send_message(msg)
            server.quit()
        except smtplib.SMTPException:
            pass