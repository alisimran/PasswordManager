import secrets
import string
import random
import re

Alphlist = string.ascii_letters + string.digits + string.punctuation
punc = set(string.punctuation)
punc.remove('"')
punc.remove("'")

def generate_password(length):
    while True:
        password = ''.join(secrets.choice(Alphlist) for i in range(length))
        # checks if the password generated has atleast 2 digits, has uppercase , lowercase and special characters
        if(any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and (sum(c.isdigit() for c in password) >= 2)
            and any(c in punc for c in password)):
            return password
            break
    return False

    