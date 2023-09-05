#!/usr/bin/python3
def print_last_digit(number):
    # Get the absolute value of the number to handle negative numbers
    abs_number = abs(number)

    # Get the last digit using the modulo operator (%)
    last_digit = abs_number % 10

    # Print the last digit
    print(last_digit)

    # Return the last digit
    return last_digit
