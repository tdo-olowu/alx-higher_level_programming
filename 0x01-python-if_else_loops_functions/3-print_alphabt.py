#!/usr/bin/python3
for i in range(ord('a'), 1 + ord('z')):
    if ((chr(i) == 'q') or (chr(i) == 'e')):
        continue
    else:
        print("{}".format(chr(i)), end="")
