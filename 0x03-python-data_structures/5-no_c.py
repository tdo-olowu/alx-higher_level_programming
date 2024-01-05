#!/usr/bin/python3
def no_c(my_string):
    py_only = ""
    for ch in my_string:
        if (ord(ch) != ord('c')):
            py_only += ch
    return (py_only)
