#!/usr/bin/python3
"""LAST BUT NOT THE LIST...
    MY LIST"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
