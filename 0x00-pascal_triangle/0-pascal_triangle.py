#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    if (n == 0):
        return []
    if (n == 1):
        return [[1]]
    result = []
    for row in range(1, n+1):
        arr = []
        for col in range(0, row):
            if (col == 0 or col == row - 1):
                arr.append(1)
            else:
                arr.append(result[row-2][col-1] + result[row-2][col])
        result.append(arr)
    return result
