#!/usr/bin/python3
"""
Module 100-my_int
Contains a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Represents a rebel integer.
    Inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return super().__eq__(other)
