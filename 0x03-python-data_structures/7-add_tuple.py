#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lngth_a = len(tuple_a)
    lngth_b = len(tuple_b)
    a0 = 0
    a1 = 0
    b0 = 0
    b1 = 0
    if (lngth_a >= 2):
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    elif (lngth_a == 1):
        a0 = tuple_a[0]
    if (lngth_b >= 2):
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    elif (lngth_b == 1):
        b0 = tuple_b[0]
    apb_tup = (a0 + b0, a1 + b1)
    return apb_tup
