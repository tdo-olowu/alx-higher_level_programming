#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def add_integer(a, b=98):
    """what can go wrong?
    correct mapping is (num, num) -> int, where num is float or int.
    'semantic' exceptions involve providing the wrong type of input, or
    generating the wrong type of output.
    check if a, b are numbers and make sure the output is a number.
    another problem is that a may not be initialised.
    """
    if (type(a) is not int) or (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) or (type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
