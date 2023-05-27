#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """Function to calculate island perimeter.
    args - grid a list of lists
    retuns - perimeter"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Deduct 1 side if neighboring cell is land
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Deduct 1 side if neighboring cell is land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Deduct 1 side if neighboring cell is land
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Deduct 1 side if neighboring cell is land

    return perimeter
