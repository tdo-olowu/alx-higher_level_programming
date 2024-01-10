#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # check for None dictionary here
    if (value not in list(a_dictionary.values())):
        return a_dictionary
    pairs = list(a_dictionary.items())
    lngth = len(pairs)
    for i in range(lngth):
        key = pairs[i][0]
        val = pairs[i][1]
        if (val == value):
            del a_dictionary[key]
    return a_dictionary
