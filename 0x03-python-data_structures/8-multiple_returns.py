#!/usr/bin/python3

def multiple_returns(sentence):
    # returns a tuple with the length of a string
    # and its first character.
    first_ch = sentence[0]
    if sentence == '':
        first_char = None

    return (len(sentence), first_char)
