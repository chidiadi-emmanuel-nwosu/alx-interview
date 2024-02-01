#!/usr/bin/python3
"""
0-making_change
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins required to
    make change for a given total amount.

    Args:
    - coins (list of int): Available denominations of coins.
    - total (int): Total amount for which change needs to be made.

    Returns:
    - int: The minimum number of coins required to
           make change for the total amount.
           Returns -1 if it's not possible to make
           change with the given coins.
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        balance = total % coin

        if balance == 0:
            return count
        total = balance

    return -1
