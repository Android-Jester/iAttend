import json
import os
import requests
from pathlib import Path
from packages.pyqt import *
from packages.date import current

class RequestThread(QThread):
    httpSignal = Signal(str)
    def __init__(self,url_details):
        super(RequestThread,self).__init__()
        self.url_details = url_details

    def run(self):
        try:
            request_body = requests.get(self.url_details)
            student_data=request_body.json()
            self.httpSignal.emit(f'Status code: {request_body.status_code}')
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
        except Exception as e:
            self.httpError_logs(str(e))
            self.httpSignal.emit(str(e))
           
    def httpError_logs(self,message):
        time =current.now().time().strftime('%I:%M:%S %p')
        date=current.now().date().strftime('%a %b %d %Y')
        filename=current.now().date().strftime('%a_%b_%d_%Y')
        path =Path(f'C:\\ProgramData\\iAttend\\data\\httpErrors\\{filename}.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n[{date}] [{time}]: {message}')
            file.close()
        
        