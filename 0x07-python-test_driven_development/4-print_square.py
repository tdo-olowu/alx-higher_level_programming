#!/usr/bin/python3
"""print_square: (int) -> stdout
    existence - non-existent size
    type error - wrong type of size
    value error - negative value or float value.
"""


def print_square(size):
    """prints square via ASCII
    uses the hash character.
    """
    size_terr_msg = "size must be an integer"
    size_verr_msg = "size must be >= 0"
    if type(size) is not int:
        raise TypeError(size_terr_msg)
    if (size < 0):
        raise ValueError(size_verr_msg)

    for i in range(size):
        print(size * "#")
