#!/usr/bin/python3
"""the basis of all geometry, the base geometry
will build everything else from here"""


class BaseGeometry():
    """BaseGeometry is a class which models
    certain geometries"""

    def area(self):
        """the area of the geometry.
        Return: area"""
        raise Exception("area() is not implemented")
