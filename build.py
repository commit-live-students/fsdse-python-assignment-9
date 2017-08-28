import re

def validate_email(emailid):
    match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",emailid)
    if match:
        return True
    else:
        return False



'''
a = raw_input('Enter EmailId : ')
print validate_email(a)
'''
