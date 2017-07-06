import re
def validate_email(user_string):

    if user_string == None:
        return None

    match = re.search(r'[\w]+@[\w.]+',user_string)

    if match:
        return True
    else:
        return None
