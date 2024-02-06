#!/usr/bin/python3
"""returning the JSON representation of an object,
as a string"""


def to_json_string(my_obj):
    """Usage:
            to_json_string({'a':1, 'b':2})
        Args:
            my_obj (any): a serialisable object e.g. list, dict
        Return (str):
            the string representation of that object in json
    """
    import json
    return json.dumps(my_obj)
