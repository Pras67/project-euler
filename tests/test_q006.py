"""
Unit tests for Question 6: Sum Square Difference.
"""

from solutions.q006_sum_square_difference import solve, solve_o1


def test_q006_sample():
    assert solve(10) == 2640
    assert solve_o1(10) == 2640


def test_q006_full():
    assert solve(100) == 25164150
    assert solve_o1(100) == 25164150
