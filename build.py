import re
def validate_email(string):
    boolean = False
    pattern = "[\w\.-]+@[\w\.-]+"
    match = re.findall(pattern, string) #TO FINDALL THE PATTERN IN A GIVEN STRING
    #     match = re.split('\s', string)
    #     print match
    for element in match:
#         print element
        if string == element:
            boolean = True
            return boolean
        else:
            return boolean
