#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """ Calculate the perimeter of an island represented by a grid.

    Args:
        grid (list of list of int): A 2D grid representing the island
                                    where each cell is either 0 or 1.

    Returns:
        int: The perimeter of the island.

    The function calculates the perimeter of the island by traversing
    through the grid and counting the number of land cells(cells with value 1).
    The perimeter is then computed based on the number of land cells adjacent
    to water (cells with value 0).
    """
    count = 0
    for row in grid:
        for cell in row:
            if cell == 1:
                count += 1

    return count * 2 + 2
