#!/usr/bin/python3
def pow(a, b):
    if a < 0 and b % 2 == 1:
        return -abs(a ** b)
    elif b < 0:
        return 1 / (a ** abs(b))
    else:
        return a ** b
