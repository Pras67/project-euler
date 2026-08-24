"""
Question 33: Digit Cancelling Fractions
URL: https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

Measured Runtime: ~0.000658s
"""

from math import gcd
import time


def solve() -> int:
    """Finds the denominator of the product of the four non-trivial digit-cancelling fractions in lowest terms."""
    product_num = 1
    product_den = 1

    # Search for two-digit fractions less than 1 (10 <= i < j < 100)
    for i in range(10, 100):
        for j in range(i + 1, 100):
            # Exclude trivial cases ending in zero
            if i % 10 == 0 and j % 10 == 0:
                continue

            i_str, j_str = str(i), str(j)

            # Check digit overlap: unit digit of numerator matches tens digit of denominator
            if i_str[1] == j_str[0] and j_str[1] != "0":
                new_num = int(i_str[0])
                new_den = int(j_str[1])

                # Check if fraction value is preserved (cross multiplication for exact integer comparison)
                if i * new_den == j * new_num:
                    product_num *= i
                    product_den *= j

    common_factor = gcd(product_num, product_den)
    return product_den // common_factor


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
