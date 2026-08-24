"""
Question 16: Power Digit Sum
URL: https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Measured Runtime: ~0.006013s
"""

import time

# q 16
# sum of digits in 2 ^ 1000


def solve(power: int = 1000) -> int:
    number = 2**power
    digits_sum = sum(map(int, str(number)))
    return digits_sum


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
