# trying to brute force
from itertools import count

# return number of factors of 'n'
def num_factors(n):
    tot = 2 # total number of factors (1 and 'n' doesn't need to be calculated)
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n+1):
        if n%i == 0: tot += 2
    
    if n%sqrt_n == 0: tot -= 1
    return tot

# print(num_factors(400))
if __name__ == "__main__":
    n = 1
    tn = 0
    while True:
        tn += n
        num_div = num_factors(tn)
        if num_div > 500: break
        else: n += 1
    
    print(tn, n)