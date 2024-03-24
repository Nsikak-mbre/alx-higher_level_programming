#!/usr/bin/python3
def pow(a, b):
    if a < 0:
        a = abs(a)
    result = 1
    if b < 0:
        for _ in range(abs(b)):
            result *= 1/a
    else:
        for _ in range(b):
            result *= a
    return result
