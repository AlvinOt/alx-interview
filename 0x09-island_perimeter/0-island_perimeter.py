#!/usr/bin/python3
"""This module calculates island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                """Start by assuming that each land
                cell contributes 4 sides"""

                # Check the neighbors to subtract shared sides
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1  # Subtract top neighbor
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1  # Subtract bottom neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1  # Subtract left neighbor
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1  # Subtract right neighbor

    return perimeter
