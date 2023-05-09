#!/usr/bin/python3

"""This module provides a function which rotates a 2D matrix clockwise"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    :param matrix: A list of n lists, each containing n integers.
    :return: None.
    """
    # transpose matrix
    transpose_matrix = [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]
    # swap the columns of the transposed matrix with it's rows
    for i in range(len(transpose_matrix)):
        transpose_matrix[i][0], transpose_matrix[i][-1] = (
            transpose_matrix[i][-1],
            transpose_matrix[i][0],
        )
    # replace the original matrix with the transposed matrix
    matrix[:] = transpose_matrix
