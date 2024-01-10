#!/usr/bin/python3
def roman_to_int(roman_string):
    # error checking
    if ((not isinstance(roman_string, str)) or (roman_string is None)):
        return 0
    # if input is correct
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_ch = None
    lngth = len(roman_string)
    for i in range(lngth):
        ch = roman_string[i]
        if ((ch == 'V') or (ch == 'X')):
            if (prev_ch == 'I'):
                val = table[ch] - 1
                total = total - 1
            else:
                val = table[ch]
            total += val
        else:
            total += table[ch]
        prev_ch = ch
    return total
