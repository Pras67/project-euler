"""
Unit tests for Question 45: Triangular, Pentagonal, and Hexagonal.
"""

from solutions.q045_triangular_pentagonal_and_hexagonal import is_pentagonal, solve


def test_q045_sample():
    # H_143 = 143 * (2 * 143 - 1) = 40755
    h_143 = 143 * (2 * 143 - 1)
    assert h_143 == 40755
    assert is_pentagonal(40755) is True


def test_q045_full():
    assert solve() == 1533776805
