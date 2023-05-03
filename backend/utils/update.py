import json

def update_mail_details(path:str,properties):
    with open(path,'r') as content:
        data = json.load(content) 
        data['sender'] = properties[0]
        data['subject'] = properties[1]
        data['mail'] = properties[2]
        data['password'] = properties[3]
        with open(path,'w') as content:
            json.dump(data, content, indent=4)
        content.close()