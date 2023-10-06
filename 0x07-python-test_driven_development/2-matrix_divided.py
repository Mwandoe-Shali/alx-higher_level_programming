#!/usr/bin/python3
"""
Module 2-matrix_divided
Requires same-size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If div is not int or float type,
                    if the matrix contains non-numbers or,
                    rows of different sizes.
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    prev_len = 0
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_msg)

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError(err_msg)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(err_msg)

        if len(block) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(block)

    return [[round(elem / div, 2) for elem in row] for row in matrix]
