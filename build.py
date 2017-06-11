import re
def validate_email(str):
    if not str:
        return False
    else:
        if re.search("[A-Za-z0-9_.]+@[A-Za-z0-9]+\\.[A-Za-z]{2,5}$",str) != None:
            return True
        else:
            return False
#print validate_email("mkyong@gmail.com.1a")
