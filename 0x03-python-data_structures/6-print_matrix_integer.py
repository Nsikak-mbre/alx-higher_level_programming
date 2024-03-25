#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        raw =' '.join('{:d}'.format(num) for num in row)
        print(raw)
    return raw
