#!/usr/bin/python3
"""n queens solution."""
import sys


def is_safe(board, row, col):
    """chech if a queen can be places at (row in a column),
    without being attacked"""

    for i in range(row):
        if board[i] == col or board[i] - 1 == col - row:
            return False
        if board[i] + 1 == col + row:
            return False
    return True


def solve_n_queens(n, row, board, result):
    """recursively solve the n queens problem."""

    print("in porgress {}n and {}row".format(n, row))
    if row == (n - 1):
        # print solution
        result.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            print([col, row])
            solve_n_queens(n, row+1, board, result)


def main():
    """main function to run program."""

    if len(sys.argv) != 2:
        print("Usage: nqueens number")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    result = []
    solve_n_queens(n, 0, board, result)
    pr


if __name__ == "__main__":
    main()
