#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """rectangle Object created"""
    def __init__(self, width=0, height=0):
        """initialise attribute for instances.


        Args:
            width (int): self explanatory
            height (int): salf explanatory
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Using property decorator to get/set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Property decorater to define getter/setter methods"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
# Best Practice
