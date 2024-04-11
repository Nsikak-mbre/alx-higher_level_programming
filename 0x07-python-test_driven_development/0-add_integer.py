#!/usr/bin/python3
""" Sum of two int"""


def add_integer(a, b=98):
    """sums two Integers.

    Parameters:
    a (int): Integer provided by user
    b (int): Integer by user or default

    Returns:
    Int: sum or an exception if wrong type is provided
    """
    if ((not instance(a, int) and not isisntance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
# according to requirement
