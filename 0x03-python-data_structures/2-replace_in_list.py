#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lngth = len(my_list)
    if ((idx >= lngth) or (idx < 0)):
        return my_list
    else:
        my_list[i] = element
        return my_list
