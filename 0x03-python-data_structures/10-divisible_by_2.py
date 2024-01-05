#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_pool = []
    lngth = len(my_list)
    for i in range(lngth):
        if (my_list[i] % 2 == 0):
            bool_pool.append(True)
        else:
            bool_pool.append(False)
    return bool_pool
