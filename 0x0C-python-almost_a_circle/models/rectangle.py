#!/usr/bin/python3
"""Rectangle class that inherits from Base Model"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Constructor

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
            x (int): X coordinate of the Rectangle
            y (int): Y coordinate of the Rectangle
            id (int): Assigns id to Rectangle object optionally
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints out visual representation of Rectangle"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """Custom string representation of rectangle class."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns values using *args if provided,else **kwargs"""
        attributes = ["id", 'width', 'height', 'x', 'y']
        for attribute, value in zip(attributes, args):
            setattr(self, attribute, value)
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
