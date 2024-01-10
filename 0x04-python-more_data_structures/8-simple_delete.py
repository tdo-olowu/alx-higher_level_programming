#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if (a_dictionary is not None):
        keys = list(a_dictionary)
        if key in keys:
            del a_dictionary[key]
        return a_dictionary
