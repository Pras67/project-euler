import time

def solve_loop(n: int = 1001) -> int:
    total_sum = 1
    for s in range(3, n + 1, 2):
        total_sum += 4 * (s * s) - 6 * (s - 1)
    return total_sum

def solve_formula(n: int = 1001) -> int:
    m = (n - 1) // 2
    return 1 + (16 * m * (m + 1) * (2 * m + 1)) // 6 + 2 * m * (m + 1) + 4 * m

if __name__ == "__main__":
    ans_loop = solve_loop(5)
    print("5x5 loop:", ans_loop)
    ans_formula = solve_formula(5)
    print("5x5 formula:", ans_formula)

    t0 = time.perf_counter()
    ans_1001_loop = solve_loop(1001)
    t1 = time.perf_counter()
    print("1001x1001 loop:", ans_1001_loop, f"Time: {t1-t0:.8f}s")

    t0 = time.perf_counter()
    ans_1001_formula = solve_formula(1001)
    t1 = time.perf_counter()
    print("1001x1001 formula:", ans_1001_formula, f"Time: {t1-t0:.8f}s")
