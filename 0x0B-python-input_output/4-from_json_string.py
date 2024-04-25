#!/usr/bin/python3
"""Returns an object represented by JSON string"""
import json


def from_json_string(my_str):
    """
    Accepts Json representation of an object

    Args:
        my_str(JSON): python object in Json format

    Returns:
        Python object
    """
    return json.loads(my_str)

