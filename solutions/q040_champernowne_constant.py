"""
Question 40: Champernowne's Constant
URL: https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the n-th digit of the fractional part, find the value of:
d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

Measured Runtime: ~0.067487s
"""

import time


def solve(target_indices: list[int] = None) -> int:
    """Calculates the product of digits at specified 1-based indices in Champernowne's constant."""
    if target_indices is None:
        target_indices = [1, 10, 100, 1000, 10000, 100000, 1000000]

    max_index = max(target_indices)
    digits = []
    current_num = 1

    while len(digits) < max_index:
        digits.extend(str(current_num))
        current_num += 1

    product = 1
    for idx in target_indices:
        product *= int(digits[idx - 1])

    return product


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
