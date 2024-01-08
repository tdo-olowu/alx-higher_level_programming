#!/usr/bin/python3
def new_lin_list(my_list, idx, element):
    cpy = []
    cpy += my_list
    lngth = len(cpy)
    if ((idx >= lngth) or (idx < 0)):
        return cpy
    else:
        new_list = []
        for i in range(lngth):
            if (i == idx):
                cpy.append(element)
            else:
                cpy.append(my_list[i])
        return cpy
