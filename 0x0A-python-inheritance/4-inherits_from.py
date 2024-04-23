#!/usr/bin/python3
"""Returns True if class is a direct sub-class of an Object"""


def inherits_from(obj, a_class):
    """Check for inheritance type

    Args:
        obj(any): Instance of a class
        a_class (type): Base class
    Return:
        True of class is directly inherits from class
    """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
