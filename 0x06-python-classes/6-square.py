#!/usr/bin/python3
"""Defines a square with a size attribute """

class Square:

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.__size = size
        self.position = position


    @property
    def size(self):
        """Retrieves the side of a square's size. """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Coordinates of this Square. """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: 
            Value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Returns: The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
