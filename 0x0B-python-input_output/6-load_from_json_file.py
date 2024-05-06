#!/usr/bin/python3
"""Creates an object from json file"""
import json


def load_from_json_file(filename):
    """Python Object representation of json file"""
    with open(filename) as file:
        json_data = file.read()
        return json.loads(json_data)
