#!/usr/bin/python3
"""
Module 10-square
Contains a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns:
            str: The string representation of the Square object.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
