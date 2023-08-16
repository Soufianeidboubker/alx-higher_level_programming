#!/usr/bin/python3
old_matrix = matrix.copy()

for s in range(len(matrix)):
    old_matrix[s] = list(map(lambda x: x**2, matrix[s]))

    return (old_matrix)
