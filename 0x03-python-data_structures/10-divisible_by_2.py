#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list.'''
    loop_list = []

    for num in my_list:
        if num % 2 == 0:
            loop_list.append(True)
        else:
            loop_list.append(False)

    return loop_list
