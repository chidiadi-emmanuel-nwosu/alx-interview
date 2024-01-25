#!/usr/bin/python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """
    rortates a 2D matrix
    """
    length = len(matrix)

    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    for row in matrix:
        row.reverse()
