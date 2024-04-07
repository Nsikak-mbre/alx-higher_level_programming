#!/usr/bin/python3
def safe_print_integer(value):
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
    except ValueError:
        pass
        return False
