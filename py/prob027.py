## BRUTE FORCE
## it's not possible that the b < 0, because if b < 0
## the value of n = 0 will be <0 as well, which is not prime
from euler import list_prime
import itertools

prime = set(list_prime(5000)) # set is faster for search

def compute():
    ans = max(((a,b) for a in range(-999,1000) for b in range(2,1001)), key=cons_prime)
    return ans[0]*ans[1]

def cons_prime(ab):
    a,b = ab
    for n in itertools.count():
        x = n*n + a*n + b
        if x not in prime or x < 0: 
            return n

if __name__ == "__main__":
    print(compute())