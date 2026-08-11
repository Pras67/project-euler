"""
Unit tests for Question 37: Truncatable Primes.
"""

from solutions.q037_truncatable_primes import is_truncatable_prime, sieve_of_eratosthenes, solve


def test_q037_sample():
    # 3797 is a truncatable prime (3797, 797, 97, 7 and 3797, 379, 37, 3 are all prime)
    is_prime_lookup = sieve_of_eratosthenes(4000)
    assert is_truncatable_prime(3797, is_prime_lookup) is True


def test_q037_full():
    # Sum of the only eleven truncatable primes is 748317
    assert solve() == 748317
