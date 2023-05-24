import json
import requests
from packages.pyqt import *

class RequestThread(QThread):
    def __init__(self,url):
        super(RequestThread,self).__init__()
        self.url = url

    def run(self):
        request_body = requests.get(self.url)
        student_data=request_body.json()
        path = 'C:\\ProgramData\\iAttend\\data\\student\\information.json'
        with open(path,'r') as content:
            update = json.load(content) 
            update['firstname'] = student_data['firstname']
            update['othername'] = student_data['othername']
            update['lastname'] = student_data['lastname']
            update['reference'] = student_data['reference']
            update['index'] = student_data['index']
            update['nationality'] = student_data['nationality']
            update['college'] = student_data['college']
            update['type'] = student_data['type']
            update['gender'] = student_data['gender']
            update['disabled'] = student_data['disabled']
            update['department'] = student_data['department']
            update['faculty'] = student_data['faculty']
            update['validity'] = student_data['validity']
        content.close()
        with open(path,'w') as content:
            json.dump(update, content, indent=4)
        content.close()
        
        