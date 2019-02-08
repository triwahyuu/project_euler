## create pandigital using permutation, then check if it's prime
from euler import is_prime
from itertools import permutations

def compute():
    ans = 0
    for n in range(9, 2, -1):
        pandig = ''.join(str(i) for i in range(1,n+1))
        perm = [''.join(i) for i in permutations(pandig, n)]
        perm = reversed(sorted(perm))  # sort from highest to lowest
        for val in perm:
            if int(val[-1])%2 == 1:  # just check the odd value
                if is_prime(int(val)):
                    ans = val
                    break
        if ans != 0:
            break
    return ans

if __name__ == "__main__":
    print(compute())