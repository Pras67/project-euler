"""
Unit tests for Question 27: Quadratic Primes.
"""

from solutions.q027_quadratic_primes import sieve_of_eratosthenes, solve


def test_q027_euler_sample():
    # Euler's formula n^2 + n + 41 produces 40 primes for 0 <= n <= 39
    is_prime_lookup = sieve_of_eratosthenes(2000)
    a, b = 1, 41
    n = 0
    while is_prime_lookup[n * n + a * n + b]:
        n += 1
    assert n == 40


def test_q027_full():
    # Product of coefficients a and b maximizing consecutive primes for |a| < 1000, |b| <= 1000 is -59231
    assert solve() == -59231
