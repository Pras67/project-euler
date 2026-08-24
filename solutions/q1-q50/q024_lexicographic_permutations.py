"""
Question 24: Lexicographic Permutations
URL: https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Measured Runtime: ~0.000022s
"""

import math
import time


def solve(target_index: int = 1000000, digits: list[int] = None) -> str:
    if digits is None:
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Convert to 0-based index
    k = target_index - 1
    pool = digits.copy()
    result = []

    # Pick digits one by one based on block size (factorial base)
    for i in range(len(pool) - 1, -1, -1):
        block_size = math.factorial(i)
        idx = k // block_size
        result.append(str(pool.pop(idx)))
        k %= block_size

    return "".join(result)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
