import re

def CorrectEmail(email):
    pattern = r"[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+(\.[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+)*"
    return re.match(pattern, email) is not None

email = "jnguyen155@student.gsu.edu"
if CorrectEmail(email):
    print(f"{email} is the correct email")
else:
    print(f"{email} is not a valid email address")