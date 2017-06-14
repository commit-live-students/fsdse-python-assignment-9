import re
def validate_email(user_input):
    if user_input==None:
        return False
    isvalid=re.match(r'[\w.-]+@[\w.-]+.\w+',user_input)
    if isvalid:
        return True
    else:
        return False
print validate_email("heha@xya")
