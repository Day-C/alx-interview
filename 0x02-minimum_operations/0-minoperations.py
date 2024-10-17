#!/usr/bin/python3
"""Get the sortest way to get results."""


def minOperations(n):
    """Calculate the fewest number of operations needed to have "n X"."""

    minimum = 0
    if n <= 0:
        return 0
    if n > 1:
        i = 2
        while n != 1:
            if n % i == 0:
                minimum += i
                n = n // i
                continue
                i = 2
            i += 1
        return minimum
    return 1
