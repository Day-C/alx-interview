#!/usr/bin/python3
"""calculate islands perlimeter."""


def island_perimeter(grid):
    """calculate the perimer of the island represented by grid."""

    perimeter = 0
    if len(grid) > 0:
        for line in range(len(grid) - 1):
            for cell in range(len(grid[line]) - 1):
                if grid[line][cell] == 1:
                    if (cell - 1) >= 0:
                        if grid[line][cell - 1] == 0:
                            # increment
                            perimeter += 1
                    if (cell + 1) <= (len(grid[line]) - 1):
                        if grid[line][cell + 1] == 0:
                            # increment
                            perimeter += 1
                    if line - 1 >= 0:
                        if grid[line - 1][cell] == 0:
                            # increment
                            perimeter += 1
                    if line + 1 <= (len(grid) - 1):
                        if grid[line + 1][cell] == 0:
                            # increment
                            perimeter += 1
    return perimeter
