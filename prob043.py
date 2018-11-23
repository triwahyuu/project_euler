from itertools import permutations

def compute():
    ## create all 0-to-9 pandigital
    pandigital = [''.join(i) for i in permutations('0123456789', 10)]
    ans = sum(int(n) for n in pandigital if has_property(n))
    return ans

def has_property(n): # n is string
    if int(n[3])%2 == 0: # first check if d4 is even (divisible by 2)
        divisor = [1,1,2,3,5,7,11,13,17]
        # how many values are divisible
        tot_div = sum(1 for i in range(3,9) if int(n[i-1:i+2])%divisor[i] == 0)
        if tot_div == 6:
            return True
    else: 
        return False

if __name__ == "__main__":
    print(compute())