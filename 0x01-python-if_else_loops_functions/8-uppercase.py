#!/usr/bin/python3
def uppercase(str):
    shift = ord('A')-ord('a')
    for ch in str:
        upp = chr(ord(ch) + shift)
        print("{}".format(upp), end="")
    print("", end="\n")
