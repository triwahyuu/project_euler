## brute force
import itertools

def compute():
    tn = 0 # triangle number
    for i in itertools.count(1):
        tn += i
        num_div = num_factors(tn)
        if num_div > 500: 
            break
    return tn

## return number of factors of 'n'
def num_factors(n):
    sqrt_n = int(n**0.5)
    tot = sum(2 for i in range(1, sqrt_n+1) if n%i == 0)
    if n%sqrt_n == 0: 
        tot -= 1
    return tot

if __name__ == "__main__":
    print(compute())