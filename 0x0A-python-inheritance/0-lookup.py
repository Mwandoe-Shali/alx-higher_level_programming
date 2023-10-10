#!/usr/bin/python3
"""
Module 0-lookup
This module returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of an object.
    """
    return dir(obj)
