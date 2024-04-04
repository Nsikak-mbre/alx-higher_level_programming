#!/usr/bin/python3
"""Now we had a method that cal's area of square """


class Square:
    """Updating by adding a public method"""

    def __init__(self, size=0):
        pass

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size **
