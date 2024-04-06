#!/usr/bin/python3
"""Define square class"""


class Square:
    """include method to print to stdout"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """get current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """allows to modify size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """gets current position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError('position must contain non-negative integers')
        self.__position = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square with character # using position values"""
        if self.__size == 0:
            print()
            return

        if self.position[1] > 0:
            for _ in range(self.position[1]):
                print()

        for _ in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)
