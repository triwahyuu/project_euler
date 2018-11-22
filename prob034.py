## limiting the search: the value of 9! is 362880, which is 6 digit,
## so the maximum value of the number is 6 digits and should have 
## around 3 digit of 9 (999000). the minimun value should have 2 digits
## or maybe it is not possible if it has digit 9 in it, so try just 5 digits
from euler import factorial

## optimize with lookup table
fact = [factorial(i) for i in range(10)]

def compute():
    ans = sum(n for n in range(11, 100000) if n == sum_factorial(n))
    return ans

def sum_factorial(n):
    num = str(n)
    return sum(fact[int(a)] for a in num)

if __name__ == "__main__":
    print(compute())
