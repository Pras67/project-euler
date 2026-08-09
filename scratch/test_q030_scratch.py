import time

def solve(power: int = 5) -> int:
    powers = [d ** power for d in range(10)]
    # Upper bound: d * 9^power where 10^(d-1) <= d * 9^power
    d = 1
    while 10**(d - 1) <= d * powers[9]:
        d += 1
    upper_bound = (d - 1) * powers[9]
    
    total_sum = 0
    matching_numbers = []
    
    for n in range(10, upper_bound + 1):
        temp = n
        s = 0
        while temp > 0:
            s += powers[temp % 10]
            temp //= 10
        if s == n:
            matching_numbers.append(n)
            total_sum += n
            
    print(f"Power {power} matching numbers:", matching_numbers)
    return total_sum

if __name__ == "__main__":
    print("Power 4 sum:", solve(4))
    
    t0 = time.perf_counter()
    res = solve(5)
    t1 = time.perf_counter()
    print("Power 5 sum:", res, f"Time: {t1-t0:.6f}s")
