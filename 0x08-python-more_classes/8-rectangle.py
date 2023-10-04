#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """ Class that represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#" """Used as symbol for string representation"""

    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectange"""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """Returns string representation of the Rectangle. """
        return "Rectangle({:d}, {:d})". format(self.__width, self.__height)

    def __del__(self):
        """Prints a msg when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
