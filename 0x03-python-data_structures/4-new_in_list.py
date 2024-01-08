#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = []
    lngth = len(my_list)
    if ((idx >= lngth) or (idx < 0)):
        cpy += my_list
        return cpy
    else:
        for i in range(lngth):
            if (i == idx):
                cpy.append(element)
            else:
                cpy.append(my_list[i])
        return cpy
