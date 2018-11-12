# try brute force
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
    spd = 1 # the sum
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n+1):
        if n%i == 0:
            spd += i + (n//i)
    
    if n%sqrt_n == 0: spd -= sqrt_n
    return spd

if __name__ == "__main__":
    print(compute())