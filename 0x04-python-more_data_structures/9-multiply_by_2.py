#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if (not a_dictionary):
        return a_dictionary
    new_dict = {}
    a_keys = list(a_dictionary)
    for k in a_keys:
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
