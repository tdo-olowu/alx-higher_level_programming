#!/usr/bin/python3
import sys
av = sys.argv[:]
ac = len(av) - 1
psum = 0
if (ac > 1):
    for i in range(1, ac + 1):
        psum += int(av[i])
print("{}".format(psum))
