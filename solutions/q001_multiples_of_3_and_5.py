"""
Question 1: Multiples of 3 and 5
URL: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time


def solve(limit: int = 1000) -> int:
    x = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            x += i
    return x


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
