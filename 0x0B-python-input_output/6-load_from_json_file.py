#!/usr/bin/python3
"""demonstrates how to load an object from a json file, in Python
"""


def load_from_json_file(filename):
    """Usage:
    """
    import json
    try:
        with open(filename, 'r', encoding="utf-8") as fobj:
            obj = json.load(fobj)
    except FileNotFoundError:
        obj = []
        with open(filename, 'w', encoding="utf-8") as fobj:
            json.dump(obj, fobj)
    return (obj)
