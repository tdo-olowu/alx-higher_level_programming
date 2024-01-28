#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def print_square(size):
    """issues
    existence - size does not exist.
    type - not an integer
    range - negative integer
    """
    size_terr_msg = "size must be an integer"
    size_verr_msg = "size must be >= 0"
    if (type(size) is not int):
        raise TypeError(size_terr_msg)
    if (size < 0):
        raise ValueError(size_verr_msg)
    for i in range(size):
        print(size * "#")
