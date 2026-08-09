"""
Unit tests for Question 28: Number Spiral Diagonals.
"""

from solutions.q028_number_spiral_diagonals import solve, solve_formula


def test_q028_sample():
    # 5x5 spiral diagonal sum is 101
    assert solve(5) == 101
    assert solve_formula(5) == 101


def test_q028_full():
    # 1001x1001 spiral diagonal sum is 669171001
    assert solve() == 669171001
    assert solve_formula() == 669171001
