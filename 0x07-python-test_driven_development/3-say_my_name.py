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
    if (not isinstance(first_name, str)) or not first_name.strip():
        raise TypeError('first_name must be a string')
    if last_name != '':
        if not isinstance(last_name, str) or not last_name.strip():
            raise TypeError('last_name must be a string')

    if last_name:
        full_name = first_name.strip() + ' ' + last_name.strip()
    else:
        full_name = first_name.strip()
    print('My name is {} {}'.format(first_name, last_name))
