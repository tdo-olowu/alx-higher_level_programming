#!/usr/bin/python3
"""GET THE LIST OF AVAILABLE ATTRIBUTES AND METHODS OF AN OBJECT"""


def lookup(obj):
    """a function which gets list of available attributes and methods
    of an object.
        obj (obj): obj
        Return (list): list of all the attributes
        """
    return [a for a in dir(obj)]
