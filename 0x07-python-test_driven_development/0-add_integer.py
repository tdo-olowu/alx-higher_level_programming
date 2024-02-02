#!/usr/bin/python3
"""add_integer: (int)U(float) x (int)U(float) -> (int)
    wrong output
    wrong types of input, wrong output
    no initialisation for a
"""


def add_integer(a, b=98):
    """This function adds integers.
    Give it an integer or a float, it casts all to integers,
    then returns the sum as an integer"""
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
