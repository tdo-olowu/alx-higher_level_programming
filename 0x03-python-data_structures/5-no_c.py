#!/usr/bin/python3
def no_c(my_string):
    py_only = ""
    c_up = ord('C')
    c_dn = ord('c')
    for ch in my_string:
        if ((ord(ch) != c_dn) and (ord(ch) != c_up)):
            py_only += ch
    return py_only
