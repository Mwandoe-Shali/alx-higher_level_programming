#!/usr/bin/python3
"""
Module 4-print_square
A function that prints a square
"""


def print_square(size):
    """This function prints a square with character "#"

    Args:
        size (int): This represents the length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            print("#", end='')
        print()
