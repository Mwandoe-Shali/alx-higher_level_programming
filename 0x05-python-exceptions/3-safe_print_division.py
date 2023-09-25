#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides an int a by b
    Args:
        a: Number to be divided
        b: Number to divide by
    Returns:
        The result of the division of a by b.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
