#!/usr/bin/python3
"""the basis of all geometry, the base geometry
will build everything else from here"""


Rect = __import__("9-rectangle").Rectangle


class Square(Rect):
    """a square which inherits from the base Geo"""
    def __init__(self, size):
        """the initialiser"""
        self.__size = size
        super().__init__(size, size)
