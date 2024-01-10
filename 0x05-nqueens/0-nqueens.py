#!/usr/bin/python3
"""n queens problem"""

import sys


def is_safe(board, row, col, N):
    """ Check if there is a queen
    in the same column"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    """solve n queens"""
    board = [[0] * N for _ in range(N)]
    solutions = []

    def backtrack(row):
        """backtrack function"""
        if row == N:
            # Found a valid solution, record the positions
            queens = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        queens.append([i, j])
            solutions.append(queens)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

    return solutions


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)
