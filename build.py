import re

def validate_email(email):
    if email is None or email == "":
        return
    pattern = re.compile('^[A-Za-z0-9_.]*@[A-Za-z0-9._]*\.[A-Za-z]*$')
    match = re.match(pattern, email)

    if match:
        return True
    else:
        return False
