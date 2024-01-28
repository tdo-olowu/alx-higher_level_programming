#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def say_my_name(first_name, last_name=""):
    """what problems can happen?
    existence - no first name given, no last name given
    type errors - type of first name or last name is not string.
    """
    str_terr_msg = " must be a string"
    if type(first_name) is not str:
        raise TypeError("first_name" + str_terr_msg)
    if type(last_name) is not str:
        raise TypeError("last_name" + str_terr_msg)
    print("My name is {} {}".format(first_name, last_name))
