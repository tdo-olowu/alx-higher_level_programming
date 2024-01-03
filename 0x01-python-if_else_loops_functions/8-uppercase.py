#!/usr/bin/python3
def uppercase(str):
    shift = ord('A')-ord('a')
    for ch in str:
        upp = chr(ord(ch) + shift)
        print(upp, end="")
    print("", end="\n")
