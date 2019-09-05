## using hardcoded memoization
from .euler import is_prime
import itertools

list_factor = {2:[2], 3:[3]}
seen_factor = {2,3} # used for searching
primes = [2,3,5,7,9,11]
seen_primes = {2,3,5,7,9,11}
C = 4   # numbers of consecutive num
D = 4   # numbers of distinct factors

def compute():
    con = 0
    for i in itertools.count(4):
        if len(factors(i)) == D:
            con += 1
            if con == C:    # found
                return i-C+1
        else:
            con = 0

## return distinct prime factors
## make use of memoization and recursive
def factors(n):
    if n in seen_factor:    # the factors has been found
        return list_factor[n]
    elif is_prime(n):
        list_factor[n] = [n]
        seen_factor.add(n)
        if n not in seen_primes: # if it's new prime
            primes.append(n)
            seen_primes.add(n)
        return [n]
    else:
        f = set()
        for d in primes:
            if n%d == 0:
                f.update([d] + factors(n//d))
                break
        list_factor[n] = list(f)
        seen_factor.add(n)
        return list(f)

if __name__ == "__main__":
    print(compute())