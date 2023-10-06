#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        results of addition of two integers

    Raises:
        TypeError: If either of the arguments is not an integer or a float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
