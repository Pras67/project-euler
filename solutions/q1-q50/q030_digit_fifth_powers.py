"""
Question 30: Digit Fifth Powers
URL: https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Measured Runtime: ~0.140766s
"""

import time


def solve(power: int = 5) -> int:
    """Finds the sum of all numbers that can be written as the sum of the power-th powers of their digits."""
    powers = [d**power for d in range(10)]

    # Upper bound calculation: 6 * 9^5 = 354,294 (since 7 * 9^5 = 413,343 < 1,000,000)
    d = 1
    while 10 ** (d - 1) <= d * powers[9]:
        d += 1
    upper_bound = (d - 1) * powers[9]

    total_sum = 0
    for n in range(10, upper_bound + 1):
        temp = n
        digit_sum = 0
        while temp > 0:
            digit_sum += powers[temp % 10]
            temp //= 10
        if digit_sum == n:
            total_sum += n

    return total_sum


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
