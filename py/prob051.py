## BRUTE FORCE, takes a bit quite a long time
## possible solution:
## loop through every prime number
## mask 1 to n digit number of them
## try replacing with 0 up to 9, and find who gets up to 8 times prime
from .euler import list_primality

## the value we are looking for is assumed to be more than 56K 
## (as in the problem states)
isprime = list_primality(1000000)

def compute():
    for n in range(56000,len(isprime)):
        for mask in range(1, (1 << len(str(n)))):
            tmp = []    # the masked value which is prime
            p = 0       # counting how many passes
            for i in range(10):
                v = mask_value(n, mask, i)
                if int(v[0]) != 0 and isprime[int(v)]:
                    tmp.append(int(v))
                else:
                    p += 1
                
                if len(tmp) == 8:
                    return sorted(tmp)[0], mask
                elif p > 2:
                    break

    raise Exception('NOT FOUND!')

## mask the value of 'n' with the binary of 'mask', replace it with 'i'
## returns string
def mask_value(n, mask, i):
    l = len(str(n))-1
    val = [(int(d)*((~mask >> (l-c)) & 1) + i*((mask >> (l-c)) & 1)) for c,d in enumerate(str(n))]
    return to_number(val)

## create number from list of digit, in string
def to_number(n):
    return ''.join(str(i) for i in n)

if __name__ == "__main__":
    print(compute())