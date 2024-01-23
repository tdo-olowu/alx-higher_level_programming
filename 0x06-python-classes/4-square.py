#!/usr/bin/python3
"""go go gadget!!!
inspector gadged...who even remembers it?
"""


class Square:
    def __init__(self, size=0):
        """sjkns klj initiative ljnjekdn eldkne
        """
        self.size = size

    def area(self):
        """placeholder jsk s shdbksd
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ jska akjs ask
        askjsa skl
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ lasksa aslk slkkkkkkkkksssssssssssssssssssssssssssssss
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
