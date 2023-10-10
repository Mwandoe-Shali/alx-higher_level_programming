#!/usr/bin/python3
"""
Module 4-inherits_from
Checks if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a subclass; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
