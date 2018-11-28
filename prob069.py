## reusing code from prob047 for calculating prime factor
## https://en.wikipedia.org/wiki/Euler%27s_totient_function#Computing_Euler's_totient_function
## n/phi(n) can be reduced to just the product part
from euler import list_primality, product

isprime = list_primality(1000000)

def compute():
    ans = max([n for n in range(2,1000001)], key=n_per_totient)
    return ans

def n_per_totient(n):
    p_fact = factors(n) # prime factors of 'n'
    prod_res = product([p/(p-1) for p in p_fact])
    return prod_res

list_factor = {2:[2], 3:[3]}
seen_factor = {2,3} # used for searching
primes = [2,3,5,7,9,11]
seen_primes = {2,3,5,7,9,11}
## return distinct prime factors
## make use of memoization and recursive
def factors(n):
    if n in seen_factor:    # the factors has been found
        return list_factor[n]
    elif isprime[n]:
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
    # print(n_per_totient(9))
    print(compute())