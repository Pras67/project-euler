"""
Question 41: Pandigital Prime
URL: https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Measured Runtime: ~0.000086s
"""

import itertools
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


def solve() -> int:
    """Finds the largest n-digit pandigital prime that exists."""
    # 9-digit and 8-digit pandigitals are divisible by 3, so max length is 7
    for perm in itertools.permutations("7654321"):
        num = int("".join(perm))
        if is_prime(num):
            return num
    return 0


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
