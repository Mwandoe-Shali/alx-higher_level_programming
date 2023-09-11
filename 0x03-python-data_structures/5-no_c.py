#!/usr/bin/python3

def no_c(my_string):
    '''removes all characters c and C from a string'''
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the input string
    for char in my_string:
        # Check if the character is not in the set {'c', 'C'}
        if char not in {'c', 'C'}:
            # Append the character to the result string
            result += char
     
    # Return the final result
    return result
