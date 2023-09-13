#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    ''' Squares elements in a matrix '''
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
