#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    lngth = len(my_list)
    if ((idx < 0) or (idx >= lngth)):
        return my_list
    else:
        new_list = my_list[:idx] + my_list[1 + idx:]
        del my_list[idx]
    return (new_list)
