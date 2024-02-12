#!/usr/bin/python3
"""Rectangle class, which inherits from the Base class
"""


import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
base = __import__('base').Base
class Rectangle(base):
    """
    class Rectangle:
        inherits from Base, which is a simple class that records
        only id.
    Attributes:
        no attributes for Rectangle
    Methods:
        width
        height
        x
        y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """the initialiser of the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
