import re


def validate_email(inputEmail):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern, inputEmail):
        return True
