#!/usr/bin/python3

from typing import List

"""This function returns the minimum number of coins
    to make change for a given amount of money."""


def makeChange(coins: List[int], total: int):
    """
    Args:
        coins (List[int]): A list of coin denominations available for
        making change.
        Each coin denomination must be a positive integer greater than 0.

        total (int): The target total for which we want to
        calculate the minimum number of coins.
    """

    minimum_number_array = [float('inf')] * (total + 1)
    minimum_number_array[0] = 0

    if total <= 0:
        return 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                minimum_number_array[i] = min(minimum_number_array[i],
                                              minimum_number_array[i-coin] + 1)
                print(minimum_number_array[total])
    if minimum_number_array[total] == float('inf'):
        return -1
    else:
        return minimum_number_array[total]
