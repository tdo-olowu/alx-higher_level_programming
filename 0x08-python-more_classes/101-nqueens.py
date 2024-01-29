#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv[:]
    argc = len(av) - 1

    if (argc != 1):
        print("Usage: nqueens N")
        exit(1)
    n = av[argc]
    try:
        n = int(n)
    except:
        print("N must be a number")
        exit(1)

    if (n < 4):
        print("N must be at least 4")
        exit(1)

    pass
