"""
Question 47: Distinct Primes Factors
URL: https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 x 7 x 23
645 = 3 x 43 x 5
646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

Measured Runtime: ~0.044932s
"""

import time


def count_distinct_prime_factors(n: int) -> int:
    """Returns the number of distinct prime factors of n."""
    count = 0
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count += 1
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        count += 1
    return count


def solve(target_consecutive: int = 4, target_factors: int = 4) -> int:
    """Finds the first of target_consecutive integers to have target_factors distinct prime factors each."""
    limit = 200000
    factors_count = [0] * limit

    for p in range(2, limit):
        if factors_count[p] == 0:
            for multiple in range(p, limit, p):
                factors_count[multiple] += 1

    consecutive = 0
    for i in range(2, limit):
        consecutive = (consecutive + 1) if factors_count[i] == target_factors else 0
        if consecutive == target_consecutive:
            return i - target_consecutive + 1

    return -1


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
