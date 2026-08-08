"""
Unit tests for Question 21: Amicable Numbers.
"""

from solutions.q021_amicable_numbers import solve, sum_proper_divisors


def test_q021_sample():
    # d(220) = 284 and d(284) = 220
    assert sum_proper_divisors(220) == 284
    assert sum_proper_divisors(284) == 220


def test_q021_full():
    # Sum of amicable numbers under 10000 = 31626
    assert solve(10000) == 31626
