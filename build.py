import re

def validate_email(x):
    if re.search(r'^[a-zA-Z0-9\.\+-_\$]+@[a-zA-Z0-9\.\+-_]+\.[a-zA-Z0-9\.]*$', x):
        return True
    else:
        return False
