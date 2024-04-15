#!/usr/bin/python3
"""Prints square with the Character #"""


def print_square(size):
    """Function takes one parameter

    Parameter:
    size (int): Determines the size of the square.

    Raises:
        TypeError if given size is not of type int
        ValueError if size less thna 0
        TypeError if type of size is float and less than 0

    Returns:
    Square shape
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size ,ust be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
# end of file
