## bottom right most diagonal of current side 'n' is n^2
## and the diagonal before it is n^2-k*(n-1); k=0,1,2,3
from euler import is_prime
import itertools

def compute():
    np = 0  # number of primes
    nd = 1  # number of diagonal
    for n in itertools.count(3, 2):
        nd += 4
        for k in range(4):
            x = n*n - k*(n-1)
            if is_prime(x):
                np += 1
        r = np/nd
        if r < 0.1:
            return n

if __name__ == "__main__":
    print(compute())