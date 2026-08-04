"""
Unit tests for Question 10: Summation of Primes.
"""

from solutions.q010_summation_of_primes import sieve_of_eratosthenes, solve


def test_q010_sample():
    # Sample from problem statement: sum of primes below 10 is 2 + 3 + 5 + 7 = 17
    assert solve(10) == 17
    assert sieve_of_eratosthenes(10) == 17


def test_q010_full():
    assert solve(2000000) == 142913828922
