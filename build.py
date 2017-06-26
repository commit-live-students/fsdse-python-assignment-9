import re
def validate_email(email_string):
    pattern = re.compile(r"[0-9a-zA-Z_+\.]+@[0-9a-zA-Z_+\.]+\.[0-9a-zA-Z_+\.]+")
    if re.match(pattern,email_string):
        return True
    if email_string == '':
        raise ValueError
    else:
        return False
