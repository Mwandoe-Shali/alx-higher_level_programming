#!/usr/bin/python3
"""
Module Square
This module defines the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id value for the object.
                            If None, a unique id will be assigned.
        """
        super().__init__( size, size, x, y, id)

    def __str__(self):    
        """
        Returns:
            str: A string representation of the Square instance in the format
                            [Square] (<id>) <x>/<y> - <size>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__width

    
    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size value for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be greater than 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: Variable length argument list.
                            The first argument should be the id attribute,
                            the second argument should be the size attribute,
                            the third argument should be the x attribute, and
                            the fourth argument should be the y attribute.
            **kwargs: Variable length keyword argument list.
                            Each key represents an attribute to be updated.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns:
            dict: A dictionary representation of the Square instance.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }



