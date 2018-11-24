## looks like the only possible difference betwen two sequences is
## multiply of 10 (last digit of them is the same), and it should be
## more than 1000 (first digit is not the same)
from euler import is_prime
import itertools

def compute():
    for i in itertools.count(1489,2):
        if is_prime(i):
            mj = (10000-i)//2
            for j in range(1000,mj,10):
                if is_permutation(i, i+j) and is_permutation(i,i+2*j):
                    if is_prime(i+j) and is_prime(i+2*j):
                        return str(i) + str(i+j) + str(i+2*j)

def is_permutation(n,m): # are they permutation to one another
    return sorted(str(n)) == sorted(str(m))

if __name__ == "__main__":
    print(compute())