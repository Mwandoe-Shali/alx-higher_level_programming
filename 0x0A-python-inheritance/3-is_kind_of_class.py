#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Checks if an object is an instance of, or if the object is an
instance of a class that is inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the class
    or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
