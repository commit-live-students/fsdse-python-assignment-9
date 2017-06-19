import re
def validate_email(s1):
    if s1 == '':
        raise ValueError
    pattern = re.compile(r"[0-9a-zA-Z_+\.]+@[0-9a-zA-Z_+\.]+\.[0-9a-zA-Z_+\.]+")
    if re.match(pattern,s1):
        return True
    else:
        return False
        
