#!/usr/bin/python3
"""Derived class from list object"""


class MyList(list):
    """Child inherits from list Object"""

    def print_sorted(self):
        """Prints list content in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
