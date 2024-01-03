#!/usr/bin/python3
sep = " "
for i in range(100):
    sep = ", "
    if (i < 10):
        print("0{}".format(i), end=sep)
    elif ((i >= 10) and (i < 100)):
        if (i == 99):
            sep = "\n"
        print(i, end=sep)
