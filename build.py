import re


def validate_email(iEmail):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.match(pattern, iEmail):
        return True

print validate_email('anujay.saraf@tcs.com')
