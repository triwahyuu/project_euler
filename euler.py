'''
this script contains some common function used
in solving project euler problems
'''

# return the product of a list
def product(lst):
    p = 1
    for a in lst: p = p*a
    
    return p

# gcd (greatest common divisor)
# using euclid's algorithm
# https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid's_algorithm
def gcd(a, b):
    if b > a: a,b = b,a # swap value

    if b == 0: return a
    else: return gcd(b, a%b)

# primality test using trial division
# https://en.wikipedia.org/wiki/Primality_test
def is_prime(n):
    if n <= 1: return False
    elif n<= 3: return True
    elif n%2 == 0 or n%3 == 0: return False
    
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0: return False
        i = i+6
    
    return True

# prime generation up to 'n'
# using Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def list_prime(n):
    st = [1]*n  # create array of one with 'n' size
    prime = []
    for i in range(2,int(n**0.5)+1):
        if st[i] == True:
            for j in range(i**2, n, i): st[j] = 0
    
    for x in range(2,n):
        if st[x] == True: prime.append(x)
    return prime


def factorial(n):
    if n < 0:
        raise ValueError('n must be positive')
    elif n == 1 or n == 0:
        return 1
    else: 
        return n*factorial(n-1)

# generate proper divisors of n 
# (numbers less than n which evenly divide n)
# using trial divisor
# mode='s' -> return sorted, mode='u' -> return unsorted
def proper_divisor(n, mode='u'):
    pd = [1]
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n+1):
        if n%i == 0:
            pd.extend([i, n//i])
    
    if n%sqrt_n == 0: pd.remove(sqrt_n)
    
    if mode == 's': pd.sort()
    elif mode == 'u': pass
    return pd