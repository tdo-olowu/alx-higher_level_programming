#!/usr/bin/python3
def roman_to_int(roman_string):
    # error checking
    if ((type(roman_string) != type("str")) or (roman_string == None)):
        return 0
    table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'M':1000}
