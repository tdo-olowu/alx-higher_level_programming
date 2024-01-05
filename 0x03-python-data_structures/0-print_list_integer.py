#!/usr/bin/python3
def print_list_integer(my_list=[]):
    lngth = len(my_list)
    for i in range(lngth):
        num = my_list[i]
        print("{}".format(num))
