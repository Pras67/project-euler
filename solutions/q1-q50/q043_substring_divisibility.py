"""
Question 43: Sub-string Divisibility
URL: https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

d_2 d_3 d_4 is divisible by 2
d_3 d_4 d_5 is divisible by 3
d_4 d_5 d_6 is divisible by 5
d_5 d_6 d_7 is divisible by 7
d_6 d_7 d_8 is divisible by 11
d_7 d_8 d_9 is divisible by 13
d_8 d_9 d_10 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Measured Runtime: ~0.050735s
"""

import time

PRIMES = (2, 3, 5, 7, 11, 13, 17)


def is_valid_pandigital(digits: list[int]) -> bool:
    """Checks if a 10-digit list satisfies all prime divisibility."""
    if len(digits) != 10:
        return False
    for i, prime in enumerate(PRIMES):
        value = digits[i + 1] * 100 + digits[i + 2] * 10 + digits[i + 3]
        if value % prime != 0:
            return False
    return True


def solve() -> int:
    """Finds the sum of all 0 to 9 pandigital numbers with the divisibility property."""
    total_sum = 0

    def build_number(digits: list[int], used: list[bool]) -> None:
        nonlocal total_sum

        # Check divisibility as soon as we have enough digits
        length = len(digits)
        if length >= 4:
            sub_value = digits[-3] * 100 + digits[-2] * 10 + digits[-1]
            prime = PRIMES[length - 4]
            if sub_value % prime != 0:
                return

        if length == 10:
            num = 0
            for d in digits:
                num = num * 10 + d
            total_sum += num
            return

        # Pick the next unused digit (0 to 9)
        for digit in range(10):
            if not used[digit]:
                used[digit] = True
                digits.append(digit)

                build_number(digits, used)

                digits.pop()
                used[digit] = False

    used_digits = [False] * 10
    build_number([], used_digits)

    return total_sum


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
