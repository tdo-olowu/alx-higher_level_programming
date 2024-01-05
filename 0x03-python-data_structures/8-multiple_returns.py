#!/usr/bin/python3
def multiple_returns(sentence):
    lngth = len(sentence)
    first = None
    if (lngth > 0):
        first = sentence[0]
    pair = (lngth, first)
    return pair
