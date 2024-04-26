#!/usr/bin/python3
"""Peak-finding algorithm
A peak is a y-value not less than its neighbouring y-vals"""


def find_peak(list_of_integers):
    """naive O(n) algorithm"""
    lngth = len(list_of_integers)
    if (lngth < 3):
        # no peak?
        return None

    for i in range(lngth):
        now = list_of_integers[i]
        if (i == 0):
            pass
        elif (i == lngth):
            prev = list_of_integers[i-1]
            if (now >= prev):
                return now
        else:
            prev = list_of_integers[i-1]
            nxt = list_of_integers[i+1]
            if (now >= prev) and (now >= nxt):
                return now
