#!/usr/bin/python3
def uppercase(str):
    uppercase_string = ''
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_chr = chr(ord(char) - 32)
            uppercase_string += uppercase_chr
        else:
            uppercase_string += char
    print(uppercase_string)
