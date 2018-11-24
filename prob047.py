from euler import is_prime
import itertools, time

list_factor = [[0],[1],[2],[3],[2],[5]]
primes = [2,3,5,7,9,11]
C = 4   # numbers of consecutive num
D = 4   # numbers of distinct factors

def compute():
    t = time.time()
    for i in itertools.count(6):
        con = 0
        while True:
            if len(factors(i + con)) == D:
                con += 1
            else:
                break
            
            if con == C:    # found
                print(time.time() - t)
                return i

## take use of memoization, some recursive
def factors(n):
    known_factor = len(list_factor)
    
    if known_factor > n:    # the factors has been found
        return list_factor[n]
    elif known_factor < n:  # the factors before it hasn't been found
        f = []
        while known_factor <= n:
            f = factors(known_factor)    # calculate the next factors
            known_factor = len(list_factor)
        return f
    elif is_prime(n):       
        list_factor.append([n])
        primes.append(n)
        return [n]
    else:
        f = set()
        for d in primes:
            if n%d == 0:
                n //= d
                f.add(d)
                f.update(factors(n))
                break
        list_factor.append(list(f))
        return list(f)

if __name__ == "__main__":
    print(compute())