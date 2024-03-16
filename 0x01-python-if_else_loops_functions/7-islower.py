#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        return False
    elif ord('a') <= ord(c) >= ord('z'):
        return True
    else:
        return False
