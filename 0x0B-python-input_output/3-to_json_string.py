#!/usr/bin/python3
"""convert object(string) to JSON"""
import json


def to_json_string(my_obj):
    """
    Returns:
        JSON string representation of given object
    """
    return json.dumps(my_obj)
