#!/usr/bin/python3
"""say_my_name: (ASCII)x(ASCII) -> stdout
    existence - no first name given, no last name
    type - type of either name is not string
    what else?
"""


def say_my_name(first_name, last_name=""):
    """say_my_name: say my name, say my name...
        give it first name and last name, and it greets you
    """
    str_terr_msg = " must be a string"

    if (type(first_name) is not str):
        raise TypeError("first_name" + str_terr_msg)
    if type(last_name) is not str:
        raise TypeError("last_name" + str_terr_msg)

    print("My name is {} {}".format(first_name, last_name))
