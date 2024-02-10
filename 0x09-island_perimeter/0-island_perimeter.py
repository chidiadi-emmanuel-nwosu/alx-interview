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
    perimeter = 0

    # Define directions to explore neighbors: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if (
                        x < 0 or x >= len(grid) or y < 0
                        or y >= len(grid[0]) or grid[x][y] == 0
                    ):
                        perimeter += 1

    return perimeter
