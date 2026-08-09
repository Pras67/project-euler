import time

def solve(max_a: int = 100, max_b: int = 100) -> int:
    distinct_powers = {a ** b for a in range(2, max_a + 1) for b in range(2, max_b + 1)}
    return len(distinct_powers)

if __name__ == "__main__":
    print("Sample 5x5:", solve(5, 5))
    t0 = time.perf_counter()
    res = solve(100, 100)
    t1 = time.perf_counter()
    print("Full 100x100:", res, f"Time: {t1-t0:.8f}s")
