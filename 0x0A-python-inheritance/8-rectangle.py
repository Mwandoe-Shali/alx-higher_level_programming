#!/usr/bin/python3
"""
Module 8-rectangle
Contains a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns:
            str: The string representation of the Rectangle object.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
