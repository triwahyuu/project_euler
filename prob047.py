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

## take use of memoization
def factors(n):
    known_factor = len(list_factor)
    
    if known_factor > n:
        return list_factor[n]
    elif is_prime(n):
        list_factor.append([n])
        primes.append(n)
        return [n]
    else:
        f = set()
        for d in primes:
            if known_factor > n:
                f.update(factors(n))
                n = 1
                break
            else:
                while n%d == 0:
                    n //= d
                    f.add(d)
                if n == 1:
                    break
        if n != 1 and is_prime(n):
            primes.append(n)
            f.add(n)
        list_factor.append(list(f))
        return list(f)

if __name__ == "__main__":
    # print(factors(645))
    print(compute())