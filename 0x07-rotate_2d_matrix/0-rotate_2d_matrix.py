#!/usr/bin/python3

"""This module provides a function which rotates a 2D matrix clockwise"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    :param matrix: A list of n lists, each containing n integers.
    :return: None.
    """
    # reverse each row the matrix so that the order changes
    for i in range(len(matrix)):
        matrix[i].reverse()
    # transpose the reversed matrix so that columns become rows
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = (
                matrix[i][j],
                matrix[j][i],
            )
    # reverse each row again to get previous order
    for i in range(len(matrix)):
        matrix[i].reverse()
    # reverse the matrix to get final result
    matrix.reverse()
