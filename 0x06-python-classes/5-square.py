#!/usr/bin/python3
"""Define square class"""


class Square:
    """include method to print to stdout"""

    def __init__(self, size=0):
        self.size = size

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

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square elmemt # to stdout"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print('')
        if self.__size == 0:
            print('')
