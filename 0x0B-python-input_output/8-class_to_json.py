#!/usr/bin/python3
"""
Module: 8-class_to_json
Returns the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
