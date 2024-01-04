#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv[:]
    argc = len(av) - 1
    msg = "arguments"
    punct = ":"
    if (argc == 1):
        msg = msg[:-1]
    if (argc == 0):
        punct = "."
    print("{} {}{}".format(argc, msg, punct))
    if (argc > 0):
        for i in range(1, argc + 1):
            print("{}: {}".format(i, av[i]))
