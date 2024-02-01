#!/usr/bin/python3
def magic_string():
    magic_string.count += 1
    return ((magic_string.count * "BestSchool ").strip())
magic_string.count = 0
