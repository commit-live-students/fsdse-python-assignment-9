import re
email= "varunppanicker@gmail.com"
def validate_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

print validate_email(email)
