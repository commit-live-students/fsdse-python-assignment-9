
import re
def validate_email(str1="default"):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.search(pattern, str1):
        return False
    else:
        return True

print(validate_email("nikhil@gmail.com"))
