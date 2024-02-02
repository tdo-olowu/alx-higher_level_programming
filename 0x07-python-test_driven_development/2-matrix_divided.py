#!/usr/bin/python3
"""matrix_divided: (M)U(int) -> (M)
    existence issues - no matrix given, no div given
    type issues - matrix or div is wrong type (incl None)
    value issues - matrix is not all numbers or aligned, or div is 0
"""


def matrix_divided(matrix, div):
    """matrix_divided - a function to scale a matrix by 1/div
        Return (list): list of lists
        """
    new_matrix = []
    row = []
    div_type_error_msg = "div must be a number"
    mat_type_error_msg = "matrix must be a matrix (list of lists) "
    mat_type_error_msg += "of integers/floats"
    row_misalign_msg = "Each row of the matrix must have the same size"
    prev_col_count = 0

    if (type(div) is not int) and (type(div) is not float):
        raise TypeError(div_type_error_msg)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(mat_type_error_msg)

    """who's to say matrix[0] exists?"""
    if (len(matrix) < 1) or (type(matrix[0]) is not list):
        raise TypeError(mat_type_error_msg)
    prev_col_count = len(matrix[0])

    for r in range(len(matrix)):
        row = matrix[r]
        """the order of these checks is important, cause of len"""
        if type(row) is not list:
            raise TypeError(mat_type_error_msg)
        if (prev_col_count != len(row)):
            raise TypeError(row_misalign_msg)

        for c in range(len(row)):
            tp = type(row[c])
            if (tp is not int) and (tp is not float):
                raise TypeError(mat_type_error_msg)
        row = list(map(lambda x: round(x/div, 2), row))
        new_matrix.append(row)

        prev_col_count = len(row)

    return (new_matrix)
