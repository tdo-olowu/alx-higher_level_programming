#!/usr/bin/python3
"""this demonstrates how to save an object to text file,
using the json representation"""


def save_to_json_file(my_obj, filename):
    """Usage:
        save_to_json_file([1, 2, 3], "sample_list.txt")
        Args:
            my_obj (obj): a serialisable Python object
            filename (str): the target file's name as a string
        Return:
            no return value
    """
    import json
    with open(filename, 'a', encoding="utf-8") as fobj:
        json.dump(my_obj, fobj)
