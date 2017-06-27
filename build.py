import re

def validate_email(email):

    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if not EMAIL_REGEX.match(email):
        return False
    else :
        return True

validate_email("we@aregreat.com")
