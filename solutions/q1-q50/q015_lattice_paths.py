"""
Question 15: Lattice Paths
URL: https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

Measured Runtime: ~0.000006s (Combinatorics), ~0.000045s (Dynamic Programming)
"""

import math
import time

# q 15
# lattice thing 20x20 only down and right


"""
Solution 1: Combinatorics (using math)
To cross a 20x20 grid, you must take 20 'right' moves and 20 'down' moves
(40 total moves).

The total number of paths is simply "40 choose 20" combinations:
40! / (20! * 20!)
"""


def solve_combinatorics(grid_size: int = 20) -> int:
    return math.comb(2 * grid_size, grid_size)


# Solution 2: Dynamic Programming (Grid Approach)
def solve_lattice_paths(grid_size: int = 20) -> int:
    # A 20x20 square grid has 21x21 intersection points (vertices)
    nodes = grid_size + 1
    grid = [[0] * nodes for _ in range(nodes)]

    # There is only 1 way to reach any point along the top edge or left edge
    for i in range(nodes):
        grid[i][0] = 1
        grid[0][i] = 1

    for r in range(1, nodes):
        for c in range(1, nodes):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

    return grid[grid_size][grid_size]


def solve(grid_size: int = 20) -> int:
    return solve_combinatorics(grid_size)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
