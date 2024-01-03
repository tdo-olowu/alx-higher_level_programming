#!/usr/bin/python3
def uppercase(str):
    shift = ord('A')-ord('a')
    for ch in str:
        if ((ord(ch) >= ord('a')) and (ord(ch) <= ord('z'))):
            upp = chr(ord(ch) + shift)
        else:
            upp = ch
        print("{}".format(upp), end="")
    print("", end="\n")
