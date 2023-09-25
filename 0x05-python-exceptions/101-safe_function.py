#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: pointer to a function
        args: Arguments for function fct.

    Returns:
        result of the function call
        If an error occurs - None.
    """
    try:
        return fct(*args)
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return None
