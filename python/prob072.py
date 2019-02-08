## SOLVED, but a bit slow, any way to optimize them?
## other approach can use euler's totient function, because it counts
## how many integer that is co-prime (gcd = 1) with it self. So the total
## is just the sum of phi(2) + phi(3) + ... + phi(n)
## if 'n' is prime, phi(n) = n-1; 
## use another properties: phi(n^k) = (n^(k-1))*phi(n)
from euler import list_primality
import itertools

limit = 10**6
isprime = list_primality(limit+1)
primes = [n for n in range(2,len(isprime)) if isprime[n]]
totient_val = [0]*(limit+1)

def compute():
    ans = sum([totient(n) for n in range(2, limit+1)])
    return ans

def totient(n):
    if totient_val[n] != 0:
        return totient_val[n]
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
                    phi -= phi//p
                    if isprime[val]:
                        phi -= phi//val
                        break
        for k in itertools.count(1):
            power = n**k
            if power > limit:
                break
            totient_val[power] = (n**(k-1)) * phi
        return totient_val[n]

if __name__ == "__main__":
    print(compute())