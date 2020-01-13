#!/usr/bin/python3
"""
Module matrix_divided
This takes a matrix of numbers.
Type int
"""


def matrix_divided(matrix, div):
    """
    Return the div of each element of the matrix
    """
    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    m2 = "Each row of the matrix must have the same size"

    new_matrix = [i[:] for i in matrix]
    if not isinstance(new_matrix, list):
        raise TypeError(m1)

    length = len(new_matrix[0])
    for row in new_matrix:
        if len(row) != length:
            raise TypeError(m2)
        for i in range(len(row)):
            if not isinstance(row[i], (float, int)):
                raise TypeError(m1)

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row_n in new_matrix:
        for i in range(len(row_n)):
            row_n[i] = round((row_n[i] / div), 2)
    return new_matrix
