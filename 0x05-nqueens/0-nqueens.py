#!/usr/bin/python3
"""N Queens Challenge"""

import sys


def is_safe(row, col, queens):
    """Check if placing a queen at position (row, col) is safe"""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_n_queens(n):
    """Solve the N Queens problem"""
    solutions = []

    def backtrack(row, queens):
        """Use backtracking to find all solutions"""
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append([row, col])
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions


def print_solutions(solutions):
    """Print all solutions"""
    for queens in solutions:
        print(queens)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)
