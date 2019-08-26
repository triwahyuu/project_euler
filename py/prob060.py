## still unsolved, 
## trying to solve with recursive, but what parameter to break it?
## use nayuki's method, the with sum of them
from euler import list_primality, is_prime
import itertools

isprime = list_primality(20000)
sum_limit = 20000

def compute():
    for i in itertools.count(3, 2):
        if not isprime[i]:
            continue
        print(i)
        ans = find_concat_prime([i], 5)
        if ans is not None:
            return ans

## 'init': initial prime value to look for the pairs, in list
def find_concat_prime(init, size):
    if len(init) == size:
        return init

    diff_to_limit = sum_limit - sum(init)
    for i in itertools.count(max(init)+2, 2):
        if isprime[i]:
            if i > diff_to_limit or i >= len(isprime): # not found
                return None
            tot = sum(1 for x in init if is_concat_prime(x, i)) ## check it with everyone
            if tot == len(init):
                result = find_concat_prime(init + [i], size)
                if result is not None:
                    return result

## is the concatenated values are prime in both ways?
def is_concat_prime(a,b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

if __name__ == "__main__":
    print(compute())