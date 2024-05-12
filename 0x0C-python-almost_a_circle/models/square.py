#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
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