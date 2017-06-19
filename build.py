import re
def validate_email(input):
    return bool(re.search("[a-zA-Z0-9\.+-_]*@[a-zA-Z]*\.[a-zA-Z]*",input))
