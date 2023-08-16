#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()

    for s in range(len(matrix)):
        nw_matrix[s] = list(map(lambda x: x**2, matrix[s]))

    return (nw_matrix)
