#!/usr/bin/python3
"""Divide elements of a Matrix"""


def matrix_divided(matrix, div):
    """Function takes two arguments.

    Parameters:
    matrix (list): list of integers
    div: (int/float) The divisor

    Raises:
        TypeError: if user inputs wrong types
        TypeError: Rows sizes dont match
        TypeError: If div type does not match requirement
        ZeroDivisionError: if div is 0

    Returns:
    (list): new matrix where elements are divided by the divisor
    """
    err = 'matrix must be a matrix (list of lists) of integers/floats'
    if matrix is None:
        raise TypeError(err)

    if not isinstance(matrix, list) or not all(isinstance(sub_list, list) and
       all(isinstance(elem, (int, float)) for elem in
       sub_list) for sub_list in matrix):
        raise TypeError(err)

    row_length = len(matrix[0])
    for sub_list in matrix:
        if len(sub_list) != row_length:
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_list = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_list
# Python convention
