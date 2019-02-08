## numerator 'n' and denominator 'd' has two digits, so it can be arranged as
## n = 10*n1 + n0; d = 10*d1 + d0
## as the problem stated, the value of fraction is less than one, so 10 <= n < d < 100
## considering d0 = n0, so it can be calculated:
## n1/d1 = n/d = (10*n1 + n0)/10*d1 + d0
## 10*d1*n1 + n1*d0 = 10*n1*d1 + d1*n0
## n1*d0 = d1*n0
## so n1=d1, which violate the rules, so d1=n1 or d0=n0 are not possible,
## then the problem can be simplified to just evaluating if n1=d0 or n0=d1
## but doesn't need to check when 'd0' or 'n0' is '0'
from euler import gcd

def compute():
    num_prod = 1
    den_prod = 1
    for n in range(10, 100):
        for d in range(n+1, 100):
            n1, n0 = n//10, n%10
            d1, d0 = d//10, d%10
            if (n1 == d0 and n0*d == n*d1) or (n0 == d1 and n1*d == n*d0):
                num_prod *= n
                den_prod *= d
    return den_prod//gcd(num_prod, den_prod)

if __name__ == "__main__":
    print(compute())