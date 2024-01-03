#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        sep = ", "
        if ((i == 8) and (j == 9)):
            sep = "\n"
        print("{}{}".format(i, j), end=sep)
