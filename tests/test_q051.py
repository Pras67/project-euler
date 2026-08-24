"""
Unit tests for Question 51: Prime Digit Replacements.
"""

from solutions.q051_prime_digit_replacements import solve


def test_q051_small_case():
    # As described in the problem statement, 56003 is the first member of a 7-prime family
    assert solve(target_family_size=7) == 56003


def test_q051_full():
    assert solve(target_family_size=8) is not None
