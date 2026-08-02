"""
Question 7: 10001st Prime
URL: https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

Measured Runtime: ~0.089003s
"""

import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n: int = 10001) -> int:
    primes = [2]
    candidate = 3
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 2
    return primes[-1]


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
