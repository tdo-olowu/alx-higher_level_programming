#!/usr/bin/python3
"""how to return an object represented by a json string
"""


def from_json_string(my_str):
    """Usage:
            from_json_string("[1, 2, 3]")
        Args:
            my_str (str): a string
        Return:
            an object
    """
    import json
    obj = json.loads(my_str)
    return (obj)
