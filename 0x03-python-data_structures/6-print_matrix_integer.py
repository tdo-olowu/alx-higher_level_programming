#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_count = len(matrix)
    for r in range(row_count):
        row = matrix[r]
        column_count = len(row)
        if (column_count == 0):
            print('')
        for c in range(column_count):
            sep = ' '
            if (c + 1 == column_count):
                sep = '\n'
            item = row[c]
            print("{:d}".format(item), end=sep)
