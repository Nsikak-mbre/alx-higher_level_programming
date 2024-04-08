#!/usr/bin/python:
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print('Inside Result: {}'.format(result))
    return result
