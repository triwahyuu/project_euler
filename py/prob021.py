# try brute force
from .euler import proper_divisor

spd_cache = {}
def compute():
    s = 0
    for n in range(100, 10000):
        a = d(n)
        if n not in spd_cache:
            spd_cache[n] = a
        
        if a in spd_cache:
            b = spd_cache[a]
        else: 
            b = d(a)
            spd_cache[a] = b
        
        if n == b and n != a:
            s += a+b
            
    return int(s/2)

# return the sum of proper divisor
def d(n): 
    return sum(proper_divisor(n))

if __name__ == "__main__":
    print(compute())