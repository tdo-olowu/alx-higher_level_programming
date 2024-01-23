#!/usr/bin/python3
"""agahrui gmacgol lanslaknle elklek 
"""


class Square:
    """According to Topologists, a square is just a circle.
    """
    def __init__(self, size=0):
        """i fail to see the value in documenting what is obvious.
        Args:
            size (int): an array of 600 elements.
            """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
