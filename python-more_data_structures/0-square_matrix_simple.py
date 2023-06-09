#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nMatrix = []
    for i in matrix:
        nMatrix.append(list(map(lambda x: x ** 2, i)))
    return nMatrix
