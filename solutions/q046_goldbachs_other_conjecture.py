"""
Question 46: Goldbach's Other Conjecture
URL: https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Measured Runtime: ~0.001s
"""

import time


def is_prime(n: int) -> bool:
    """Checks if n is a prime number."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, int(n**0.5) + 1, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True


def is_goldbach_valid(n: int) -> bool:
    """Checks if an odd number n can be written as prime + 2 * k^2 for k >= 1."""
    limit = int((n // 2) ** 0.5)
    return any(is_prime(n - 2 * k * k) for k in range(1, limit + 1))


def solve() -> int:
    """Finds the smallest odd composite number that violates Goldbach's conjecture."""
    n = 9
    while True:
        if not is_prime(n) and not is_goldbach_valid(n):
            return n
        n += 2


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
