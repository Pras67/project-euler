"""
Unit tests for Question 1: Multiples of 3 and 5.
"""

from solutions.q001_multiples_of_3_and_5 import solve


def test_q001_sample():
    assert solve(10) == 23


def test_q001_full():
    assert solve(1000) == 233168
