"""
Question 35: Circular Primes
URL: https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Measured Runtime: ~0.108750s
"""

import time

# Sieve to calculate all primes up to limit (default limit is 1,000,000)
def sieve_of_eratosthenes(limit: int) -> list[bool]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime


def solve(limit: int = 1000000) -> int:
    """Calculates the number of circular primes below limit."""
    is_prime_lookup = sieve_of_eratosthenes(limit - 1)
    count = 0

    for p in range(2, limit):
        if not is_prime_lookup[p]:
            continue

        s = str(p)

        # Multi-digit circular primes cannot contain even digits or 5
        # Single digit primes are circular primes
        if len(s) > 1 and any(ch in "024568" for ch in s):
            continue

        # Check if all cyclic rotations are prime
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
        if all(is_prime_lookup[rot] for rot in rotations):
            count += 1

    return count


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
