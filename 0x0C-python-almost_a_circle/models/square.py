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
        self.size = size
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
        """getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size"""
        super().width(self, self.size)
        super().height(self, self.size)
