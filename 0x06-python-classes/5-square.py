#!/usr/bin/python3
"""Defines a square with a size attribute """


class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves the side of a square's size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns: The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
