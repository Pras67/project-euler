"""
Question 26: Reciprocal Cycles
URL: https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.3(3...)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6...)
1/7  = 0.142857...
1/8  = 0.125
1/9  = 0.1(1...)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

Measured Runtime: ~0.000504s
"""

import time


def get_cycle_length(d: int) -> int:
    """Finds the recurring cycle length in decimal expansion of 1/d using long division remainder tracking."""
    seen = {}
    r = 1
    position = 0
    while r != 0:
        if r in seen:
            return position - seen[r]
        seen[r] = position
        r = (r * 10) % d
        position += 1
    return 0


def solve(limit: int = 1000) -> int:
    """Returns d < limit for which 1/d has the longest recurring cycle in its decimal fraction."""
    max_length = 0
    best_d = 0
    # Search downwards because max cycle length for d is at most d - 1
    for d in range(limit - 1, 1, -1):
        if max_length >= d:
            break
        length = get_cycle_length(d)
        if length > max_length:
            max_length = length
            best_d = d
    return best_d


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
