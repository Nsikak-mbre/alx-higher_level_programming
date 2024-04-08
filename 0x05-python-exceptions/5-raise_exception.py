#!/usr/bin/python3
def raise_exception(text):
    try:
        text = "The answer is: " +  4
        return text
    except TypeError:
        print('Exception raised')
