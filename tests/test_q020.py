"""
Unit tests for Question 20: Factorial Digit Sum.
"""

from solutions.q020_factorial_digit_sum import solve, solve_problem_20


def test_q020_sample():
    # 10! = 3628800, sum of digits = 27
    assert solve(10) == 27


def test_q020_full():
    # Sum of digits in 100! = 648
    assert solve(100) == 648
    assert solve_problem_20() == 648
