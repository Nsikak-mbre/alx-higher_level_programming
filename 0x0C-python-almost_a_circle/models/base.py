#!/usr/bin/python3
"""Base model"""
import json


class Base:
    """Base from which other classes/methods gets derived

    Private class Attribute:
        __nb_object (int): Tracks number of Instantiation
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor

        Args:
            id (int): Assigns id to derived object optionally
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
