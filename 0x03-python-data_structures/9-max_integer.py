#!/usr/bin/python3
def max_integer(my_list=[]):
    lngth = len(my_list)
    makks = None
    if (lngth > 0):
        makks = my_list[0]
        for i in range(lngth):
            current_int = my_list[i]
            if (makks < current_int):
                makks = current_int
    return makks
