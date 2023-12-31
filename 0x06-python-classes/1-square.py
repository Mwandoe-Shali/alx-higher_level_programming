#!/usr/bin/python3
""" Defines a square with a size attribute"""


class Square:
    """square class with size attribute

    args:
        size - Represents the size of the square defined

    attributes:
        size - private instance attribute
    """

    def __init__(self, size):
        self.__size = size
