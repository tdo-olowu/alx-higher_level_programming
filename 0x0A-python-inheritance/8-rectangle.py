#!/usr/bin/python3
"""the basis of all geometry, the base geometry
will build everything else from here"""


BGeo = __import__("7-base_geometry").BaseGeometry


class Rectangle(BGeo):
    """a square which inherits from the base Geo"""
    def __init__(self, width, height):
        """the initialiser"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
