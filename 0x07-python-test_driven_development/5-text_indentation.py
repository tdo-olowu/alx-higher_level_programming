#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def text_indentation(text):
    """what errors can aris?
    existence - text doesn't exist.
    type - text is not a string
    """
    type_err_msg = "text must be a string"
    if (type(text) is not str):
        raise TypeError(type_err_msg)
    prev_ch = text[0]
    for ch in text:
        if prev_ch in [".", "?", ":"]:
            print("\n")
            if ch in [" ", "\t"]:
                print("", end="")
        else:
            print(ch, end="")
        prev_ch = ch
    print("")
