#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    ''' This function prints a text with 2 new lines after each ".", "?", or ":"
    There should be no space at the beginning or at the end of each printed line

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
