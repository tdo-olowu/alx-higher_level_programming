#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix is None):
        return None
    neo = []
    row = []
    nrows = len(matrix)
    for r in range(nrows):
        if (matrix[r] is None):
            continue
        transf = map(lambda x: x**2, matrix[r])
        row = list(transf)
        neo.append(row)
    return neo
