import difflib
import re

def minLength(password):
    return len(password) >= 8

def minDifference(username, password):
    complexity = difflib.SequenceMatcher(None, username, password)
    return complexity.ratio() < 0.9

def minComplex(password):
    regex1 = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    regex2 = re.compile('[a-z0-9A-Z]')
    return regex1.search(password) and regex2.search(password)