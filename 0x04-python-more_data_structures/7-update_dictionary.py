#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if (not a_dictionary):
        return a_dictionary
    lkeyz = list(a_dictionary)
    if key not in lkeyz:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
