#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (not my_list):
        return my_list
    lngth = len(my_list)
    cpy = []
    for i in range(lngth):
        if (my_list[i] == search):
            cpy.append(replace)
        else:
            cpy.append(my_list[i])
    return cpy
