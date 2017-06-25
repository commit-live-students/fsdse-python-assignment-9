import re
def validate_email(string):
    if (string != ""):
        if re.findall('@',string):
            return True
        else:
            return False

    else:
        print " invalid email"
