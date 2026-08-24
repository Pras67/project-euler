"""
Question 50: Consecutive Prime Sum
URL: https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:
2 + 3 + 5 + 7 + 11 + 13 = 41

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be expressed as the sum of the most consecutive primes?

Measured Runtime: ~0.060833s
"""

import time


def solve(limit: int = 1_000_000) -> int:

    is_prime = sieve_of_eratosthenes(limit)
    primes = [i for i in range(2, limit + 1) if is_prime[i]]

    # prefix sums
    prefix_sums = [0] * (len(primes) + 1)

    for i in range(len(primes)):
        prefix_sums[i + 1] = prefix_sums[i] + primes[i]

    max_terms = 0
    max_prime = 0

    for start in range(len(primes)):
        
        for end in range(start + max_terms + 1, len(primes) + 1):
            current_sum = prefix_sums[end] - prefix_sums[start]

            if current_sum >= limit:
                break

            if is_prime[current_sum]:
                max_terms = end - start
                max_prime = current_sum

    return max_prime


def sieve_of_eratosthenes(limit: int = 1_000_000) -> list[bool]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime



if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
