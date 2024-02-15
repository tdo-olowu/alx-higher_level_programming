#!/usr/bin/python3
"""Rectangle class, which inherits from the Base class
"""


import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
rect = __import__('rectangle').Rectangle
class Square(rect):
    """models a Square digitally.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializer"""
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """what to give when str() or print() ask
        """
        myid = self.id
        myx = self.x
        myy = self.y
        mysz = self.width
        return (f"[Square] ({myid}) {myx}/{myy} - {mysz}")

    @property
    def size(self):
        """I'm forbidden from directly creating a sz attribute
        it's assumed that the width and height are equal"""
        return (super().width)

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes for the square object.
            Args:
                *args - a list of arguments, w/o keywords.
                in order, it's id, size, x, y
                **kwargs - a dictionary of arguments
        """
        attrs = ("id", "size", "x", "y")
        if (args is not None) and (len(args) > 0):
            for i in range(len(args)):
                if (i >= len(attrs)):
                    break
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """This returns the dictionary representation of the obj,
        for the sake of serialising in json format.
        Return:
            the serialisable dictionary representation of the obj
        """
        dct_repr = {}
        sought_attr = ("id", "size", "x", "y")
        for attr in sought_attr:
            if hasattr(self, attr):
                dct_repr[attr] = getattr(self, attr)
            else:
                dct_repr[attr] = None
        return (dct_repr)
