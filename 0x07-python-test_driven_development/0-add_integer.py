#!/usr/bin/python3
""" Sum of two int
"""

def add_integer(a, b=98):
    """sums two Integers.

    Parameters:
    a (int): Integer provided by user
    b (int): Integer by user or default

    Returns:
    Int: sum or an exception if wrong type is provided
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError('a must be an integer')

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError('b must be an integer')

    return a + b
