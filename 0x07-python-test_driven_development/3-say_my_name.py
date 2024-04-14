#!/usr/bin/python3
"""Function that prints full-name's"""


def say_my_name(first_name, last_name=""):
    """Funtion takes two argument.

    Paramter:
    first_name (str) : only accepts a string
    last_name (str): ... could be optional

    Raises:
        TypeError: if user inputs wrong type

    Returns:
    (str): value for both names, or error message if any wrong type is supplied
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
