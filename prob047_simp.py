## simplified solution, using built-in memoization tools
from euler import is_prime
from functools import lru_cache # memoization tools
import itertools, time

primes = [2,3,5,7,9,11]
C = 4   # numbers of consecutive num
D = 4   # numbers of distinct factors

def compute():
    t = time.time()
    con = 0
    for i in itertools.count(4):
        if len(factors(i)) == D:
            con += 1
            if con == C:    # found
                print(time.time() - t)
                return i-C+1
        else:
            con = 0

@lru_cache(maxsize=200000)
def factors(n):
    if is_prime(n):
        primes.append(n)
        return [n]
    else:
        f = set()
        for d in primes:
            if n%d == 0:
                f.update([d] + factors(n//d))
                break
        return list(f)

if __name__ == "__main__":
    print(compute())