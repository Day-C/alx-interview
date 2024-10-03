#!/usr/bin/python3
"""create a pascals triangle."""


def pascal_triangle(n):
    """eate a list of lists of integers that represent a Pascal's Triangle."""

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if len(triangle) < 1:
            row = [1]
            triangle.append(row)
        elif len(triangle) == 1:
            row = [1, 1]
            triangle.append(row)
        else:
            prev_row = i - 1
            row = [1]
            for j in range(len(triangle[prev_row])):
                cur_val = triangle[prev_row][j]
                if j + 1 <=  len(triangle[prev_row]) - 1:
                    next_val = triangle[prev_row][j + 1]
                    row.append(cur_val + next_val)
                else:
                    row.append(1)
            triangle.append(row)
    return triangle
