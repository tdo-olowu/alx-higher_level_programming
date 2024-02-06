#!/usr/bin/python3
"""demonstration of how to append a string to the end of a 
text file in python."""


def append_write(filename="", text=""):
    """Usage:
            append_write('sample.txt', 'Hello world')
        Args:
            filename (str): the name of the file as a string
            text (str): the text to append to the end of the file
        Return (int):
            the number of bytes written
    """
    with open(filename, 'a', encoding='utf-8') as fobj:
        bytes_written = fobj.write(text)
    return (bytes_written)
