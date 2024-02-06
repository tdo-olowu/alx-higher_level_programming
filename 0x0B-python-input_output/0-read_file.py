#!/usr/bin/python3
"""simple demonstration of file reading.
reads from a file"""


def read_file(filename=""):
    """what could go wrong?
    file doesn't exist, filename isn't string object, 
    etc. This funct returns nothing.
    """
    with open(filename, 'r', encoding="utf-8") as fobj:
        for line in fobj:
            print(line, end='')
