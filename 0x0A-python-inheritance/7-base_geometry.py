#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """calculates area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer input

        Args:
            name(string): naming instance
            value(int): specification
        Raises:
            TypeError: if wrong type is used
            ValueError: If value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
