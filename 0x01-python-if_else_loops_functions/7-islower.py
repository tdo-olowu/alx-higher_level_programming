#!/usr/bin/python3
def islower(c):
    a = ord('a')
    z = ord('z')
    ch = ord(c)
    if ((ch >= a) and (ch <= z)):
        return True
    return False
