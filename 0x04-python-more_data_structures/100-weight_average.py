#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        divider = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            divider += (tup[1])
        return (num/divider)
    return 0
