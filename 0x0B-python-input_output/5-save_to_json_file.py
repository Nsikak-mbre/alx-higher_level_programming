#!/usr/bin/python3
"""Returns Json representation of an object"""
import json


def save_to_json_file(my_obj, filename):
    """
    Accepts Object and file destination

    Args:
        my_obj(object): Data-type in Python

    Returns:
        Json tect representation of given Object
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, sort_keys=True)
