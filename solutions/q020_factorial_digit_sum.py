"""
Question 20: Factorial Digit Sum
URL: https://projecteuler.net/problem=20

n! means n * (n - 1) * ... * 3 * 2 * 1.

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Measured Runtime: ~0.000020s
"""

import math
import time


def solve(n: int = 100) -> int:
    # Calculate n! (n factorial)
    factorial_n = math.factorial(n)

    # Convert the factorial to a string and sum each digit
    digit_sum = sum(int(digit) for digit in str(factorial_n))

    return digit_sum


def solve_problem_20() -> int:
    return solve(100)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
