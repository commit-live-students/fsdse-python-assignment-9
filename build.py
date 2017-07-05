import re
def validate_email(email):
    if email == '' or email == None:
        return False

    if re.match(r"[^@]+@[^@]+\.[^@]", email) is None:
        return False
    return True
