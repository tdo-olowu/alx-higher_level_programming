#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lngtha = len(tuple_a)
    lngthb = len(tuple_b)
    a_0 = 0
    a_1 = 0
    b_0 = 0
    b_1 = 0
    if (lngth_a >= 2):
        a_0 = tuple_a[0]
        a_1 = tuple_a[1]
    elif (lngth_a == 1):
        a_0 = tuple_a[0]
    if (lngth_b >= 2):
        b_0 = tuple_b[0]
        b_1 = tuple_b[1]
    elif (lngth_b == 1):
        b_0 = tuple_b[0]
    apb_tup = (a0 + b0, a1 + b1)
    return apb_tup
