#!/usr/bin/python3
"""Creates an object from json file"""
import json


def save_to_json_file(filename):
    """
    Returns:
        Python Object representation of json file
    """
    with open(filename, 'r') as file:
        json_data = file.read()
        return json.loads(json_data)
