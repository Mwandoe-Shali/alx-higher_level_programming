#!/usr/bin/python3
def magic_calculation(a, b):
    """bytecode magic calculator."""
    from magic_calculation_102 import add, sub

    if a < b:
        magic_sum = add(a, b)
        for i in range(4, 6):
            magic_sum = add(magic_sum, i)
        return (magic_sum)
    else:
        return (sub(a, b))
