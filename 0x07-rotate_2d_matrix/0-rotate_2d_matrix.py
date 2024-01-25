#!/usr/bin/python3
"""
rotate_2d_matrix module;
provides a function for rotating a 2D matrix.
"""


def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """
    Rotates a given 2D matrix in-place.

    Args:
        matrix: The input 2D matrix to be rotated.
    """
    length = len(matrix)

    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
