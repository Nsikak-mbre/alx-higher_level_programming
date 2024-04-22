#!/usr/bin/python3
"""This function returns the available attributes and methods of an Object"""


def lookup(obj):
    """Returns a list of obj's availables attribute"""
    return (dir(obj))
