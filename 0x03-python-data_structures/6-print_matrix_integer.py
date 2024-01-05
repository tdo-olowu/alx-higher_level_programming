#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_count = len(matrix)
    for r in range(row_count):
        row = matrix[r]
        column_count = len(row)
        for c in range(column_count):
            sep = ' '
            if (c + 1 == column_count):
                sep = '\n'
            item = row[c]
            print("{}".format(item), end = sep)

if __name__ == "__main__":
    matrix = [
            [1, 2, 3, 4],
            [5, 6, 7],
            [8, 9],
            [10],
            []
            ]
    print_matrix_integer(matrix)
