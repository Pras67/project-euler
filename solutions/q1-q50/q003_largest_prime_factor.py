"""
Question 3: Largest Prime Factor
URL: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Measured Runtime: ~0.000073s
"""

import math
import time


def solve(n: int = 600851475143) -> int:
    largest_pf = 1

    while n % 2 == 0:
        largest_pf = 2
        n //= 2

    a = 3
    while a <= math.isqrt(n):
        while n % a == 0:
            largest_pf = a
            n //= a
        a += 2

    if n > 1:
        largest_pf = n

    return largest_pf


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
