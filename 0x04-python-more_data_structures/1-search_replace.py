#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list

    Args:
        my_list: initial list
        search: element to replace in the list
        replace: the new element

    Returns:
        the new list
    """
    mod_list = list()
    for i in range(len(my_list)):
        if my_list[i] == search:
            mod_list.append(replace)
        else:
            mod_list.append(my_list[i])

    return mod_list
