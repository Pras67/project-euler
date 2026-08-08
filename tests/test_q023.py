"""
Unit tests for Question 23: Non-Abundant Sums.
"""

from solutions.q023_non_abundant_sums import solve, sum_proper_divisors


def test_q023_abundant_definition():
    # 12 is smallest abundant number: 1+2+3+4+6 = 16 > 12
    assert sum_proper_divisors(12) == 16


def test_q023_full():
    # Sum of non-abundant sums under 28123 = 4179871
    assert solve() == 4179871
