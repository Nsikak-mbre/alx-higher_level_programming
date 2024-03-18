#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ''
    for char in range(len(my_string)):
        if char not in ('c', 'C'):
            new_string += char
    print(new_string.format())
