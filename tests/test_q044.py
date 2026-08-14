"""
Unit tests for Question 44: Pentagon Numbers.
"""

from solutions.q044_pentagon_numbers import is_pentagonal, solve


def test_q044_sample():
    assert is_pentagonal(22) is True
    assert is_pentagonal(70) is True
    assert is_pentagonal(48) is False


def test_q044_full():
    assert solve() == 5482660
