#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    lngth = len(my_list)
    if ((idx < 0) or (idx >= lngth)):
        return my_list
    else:
        for i in range(lngth):
            if (i != idx):
                new_list.append(my_list[i])
    return (new_list)
