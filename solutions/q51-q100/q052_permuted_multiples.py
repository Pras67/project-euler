"""
Question 52: Permuted Multiples
URL: https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Measured Runtime: ~0.020815s
"""

import time


def solve() -> int:

    solution = 0
    n = 2

    while solution == 0:
        n += 1

        for i in range(10 ** (n - 1), (10 ** n) // 6):
            if sorted(str(i)) == sorted(str(2*i)) == sorted(str(3*i)) == sorted(str(4*i)) == sorted(str(5*i)) == sorted(str(6*i)):
                solution = i
                break

    return solution


if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    elapsed = time.time() - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
