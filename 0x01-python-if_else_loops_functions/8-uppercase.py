#!/usr/bin/python3
def uppercase(str):
    capital_letter = ''
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            capital_letter += chr(ord(str[i]) - 32)
        else:
            capital_letter += str[i]
    print('{}'.format(capital_letter))
