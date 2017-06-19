import re

def validate_email(ip):
    result = True
    cnt = re.findall('^[A-Za-z0-9].*@.*\.com',ip)
    print cnt
    if cnt == []:
        result = False
    print result
    return result


validate_email('adinathau2ti@ysmail.com')
