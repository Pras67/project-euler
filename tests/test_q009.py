"""
Unit tests for Question 9: Special Pythagorean Triplet.
"""

from solutions.q009_special_pythagorean_triplet import solve


def test_q009_sample():
    # Sample case: a + b + c = 12 -> (3, 4, 5) -> 3 * 4 * 5 = 60
    assert solve(12) == 60


def test_q009_full():
    # Full case: a + b + c = 1000 -> (200, 375, 425) -> 200 * 375 * 425 = 31875000
    assert solve(1000) == 31875000
