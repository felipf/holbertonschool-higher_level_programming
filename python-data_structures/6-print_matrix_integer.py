#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return
    for column in range(len(matrix)):
        for row in range(len(matrix[column])):
            print("{:d}".format(matrix[column][row]), end="")
            if row < len(matrix[column]) - 1:
                print(end=" ")
        print()
