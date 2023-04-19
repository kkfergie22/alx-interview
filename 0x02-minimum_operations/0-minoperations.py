#!/usr/bin/python3

"""This function calculates the minimum number of operations
to achieve a result"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n
    H characters in the file.

    Args:
        n(int): The desired number of H characters in the file.

    Returns:
        int: The fewest number of operations needed to obtain n H characters.
    """

    if n <= 1:
        return 0

    num_ops = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            num_ops += factor
            n //= factor
        factor += 1

    if n > 1:
        num_ops += n

    return num_ops
