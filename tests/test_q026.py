"""
Unit tests for Question 26: Reciprocal Cycles.
"""

from solutions.q026_reciprocal_cycles import get_cycle_length, solve


def test_q026_sample():
    # 1/7 has a 6-digit recurring cycle (0.142857...)
    assert get_cycle_length(7) == 6
    assert solve(10) == 7


def test_q026_full():
    # Value of d < 1000 with longest recurring cycle is 983
    assert solve(1000) == 983
