"""
Question 39: Integer Right Triangles
URL: https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral side lengths, {a,b,c},
there are exactly three solutions for p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximized?

Measured Runtime: ~0.007000s
"""

import time


def count_solutions(p: int) -> int:
    """Counts valid integer right triangles for perimeter p."""
    count = 0
    for a in range(1, p // 3 + 1):
        if (p * (p - 2 * a)) % (2 * (p - a)) == 0:
            b = (p * (p - 2 * a)) // (2 * (p - a))
            if a < b:
                count += 1
    return count


def solve(limit: int = 1000) -> int:
    """Finds the perimeter p <= limit with the maximum right triangle solutions."""
    return max(range(2, limit + 1, 2), key=count_solutions)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
