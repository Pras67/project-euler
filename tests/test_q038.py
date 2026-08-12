"""
Unit tests for Question 38: Pandigital Multiples.
"""

from solutions.q038_pandigital_multiples import get_concatenated_product, is_pandigital_1_to_9, solve


def test_q038_sample():
    # Example 1: 192 multiplied by (1, 2, 3) gives 192384576
    cp192 = get_concatenated_product(192)
    assert cp192 == "192384576"
    assert is_pandigital_1_to_9(cp192) is True

    # Example 2: 9 multiplied by (1, 2, 3, 4, 5) gives 918273645
    cp9 = get_concatenated_product(9)
    assert cp9 == "918273645"
    assert is_pandigital_1_to_9(cp9) is True


def test_q038_full():
    # The largest 1 to 9 pandigital 9-digit number is 932718654 (x = 9327)
    assert solve() == 932718654
