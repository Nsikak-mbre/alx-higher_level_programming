#!/usr/bin/python3
import json
"""convert object(string) to JSON"""


def to_json_string(my_obj):
    """
    Accepts an object

    Args:
        my_obj(any-type): string object to be serialized

    Returns:
        JSON string representation of given object
    """
    return json.dumps(my_obj)
