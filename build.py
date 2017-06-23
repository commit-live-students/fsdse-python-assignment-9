import re
def validate_email(string):
    exp = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if string != '':
        m = re.findall(exp,string)
    return True   
