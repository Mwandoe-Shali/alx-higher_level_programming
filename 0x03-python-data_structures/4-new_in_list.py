#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''
    replaces an element in a list at a specific position
    without modifying the original list (like in C).
    '''
    if idx < 0 or idx >= len(my_list):
        temp = my_list.copy()
        return temp
    else:
        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list    
     
