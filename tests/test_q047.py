"""
Unit tests for Question 47: Distinct Primes Factors.
"""

from solutions.q047_distinct_primes_factors import count_distinct_prime_factors, solve


def test_q047_sample():
    assert count_distinct_prime_factors(14) == 2
    assert count_distinct_prime_factors(15) == 2
    assert solve(2, 2) == 14

    assert count_distinct_prime_factors(644) == 3
    assert count_distinct_prime_factors(645) == 3
    assert count_distinct_prime_factors(646) == 3
    assert solve(3, 3) == 644


def test_q047_full():
    assert solve() == 134043
