#!/usr/bin/python3
"""serialising a class in python
"""


def class_to_json(obj):
    """Expresses a class in serialisable form
    Args:
        obj (any): should have serialisable attrs
    Return:
        the serialisable string of the object?
    """
    dct = {}
    objdct = obj.__dict__
    for k, v in objdct.items():
        dct[k] = v
    return (dct)
