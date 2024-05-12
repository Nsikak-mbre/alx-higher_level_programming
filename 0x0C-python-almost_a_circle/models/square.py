#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square Constructor

        Args:
            size (int): Width and Height of the Square
            x (int): X coordinate of the Square
            y (int): Y coordinate of the Square
            id (int): Assigns id to Square object optionally
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Custom string which overrides, inherited implemtation."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """returns width of a square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attribute values using *args if provided,else **kwargs."""
        attributes = ["id", "size", "x", "y"]
        for attribute, value in zip(attributes, args):
            setattr(self, attribute, value)
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Manual dictionary representation of some class attributes"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
