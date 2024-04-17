#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        print_symbol (object): Used for string representation
        number_of_instances (int): self explanatory
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        "Perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns human readable representation of an object/reactanlge

        Represents the rectanlge with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ('')

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return (''.join(rect))

    def __repr__(self):
        """Returns Rectangle's representation primarily for debugging"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes instances of Rectangle"""

        type(self).number_of_instances -= 1
        print('{}'.format('Bye rectangle...'))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns largest instance of rectangle

        Args:
            rect_1 (Rectangle): an instance of Rectangle class
            rect_2 (Rectangle): Another instance of Rectangle class
        Raises:
            TypeError: if either is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
