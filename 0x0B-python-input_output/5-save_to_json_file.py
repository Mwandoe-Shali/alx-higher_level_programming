#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Writes an object to a text file using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename: The name of the file to write the object to.

    Returns:
        None
    """
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
