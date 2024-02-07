#!/usr/bin/python3
"""inherits from 
from
"""

def inherits_from(obj, a_class):
    """
        Args:
            obj (object)
            a_class (a class)
        Return:
            bool
    """
    tobj = type(obj)
    if (tobj is a_class):
        return False
    if issubclass(tobj, a_class):
        return True
    for base_class in tobj.__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False
