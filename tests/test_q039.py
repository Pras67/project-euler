"""
Unit tests for Question 39: Integer Right Triangles.
"""

from solutions.q039_integer_right_triangles import count_solutions, solve


def test_q039_sample():
    # For p = 120, there are exactly 3 solutions: {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
    assert count_solutions(120) == 3


def test_q039_full():
    # The value of p <= 1000 with the maximum number of integer right triangle solutions is 840
    assert solve() == 840
