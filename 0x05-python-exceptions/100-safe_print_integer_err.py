#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    prints formatted value

    Args:
        (value): itme to be formatted

    Returns:
        True if rightly formatted
    """
    try:
        formatted_value = '{:d}'.format(value)
        print(formatted_value)
        return True
    except (ValueError, TypeError) as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        return False
