from itertools import combinations_with_replacement
import time

FACTORIALS = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

def solve() -> int:
    curious_set = set()

    for length in range(2, 8):
        for combo in combinations_with_replacement(range(10), length):
            val = sum(FACTORIALS[d] for d in combo)
            if val >= 10:
                # Check if digits of val match the combination
                val_digits = tuple(sorted(int(ch) for ch in str(val)))
                if val_digits == combo:
                    curious_set.add(val)

    return sum(curious_set)

if __name__ == "__main__":
    t0 = time.perf_counter()
    ans = solve()
    t1 = time.perf_counter()
    print("Answer:", ans)
    print(f"Execution Time: {t1-t0:.6f}s")
