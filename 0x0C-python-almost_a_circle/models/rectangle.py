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
        width (int) -
        height (int) -
        x (int) -
        y (int) -
        id (int) -
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

    def __str__(self):
        """what to do when print(obj) is called"""
        myid = self.id
        myx = self.x
        myy = self.y
        myw = self.width
        myh = self.height
        return (f"[Rectangle] ({myid}) {myx}/{myy} - {myw}/{myh}")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """usage:
                rect.area()
           Return (int):
                the area of the rectangle object.
        """
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle using the # character
        """
        for n in range(self.y):
            print("")
        for r in range(self.height):
            print((self.x * " ") + (self.width * "#"))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute.
        1st arg should be id, 2nd should be width,
        3rd should be height, 4th should be x
        5th should be y"""
        attrs = ("id", "width", "height", "x", "y")
        if (args is not None) and (len(args) > 0):
            for i in range(len(args)):
                if (i >= len(attrs)):
                    break
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
