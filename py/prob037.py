## the only possible number of the truncated prime in both ways is
## that it starts and ends with digits that is prime, so the maximum
## possible value less than 1M is below 780K
from .euler import is_prime, list_prime

primes = list_prime(780000)     

def compute():
    # primes < 10 not included
    ans = sum(i for i in primes[4::] if is_truncated_prime(i))
    return ans

def is_truncated_prime(n):
    n = str(n)
    trn = [n[:i:] for i in range(len(n),0,-1)]
    trn.extend(n[i+1::] for i in range(len(n)-1))
    
    res = [1 for i in trn if is_prime(int(i))]
    if len(res) == len(trn):
        return True
    else:
        return False

if __name__ == "__main__":
    print(compute())