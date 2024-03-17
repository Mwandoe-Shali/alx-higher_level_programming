#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is an element which is not smaller than its neighbors.
    For corner elements, we need to consider only one neighbor.
    """
    # If the list is empty, return None
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])):
            return list_of_integers[mid]
        
        # If the element at mid is not a peak and its left neighbor is greater than it,
        # then the left half must have a peak
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        
        # Otherwise, the right half must have a peak
        else:
            low = mid + 1
    
    return None
