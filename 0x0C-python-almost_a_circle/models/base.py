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

    @staticmethod
    def to_json_string(list_dictionaries):
        """this function is callable via the class' name
        Notice how it doesn't require the 'self' parameter.
        Args:
            list_dictionaries (list) - a list of dictionaries
        Return:
            the json string representation of list_dictionaries
        """
        empty = "[]"
        if (list_dictionaries is None):
            return empty
        if (len(list_dictionaries) is None):
            return empty
        jsonrepr = "["
        dct_count = len(list_dictionaries)
        for i in range(dct_count):
            if (i == dct_count - 1):
                sep = ""
            else:
                sep = ", "
            jsonrepr += str(list_dictionaries[i])
            jsonrepr += sep
        jsonrepr += "]"
        return (jsonrepr)

    @staticmethod
    def from_json_string(json_string):
        """given a json string repr of a list of dictionaries...
        returns an actual list of these dictionaries.
        interesting.
            Args:
                json_string (str) - string of dicts
            Return (list):
                list of what the str represents
        """
        if (json_string is None):
            return []
        from json import loads
        return (loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of the list_objs
        to a file. BEWARE!!! The existing file <classname>.json
        will be overwritten!
        Args:
            cls (obj) - a class
            list_objs (list) - a list of instances which inherit
            from Base e.g. list of Rectangle, or Squre instances.
        """
        from json import dump
        save_me = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as fobj:
            if (list_objs is None):
                dump([], fobj)
            else:
                for obj in list_objs:
                    save_me.append(obj.to_dictionary())
                s = Base.to_json_string(save_me)
                dump(s, fobj)
