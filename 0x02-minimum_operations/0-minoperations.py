#!/usr/bin/python3
"""
File: min_operations_file.py

Contains a function to calculate the fewest number of operations needed
to achieve a specific number of 'H' characters in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly 'n' H characters in a file.

    Parameters:
    - n: The desired number of H characters in the file.

    Returns:
    - The fewest number of operations required to achieve 'n' H characters
      If 'n' is impossible to achieve, returns 0.
    """
    if n == 1:
        return 0

    nb_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            nb_operations += factor
            n //= factor

        factor += 1

    return nb_operations
