def matrix_divided(matrix, div):
    """Function takes two arguments.

    Parameters:
    matrix (list): list of integers
    dit
    (int): divider

    Returns:
    (list): new matrix where elements are divided by the divisor
    """
    if matrix is None or not matrix:
        raise TypeError('matrix must be a matrix\
                        (list of lists) of integers/floats')

    if not isinstance(matrix, list) or not all(isinstance(sub_list, list) and
       all(isinstance(elem, (int, float)) for elem in
       sub_list) for sub_list in matrix):
        raise TypeError('matrix must be a matrix\
                        (list of lists) of integers/floats')

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
