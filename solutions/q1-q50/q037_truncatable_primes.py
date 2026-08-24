"""
Question 37: Truncatable Primes
URL: https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible to
continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7.

Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Measured Runtime: ~0.075000s
"""

import time


def sieve_of_eratosthenes(limit: int) -> list[bool]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime


def is_truncatable_prime(n: int, is_prime_lookup: list[bool]) -> bool:
    """Checks if n is truncatable from left-to-right and right-to-left."""
    s = str(n)
    length = len(s)

    # Check left-to-right truncations (e.g. 3797 -> 797 -> 97 -> 7)
    for i in range(1, length):
        if not is_prime_lookup[int(s[i:])]:
            return False

    # Check right-to-left truncations (e.g. 3797 -> 379 -> 37 -> 3)
    for i in range(1, length):
        if not is_prime_lookup[int(s[:i])]:
            return False

    return True


def solve(target_count: int = 11) -> int:
    """Finds the sum of the only 11 truncatable primes."""
    limit = 1000000
    is_prime_lookup = sieve_of_eratosthenes(limit)

    truncatable_primes = []
    # Single digit primes (2, 3, 5, 7) are excluded, so we start from 11
    for p in range(11, limit, 2):
        if is_prime_lookup[p] and is_truncatable_prime(p, is_prime_lookup):
            truncatable_primes.append(p)
            if len(truncatable_primes) == target_count:
                break

    return sum(truncatable_primes)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
