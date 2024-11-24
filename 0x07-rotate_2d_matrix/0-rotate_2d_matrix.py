#!/usr/bin/python3
"""Rotate a matrix 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """retate a matrix."""

    # create a matrix to mimic the original in structure
    c_matrix = []
    for i in range(len(matrix)):
        c_matrix.append([])

    # make changes to the cloned matrix
    for j in range(len(matrix[0])):
        n = 0
        # loop from last to first each time
        for i in range(len(matrix) - 1, -1, -1):
            c_matrix[j].append(matrix[i][j])

    # copy from the cloned matrix to the original
    for i in range(len(c_matrix)):
        for k in range(len(c_matrix)):
            matrix[i][k] = c_matrix[i][k]
