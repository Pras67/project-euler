import time

primes = [2, 3, 5, 7, 11, 13, 17]

def solve():
    def search(curr_str, unused_digits):
        if len(curr_str) == 10:
            return [int(curr_str)]
        
        results = []
        for digit in unused_digits:
            next_str = curr_str + digit
            if len(next_str) >= 4:
                sub_val = int(next_str[-3:])
                prime = primes[len(next_str) - 4]
                if sub_val % prime != 0:
                    continue
            results.extend(search(next_str, unused_digits - {digit}))
        return results

    digits = set('0123456789')
    valid_numbers = search('', digits)
    return sum(valid_numbers)

start = time.perf_counter()
total = solve()
elapsed = time.perf_counter() - start
print(f"Total sum: {total}")
print(f"Elapsed: {elapsed:.6f}s")
