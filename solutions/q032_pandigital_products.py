"""
Question 32: Pandigital Products
URL: https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 39186, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Measured Runtime: ~0.092000s
"""

import time


def is_pandigital_identity(a: int, b: int, c: int) -> bool:
    """Checks if the identity a * b = c uses digits 1 through 9 exactly once."""
    s = f"{a}{b}{c}"
    return len(s) == 9 and set(s) == set("123456789")


def solve() -> int:
    """Finds the sum of all unique products whose multiplicand/multiplier/product identity is 1 through 9 pandigital."""
    products = set()

    # Case 1: 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1000, 10000):
            c = a * b
            if is_pandigital_identity(a, b, c):
                products.add(c)

    # Case 2: 2-digit * 3-digit = 4-digit
    for a in range(10, 100):
        for b in range(100, 1000):
            c = a * b
            if is_pandigital_identity(a, b, c):
                products.add(c)

    return sum(products)


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
