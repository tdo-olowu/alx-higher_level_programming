#!/usr/bin/python3
"""This is a Base class. It is meant to represent...
"""


class Base():
    """class Base
        The 'base' of all other classes in this project.
        Its goal is to manage the id attribute in all future classes,
        and to avoid duplicating the same code (by extension, same bugs)
        Attributes:
            __nb_objects (int) - private class attr counting number
            of instances of Base. Must be non-negative.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialiser for a Base instance.
            Args:
                id (integer) - an id number. assumed to be int.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
