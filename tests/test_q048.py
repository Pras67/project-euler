"""
Unit tests for Question 48: Self Powers.
"""

from solutions.q048_self_powers import find_last_digits, solve


def test_q048_sample():
    assert find_last_digits(10, 10) == 405071317


def test_q048_full():
    assert solve() == 9110846700
