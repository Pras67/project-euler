"""
Question 28: Number Spiral Diagonals
URL: https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction an 5 by 5
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Measured Runtime: ~0.000040s
"""

import time


def solve(n: int = 1001) -> int:
    """Calculates the sum of numbers on the diagonals of an n x n number spiral."""
    total_sum = 1
    # Each odd side length s adds 4 corners: s^2, s^2 - (s-1), s^2 - 2(s-1), s^2 - 3(s-1)
    # Sum of 4 corners for side s = 4 * s^2 - 6 * (s - 1)
    for s in range(3, n + 1, 2):
        total_sum += 4 * (s * s) - 6 * (s - 1)
    return total_sum


def solve_formula(n: int = 1001) -> int:
    """Alternative O(1) closed-form solution for the diagonal sum of an n x n number spiral."""
    m = (n - 1) // 2
    return 1 + (16 * m * (m + 1) * (2 * m + 1)) // 6 + 2 * m * (m + 1) + 4 * m


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
