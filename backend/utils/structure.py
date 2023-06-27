import json

def load_data(resource_path):
    """
    Returns the content of the file read
    or nothing if there is an error.
    Args: 
        path = path to the file to read.
    """
    with open(resource_path,'r') as f:
        data = f.read()
        try:
            return json.loads(data)
        except Exception as e:
            print(e)

def load_colleges(resource_path):
    """
    Returns a list of colleges from the file read.
    """
    data = load_data(resource_path)
    items = []
    for x in data:
        item = get_key(x)
        items.append(item)
    return items

def get_key(item):
        """
        Returns the key of the first item of a 
        dictionary.
        Args: 
            item = represents the name of the dictionary.
        """
        key, *_ = item.keys()
        return key

def load_faculties(resource_path,name_of_college):
    """
    Returns the names of all faculties under
    a particular college.
    Args:
        name_of_college = represents the name
        of the collge while faculties are to be returned.
    """
    data = load_data(resource_path)
    result = [c for c in data if get_key(c) == name_of_college]
    if len(result) > 0:
        college = result[0][name_of_college]        
        items = []
        for item in college.keys():
            items.append(item) 
        return items

def get_dept(resource_path,name_of_college, faculty_name):
     """
     Returns the department under a particular
     faculty.
     Args:
        name_of_college
        faculty_name
     """
     data = load_data(resource_path)
     result = [c for c in data if get_key(c) == name_of_college]
     if len(result) > 0:
        college = result[0][name_of_college]        
        return college[faculty_name]
    
def load_database_properties(resource_path,name_of_college):
    data = load_data(resource_path)
    result = [c for c in data if get_key(c) == name_of_college]
    if len(result) > 0:
        college = result[0][name_of_college]        
        items = []
        for item in college.values():
            items.append(item) 
        return items
