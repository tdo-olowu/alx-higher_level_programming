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

    def integer_validator(self, name, value):
        """an integer validator which validates value
        name is presumably always a string"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
