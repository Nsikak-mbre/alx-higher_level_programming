def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        raw = ' '.join([f'{num:d}' for num in row])
        print(raw)
