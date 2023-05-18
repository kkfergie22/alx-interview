#!/usr/bin/python3

"""This function returns the minimum number of coins
    to make change for a given amount of money."""


def makeChange(coins, total):
    """
    Args:
        coins (List[int]): A list of coin denominations available for
        making change.
        Each coin denomination must be a positive integer greater than 0.

        total (int): The target total for which we want to
        calculate the minimum number of coins.
    """
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    minimum_number = 0

    for coin in coins:
        if total <= 0:
            break

        if coin <= total:
            minimum_number += total // coin
            total %= coin

    if total > 0:
        return -1

    return minimum_number
