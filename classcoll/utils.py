import re
import os

messages = [
    'Password must be at least 8 characters',
    'Password must not be the same as username',
    'Password must contain at least one non alpha-numeric character',
    'Password is acceptable'
]

def validatePassword(username, password):
    if password.len() < 8:
        return messages[0]
    if password == username:
        return messages[1]
    pattern = '^[\w-]+$'
    valid = re.match(pattern, password)
    if valid is None:
        return messages[2]
    else:
        return messages[3]
    