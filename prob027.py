from euler import list_prime
from itertools import count

def compute():
    prime = list_prime(5000)
    m = 0
    val = 0
    for a in range(1,1000):
        for b in range(1,1001):
            n1 = gen_prime_len(a,b,prime)
            n2 = gen_prime_len(-a,-b,prime)
            n3 = gen_prime_len(a,-b,prime)
            n4 = gen_prime_len(-a,b,prime)
            
            if m < n1 or m < n2:
                val = a*b
                m = max([n1,n2])
            elif m < n3 or m < n4: 
                val = -a*b
                m = max([n3,n4])
    return val

def gen_prime_len(a,b,p):
    for n in count():
        x = n*n + a*n + b
        if x not in p: 
            return n
        if x > 5000:
            raise Exception('list of prime not enough')

if __name__ == "__main__":
    print(compute())