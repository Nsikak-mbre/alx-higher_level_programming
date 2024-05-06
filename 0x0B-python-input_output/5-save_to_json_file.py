#!/usr/bin/python3
"""Returns Json representation of an object"""
import json


def save_to_json_file(my_obj, filename):
    """Returns Json representation of an object"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
