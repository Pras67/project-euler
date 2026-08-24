"""
Question 5: Smallest Multiple
URL: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Measured Runtime: ~0.000013s
"""

import time

# Helper function to find greatest common divisor (GCD)
# Uses euclids algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Helper function to find least common multiple (LCM)
def lcm(a, b):
    return (a * b) // gcd(a, b)


def solve(n: int = 20) -> int:
    current_lcm = 1
    for num in range(1, n + 1):
        current_lcm = lcm(num, current_lcm)
    return current_lcm


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
