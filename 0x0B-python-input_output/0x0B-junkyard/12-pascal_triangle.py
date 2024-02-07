#!/usr/bin/python3
"""implementation of pascal's triangle
    the relation is (n, c) = (n-1, c) + (n-1, c-1)
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the pascal's triangle up to n rows.
    Args:
        n (int): the number of rows of the triangle
    Return (list of lists):
        should be a zero-padded matrix but whatever.
        returns the pascal's triangle
    """
    if (n <= 0):
        return []

    pascalz = []
    prev_row = []
    for r in range(n):
        row = []
        # please guarantee that prev_row starts at 0 length
        for c in range(r + 1):
            # r is length of prev row. starts at 0
            if (c == 0) or (c == r):
                row.append(1)
            else:
                row.append(prev_row[c] + prev_row[c - 1])
        print("Row {} {}".format(r, row))
        pascalz.append(row)
        # prev_row = row?
        prev_row = row[:]
    return (pascalz)

if __name__=="__main__":
    pascal_triangle(10)
