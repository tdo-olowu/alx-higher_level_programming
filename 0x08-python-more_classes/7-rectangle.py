#!/usr/bin/python3
"""RECTANGLE: Explore object-oriented programming in Python via
Rectangles, courtesy ALX
"""


class Rectangle:
    """a simple class to model rectangles.

    Attributes:
        number_of_instances (int): keeps track of instances.
        print_symbol: symbol for string repr. May be any type.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialiser for when a new instance is created.
        Attributes:
            width (int): how many cells wide the rectangle is
            height (int): how many cells tall the rectangle is
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """the rectangle in intuitive string form.
        Return (str):
            the rectangle's string form
        """
        if (self.__width == 0) or (self.__height == 0):
            return ""
        else:
            str_rep = ""
            ps = Rectangle.print_symbol
            if "print_symbol" in list(self.__dict__.keys()):
                ps = str(self.print_symbol)
            for i in range(self.__height):
                end = "\n"
                if (i == self.__height - 1):
                    end = ""
                str_rep += (self.__width * ps) + end
            return (str_rep)

    def __repr__(self):
        """internal representation of the rectangle.
        especially useful when passed to eval() function.
        Return (str):
            a str representing the repr of the rectangle
        """
        w = self.__width
        h = self.__height
        return ("Rectangle({}, {})".format(w, h))

    def __del__(self):
        """code is executed when instance is deleted.
        normally we'd worry about the number_of_inst being < 0
        but it's hard to see how that could happen, unless we failed
        to increment the number_of_inst upon instance creation,
        or we decrement too much.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter for the width.
        Return (int): the width of the particular rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height
        Return (int):
            the height of the particular rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle is total number of cells.
        Return (int): area of the rectangle width x height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of rectangle is total length of boundary
        Return (int): perimeter of rectangle 2 * (width + height)
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * (self.__width + self.__height))
