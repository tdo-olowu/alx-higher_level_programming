#!/usr/bin/python3
"""simple demonstration of how to overwrite a file
with sample text
"""


def write_file(filename="", text=""):
    """write_file(sample.txt, 'this is example')
    what could go wrong? perhaps the filename isn't
    string type, or file does not exist or we don't have
    the proper permissions, or the function corrupts the file
    while writing to it, or we don't have enough memory to deal
    with the file

    Args:
        filename (str): the name of the file, as a string
        text (str): the text to write to the string.
    Return (int):
        the number of bytes written
    """
    with open(filename, 'w', encoding="utf-8") as fobj:
        count = fobj.write(text)
    return (count)
