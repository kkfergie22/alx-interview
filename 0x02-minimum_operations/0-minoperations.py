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
    operations_counter = 0
    current_counter = 1
    clipboard = 0

    while current_counter <= n:
        if n % current_counter == 0:
            clipboard = current_counter
            n = n / current_counter
        else:
            current_counter += 1
            continue
        if clipboard != 0:
            operations_counter += 2
            current_counter = clipboard
        clipboard = 0
    if n > 1:
        return 0

    return operations_counter
