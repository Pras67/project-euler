"""
Question 18: Maximum Path Sum I
URL: https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below.

Measured Runtime: ~0.000030s
"""

import copy
import time

DEFAULT_TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def solve(triangle: list[list[int]] = None) -> int:
    if triangle is None:
        triangle = DEFAULT_TRIANGLE

    # Create a deep copy to prevent mutating the original input array
    grid = [row[:] for row in triangle]

    # Start from the second-to-last row and work upwards to index 0
    for row in range(len(grid) - 2, -1, -1):
        for col in range(len(grid[row])):
            # Add the maximum of the two reachable numbers directly below
            grid[row][col] += max(grid[row + 1][col], grid[row + 1][col + 1])

    # The maximum path sum collapses into the top position
    return grid[0][0]


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
