#!/usr/bin/python3
"""what is a module?
    a module is a generalization of the notion of vector space
    in which the field of scalars is replaced by a ring.
    The concept of module generalizes also the notion of abelian group,
    since the abelian groups are exactly the modules over the ring of integers.
    """


class Square:
    """what is a square?
    a square is a regular quadrilateral, or you can call it...
    a rhombus with
        a 90 degree angle
        """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """how do you computer
        the area of a square?
        """
        return (self.__size ** 2)
