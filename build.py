import re

def validate_email(emailString):

    match = re.search(r'[\w.-]+@[\w.-]+.\w+', emailString)

    if match:
        return True
    else:
        return False
