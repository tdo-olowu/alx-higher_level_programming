#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lngth = len(my_list)
    for i in range(lngth):
        item = my_list[lngth - 1 - i]
        print("{:d}".format(item))
