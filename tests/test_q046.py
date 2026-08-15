"""
Unit tests for Question 46: Goldbach's Other Conjecture.
"""

from solutions.q046_goldbachs_other_conjecture import is_goldbach_valid, solve


def test_q046_sample():
    # Test examples given in problem description
    assert is_goldbach_valid(9) is True
    assert is_goldbach_valid(15) is True
    assert is_goldbach_valid(21) is True
    assert is_goldbach_valid(25) is True
    assert is_goldbach_valid(27) is True
    assert is_goldbach_valid(33) is True


def test_q046_full():
    assert solve() == 5777
