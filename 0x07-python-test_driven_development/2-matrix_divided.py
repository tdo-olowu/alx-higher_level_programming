#!/usr/bin/python3
"""CODE DOCUMENTATION GOES HERE.
"""


def matrix_divided(matrix, div):
    """what problems could arise?
    existence problems - no matrix given, no div given.
    type problems - matrix is the wrong type (incl None), or
    div is the wrong type.
    matrix must be a list and div must be a number
    value problems - matrix is not a proper matrix.
        either it has wrong dimensions (not all rows same length) or
        it has non-numerical entries.
        div is not a non-zero number.
    memory problems? Haha, this isn't C. Hopefully this won't be an issue.
    """
    new_matrix = []
    row = []
    mat_type_error_msg = "matrix must be a list of lists"
    prev_col_count = 0

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(mat_type_error_msg)

    if type(matrix[0]) is list):
        prev_col_count = len(matrix[0])
    for r in range(len(matrix)):
        row = matrix[r]
        if type(row) is not list:
            raise TypeError(mat_type_error_msg)
        for c in range(len(row)):
            tp = type(row[c])
            if (tp is not int) or (tp is not float):
                raise TypeError(mat_type_error_msg)
            row = list(map(lambda x:x/div, row[c]))
            new_matrix.append(row)

        if (prev_col_count != len(matrix[r]):
                raise TypeError(mat_type_error_msg)
        prev_col_count = len(matrix[r])

    return (new_matrix)
