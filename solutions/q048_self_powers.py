"""
Question 48: Self Powers
URL: https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Measured Runtime: ~0.015562s
"""

import time


def find_last_digits(n: int = 1000, digits: int = 10) -> int:
    """Calculates the last `digits` of the sum of i^i for i from 1 to n."""
    number = 0
    for i in range(1, n + 1):
        number = number + i ** i
    return number % (10 ** digits)


def solve(n: int = 1000, digits: int = 10) -> int:
    """Finds the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000."""
    return find_last_digits(n, digits)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
