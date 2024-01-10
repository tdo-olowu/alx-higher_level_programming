#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is not None):
        keyz = a_dictionary.keys()
        lkeyz = list(keyz)
        lkeyz.sort()
        for a in lkeyz:
            val = a_dictionary[a]
            print("{}: {}".format(a, val))
