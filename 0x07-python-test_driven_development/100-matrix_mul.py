#!/usr/bin/python3
"""matrix_mul: (A) X (A) -> (A)
    type issues - inputs are not "aligned" rows of ints
    dimension issues - matrices aren't multipliable.
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrixes,
        produces a matrix in return.
    """
    mterr_msg_bal = " must be a list"
    mterr_msg_lol = " must be a list of lists"
    mverr_msg_cbe = " can't be empty"
    mterr_msg_iof = " should contain only integers or floats"
    mterr_msg_ssza = "each row of "
    mterr_msg_sszb = " must be of the same size"
    mverr_msg_cbm = "m_a and m_b can't be multiplied"

    """verify m_a..."""
    if (type(m_a) is not list):
        raise TypeError("m_a" + mterr_msg_bal)
    if (len(m_a) == 0) or (len(m_a[0]) == 0):
        raise ValueError("m_a" + mverr_msg_cbe)
    else:
        """this loop does many checks at once"""
        prev_len = len(m_a[0])
        for r in range(len(m_a)):
            row = m_a[r]
            if (type(row) is not list):
                raise TypeError("m_a" + mterr_msg_lol)
            if (prev_len != len(row)):
                raise TypeError(mterr_msg_ssza + "m_a" + mterr_msg_sszb)
            """verify that the row contains only numbers"""
            for c in range(len(row)):
                tp = type(row[c])
                if (tp is not int) and (tp is not float):
                    raise TypeError("m_a" + mterr_msg_iof)
            prev_len = len(row)

    """then verify m_b..."""
    if (type(m_b) is not list):
        raise TypeError("m_b" + mterr_msg_bal)
    if (len(m_b) == 0) or (len(m_b[0]) == 0):
        raise ValueError("m_b" + mverr_msg_cbe)
    else:
        """this loop does many checks at once"""
        prev_len = len(m_b[0])
        for r in range(len(m_b)):
            row = m_b[r]
            if (type(row) is not list):
                raise TypeError("m_b" + mterr_msg_lol)
            if (prev_len != len(row)):
                raise TypeError(mterr_msg_ssza + "m_b" + mterr_msg_sszb)
            """verify that the row contains only numbers"""
            for c in range(len(row)):
                tp = type(row[c])
                if (tp is not int) and (tp is not float):
                    raise TypeError("m_b" + mterr_msg_iof)
            prev_len = len(row)

    """then check if m_a and m_b can be multiplied..."""
