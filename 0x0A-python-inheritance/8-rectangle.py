#!/usr/bin/python3
"""Define Class Rectangle, with direct inheritance from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from Parent classs."""

    def __init__(self, width, height):
        """Initialise attributes for instances.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
