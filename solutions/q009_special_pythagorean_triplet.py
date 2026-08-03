"""
Question 9: Special Pythagorean Triplet
URL: https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Measured Runtime: ~0.019560s
"""

import time


def pythagorean_triplet_finder(target_sum: int = 1000) -> int:
    # Known that a < b < c and the total sum must be 1000.
    max_a = 334 if target_sum == 1000 else target_sum
    for a in range(1, max_a):
        for b in range(a, target_sum):
            c = target_sum - a - b

            if a**2 + b**2 == c**2:
                return a * b * c
    return 0


def solve(target_sum: int = 1000) -> int:
    return pythagorean_triplet_finder(target_sum)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
