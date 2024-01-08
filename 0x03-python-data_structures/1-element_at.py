#!/usr/bin/python3
def element_at(my_list, idx):
    lngth = len(my_list)
    if (idx < 0):
        return None
    elif (idx >= lngth):
        return None
    else:
        return my_list[idx]
