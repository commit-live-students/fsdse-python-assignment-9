import re

def validate_email(mail):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern, mail):
        return True
    else:
        return False
