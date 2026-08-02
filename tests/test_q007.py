"""
Unit tests for Question 7: 10001st Prime.
"""

from solutions.q007_10001st_prime import is_prime, solve


def test_q007_sample():
    # Sample from problem statement: 6th prime is 13
    assert solve(6) == 13


def test_q007_full():
    assert solve(10001) == 104743
