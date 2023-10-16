#!/usr/bin/python3
"""
Module Rectangle
This module defines the Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The id value for the object.
                            If None, a unique id will be assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute. """
        return self.__width

    @property
    def height(self):
        """Getter method for the height attribute. """
        return self.__height

    @property
    def x(self):
        """Getter method for the x attribute. """
        return self.__x

    @property
    def y(self):
        """Getter method for the y attribute. """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The value to set as width

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The value to set as height

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter method for the x attribute.

        Args:
            value (int): The value to set as x-coordinate

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0 """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter method for the y attribute.

        Args:
            value (int): The value to set as y-coordinate

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0 """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle using the # character
        Takes into account the x & y attributes
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns:
            str: The string representation of the Rectangle instance.
        """
        rect = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return rect

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.

        Args:
            *args: No. of arguments in order (id, width, height, x, y).
            **kwargs: No. of keyword args showing attribute-value pairs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns:
            dict: A dictionary representation of the Rectangle instance.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
