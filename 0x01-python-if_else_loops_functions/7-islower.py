#!/usr/bin/python3
def islower(c):
    if isinstance(c, str) and len(c) == 1 and 97 <= ord(c) <= 122:
        return True
    else:
        return False
