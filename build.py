import re

def validate_email(email):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern, email):
        return True
    else:
        return False

r = "[0-3]?[0-9]-[0-9]{2}-[0-9]{4}$"  #12-01-1998 (1-31)

print(validate_email('info@greyatom.co.in'))
print (validate_email('info@greyatom'))
