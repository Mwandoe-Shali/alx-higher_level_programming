#!/usr/bin/python3
"""
Module 2-is_same_class
This module defines the is_same_class function that
checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.
    Returns True if the object is an instance of the class; otherwise, False.
    """
    return type(obj) is a_class
