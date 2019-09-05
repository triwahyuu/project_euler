## evenly divisible by two number is also called least common 
## multiplier (LCM), which also have associative properties
## https://en.wikipedia.org/wiki/Least_common_multiple

from .euler import gcd

## using associative properties of LCM to solve the problem
## lcm(k1,k2,...,k_n) = lcm(k1,lcm(k2,...,lcm(k_n-1,k_n)...)
def compute():
    res = 1
    for i in range(20, 2, -1):
        res = lcm(i, res)
    return res

## using reduction by gcd method
def lcm(a,b):
    return a*b//gcd(a,b)

if __name__ == "__main__":
    print(compute())