#!/usr/bin/python3
"""
0-making_change
"""

def makeChange(coins, total):
    """makeChange
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
