#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print x elememts of a list.
    Args:
        my_list: list to print elements from
        x : number of elements to print
    Returns:
        The total number of elements printed
    """
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return total
