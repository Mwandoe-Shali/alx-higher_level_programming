#!/usr/bin/python3
"""
Module: 1-write_file
Writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): The name of the text file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
