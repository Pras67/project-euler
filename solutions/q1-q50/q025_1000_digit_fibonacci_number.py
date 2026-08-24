"""
Question 25: 1000-digit Fibonacci Number
URL: https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms are:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Measured Runtime: ~0.000500s
"""

import time


def solve(target_digits: int = 1000) -> int:
    # Smallest number with target_digits (10^999 for 1000 digits)
    limit = 10 ** (target_digits - 1)

    a, b = 1, 1
    index = 2

    # Loop until the current term reaches target_digits length
    while b < limit:
        a, b = b, a + b
        index += 1

    return index


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
