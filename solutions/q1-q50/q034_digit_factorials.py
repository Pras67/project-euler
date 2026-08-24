"""
Question 34: Digit Factorials
URL: https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Measured Runtime: ~0.045000s
"""

from itertools import combinations_with_replacement

FACTORIALS = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)


def solve() -> int:
    """Finds the sum of all numbers equal to the sum of the factorial of their digits.

    Optimized using combinations with replacement: digit multiset determines digit factorial sum.
    Upper bound is 7 * 9! = 2,540,160 (7 digits max).
    """
    curious_set = set()

    for length in range(2, 8):
        for combo in combinations_with_replacement(range(10), length):
            val = sum(FACTORIALS[d] for d in combo)
            if val >= 10:
                val_digits = tuple(sorted(int(ch) for ch in str(val)))
                if val_digits == combo:
                    curious_set.add(val)

    return sum(curious_set)


if __name__ == "__main__":
    import time

    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
