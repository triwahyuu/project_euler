## too long, is there any more optimization?
## list prime, then calculate the value; exploit the power properties
## phi(n^k) = phi(n)*n^(k-1)
## http://mathworld.wolfram.com/TotientFunction.html
## quotient -> n/phi

from euler import list_primality
import itertools

limit = 10**7
isprime = list_primality(limit)
primes = [n for n in range(2,len(isprime)) if isprime[n]]
totient_val = [0]*(limit)

def compute():
    min_q = ans = limit
    for n in range(21, limit):
        if totient_val[n] != 0:
            phi = totient_val[n]
        else:
            if isprime[n]:
                phi = n-1
            else:
                phi = val = n
                for p in primes:
                    if p*p > n:
                        break
                    elif val%p == 0:
                        while val%p == 0:
                            val //= p
                        phi -= phi/p
                        if isprime[val]:
                            phi -= phi/val
                            break
            for k in itertools.count(1):
                power = n**k
                if power >= limit:
                    break
                totient_val[power] = (n**(k-1)) * phi
        if min_q > n/phi and is_permutation(n, int(phi)):
            min_q = n/phi
            ans = n
    return ans

def is_permutation(x,y):
    x,y = str(x), str(y)
    if len(x) != len(y):
        return False
    else:
        return sorted(x) == sorted(y)

if __name__ == "__main__":
    print(compute())