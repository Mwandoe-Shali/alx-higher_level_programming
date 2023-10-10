#!/usr/bin/python3
"""
Module: 0-read_file
Reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
