#!/usr/bin/python3
"""
Module 1-my_list
This module defines the MyList class that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
