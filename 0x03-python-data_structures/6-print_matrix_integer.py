#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers.'''
    for row in matrix:
        for col in row:
            if col != row[-1]:
                # If col is not the last element in the row,
                # print without a trailing space
                print('{}'.format(col), end='')
            else:
                # If col is last element in row, print with a trailing space
                print("{}".format(col), end=' ')
        # Move to the next row after printing all columns
        print()
