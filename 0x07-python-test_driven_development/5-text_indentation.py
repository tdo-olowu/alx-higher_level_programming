#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def text_indentation(text):
    """what errors can aris?
    existence - text doesn't exist.
    type - text is not a string
    """
    type_err_msg = "text must be a string"
    if type(text) is not str:
        raise TypeError(type_err_msg)
    for ch in text:
        if ch in [".", "?", ":"]:
            print("\n\n", end="")
        else:
            print("{}".format(ch), end="")
    print("\n", end="")
