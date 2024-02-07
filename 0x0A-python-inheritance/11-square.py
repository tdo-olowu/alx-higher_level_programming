#!/usr/bin/python3
"""the basis of all geometry, the base geometry
will build everything else from here"""


Rect = __import__("9-rectangle").Rectangle


class Square(Rect):
    """a square which inherits from the base Geo"""
    def __init__(self, size):
        """the initialiser"""
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """print implementation"""
        width = self.__size
        height = width
        return ("[Rectangle] {}/{}".format(width, height))

    def area(self):
        """implementing area"""
        return (self.__size ** 2)
