import itertools
from euler import is_prime

def compute():
    val = 9
    while is_expressible(val):
        val += 2
    return val

def is_expressible(n):
    if n%2 == 0 or is_prime(n):
        return True
    
    for i in itertools.count(1):
        x = n - 2*i*i
        if x <= 0:
            return False
        elif is_prime(x):
            return True

if __name__ == "__main__":
    print(compute())