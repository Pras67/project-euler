"""
Question 19: Counting Sundays
URL: https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Measured Runtime: ~0.000101s
"""

import time

# Days in each month for a non-leap year
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def solve(start_year: int = 1901, end_year: int = 2000) -> int:
    sundays = 0
    # Jan 1, 1901 was a Tuesday (Sunday = 0, Mon = 1, Tue = 2, ...)
    current_day = 2

    for year in range(start_year, end_year + 1):
        for month in range(12):
            # Check if the 1st of the current month is a Sunday
            if current_day == 0:
                sundays += 1

            # Get days in month
            if month == 1 and is_leap(year):
                days = 29
            else:
                days = month_days[month]

            # Advance current_day to the 1st of the next month
            current_day = (current_day + days) % 7

    return sundays


if __name__ == "__main__":
    start_time = time.perf_counter()
    answer = solve()
    elapsed = time.perf_counter() - start_time

    print(f"Answer: {answer}")
    print(f"Execution Time: {elapsed:.6f} seconds")
