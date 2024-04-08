#!/usr/bin/python3
def raise_exception(text):
    """

    Function that raises a type exception

    """
    try:
        text = "The answer is: " + 4
        return text
    except TypeError:
        print('Exception raised')
