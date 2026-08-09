"""
Question 27: Quadratic Primes
URL: https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 is divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
for consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601,
is -126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n = 0.

Measured Runtime: ~0.040829s
"""

import time


def sieve_of_eratosthenes(limit: int) -> list[bool]:
    """Generate a boolean lookup array where index i is True if i is prime."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime


def solve(max_abs_a: int = 999, max_abs_b: int = 1000) -> int:
    """Finds product of a and b (|a| <= max_abs_a, |b| <= max_abs_b) maximizing consecutive primes."""
    # Sieve up to 200,000 to cover all quadratic value evaluations
    sieve_limit = 200000
    is_prime_lookup = sieve_of_eratosthenes(sieve_limit)

    # b must be a prime number (since for n = 0, n^2 + a*n + b = b must be prime)
    b_candidates = [b for b in range(2, max_abs_b + 1) if is_prime_lookup[b]]

    max_n = 0
    best_product = 0

    for b in b_candidates:
        for a in range(-max_abs_a, max_abs_a + 1):
            # For b > 2, 1 + a + b is prime requires a to be odd
            if b > 2 and a % 2 == 0:
                continue

            # Early pruning check:
            # If (max_n)^2 + a*(max_n) + b is not prime, this (a, b) cannot beat max_n
            test_val = max_n * max_n + a * max_n + b
            if test_val <= 1 or test_val > sieve_limit or not is_prime_lookup[test_val]:
                continue

            # Count consecutive primes starting from n = 0
            n = 0
            while True:
                val = n * n + a * n + b
                if val <= 1 or val > sieve_limit or not is_prime_lookup[val]:
                    break
                n += 1

            if n > max_n:
                max_n = n
                best_product = a * b

    return best_product


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
