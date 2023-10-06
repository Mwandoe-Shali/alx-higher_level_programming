#!/usr/bin/python3
"""Module 6-max_integer
"""


def max_integer(list=[]):
    """
    Returns:
            The max integer in a list of integers or else
            If the list is empty, the function returns None
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
