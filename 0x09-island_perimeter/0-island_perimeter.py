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
    """
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if (
                        x < 0 or x >= len(grid) or y < 0
                        or y >= len(grid[0]) or grid[x][y] == 0
                    ):
                        perimeter += 1

    return perimeter
