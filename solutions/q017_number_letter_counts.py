"""
Question 17: Number Letter Counts
URL: https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Measured Runtime: ~0.000422s
"""

import time


def get_letter_count(n: int) -> int:
    # Lookup arrays for base word lengths
    ones = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if n == 1000:
        return len("onethousand")  # 11 letters

    count = 0
    hundreds = n // 100
    remainder = n % 100

    # Process Hundreds
    if hundreds > 0:
        count += len(ones[hundreds]) + len("hundred")  # e.g., "three hundred"
        if remainder > 0:
            count += len("and")  # British English requires "and"

    # Process Remainder (1–99)
    if remainder > 0:
        if remainder < 20:
            count += len(ones[remainder])
        else:
            count += len(tens[remainder // 10]) + len(ones[remainder % 10])

    return count


def solve(limit: int = 1000) -> int:
    return sum(get_letter_count(i) for i in range(1, limit + 1))


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
