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

def update_information_file():
    path = 'C:\\ProgramData\\iAttend\\data\\student\\information.json'
    with open(path,'r') as content:
        update = json.load(content) 
        update['firstname'] = 'firstname'
        update['othername'] = 'othername'
        update['lastname'] = 'lastname'
        update['reference'] = 'reference'
        update['index'] = 'index'
        update['nationality'] = 'nationality'
        update['college'] = 'college'
        update['type'] = 'type'
        update['gender'] = 'gender'
        update['disabled'] = 'disabled'
        update['department'] = 'department'
        update['faculty'] = 'faculty'
        update['validity'] = 'validity'
    content.close()
    with open(path,'w') as content:
        json.dump(update, content, indent=4)
    content.close()