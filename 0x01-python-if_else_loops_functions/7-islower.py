#!/usr/bin/python3
def islower(c):
    if len(c) != 1 or not c.isalpha():
        return False
    elif 'a' <= c <= 'z':
        return True
    else:
        return False
