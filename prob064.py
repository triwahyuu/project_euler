## using continued fraction expansion
## https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

def compute():
    tot = sum(1 for n in range(2,10001) if num_period(n)%2 == 1)
    return tot

def sqrt2_expand(n):
    if (n**0.5)%1 == 0: # doesn't need to calculate if it's a square
        return int(n**0.5), []
    m, d = 0, 1         # initial value
    a = a0 = int(n**0.5)
    seen_param = {(a,d,m)}  # storing known parameter (a,d,m)
    param_value = [[a]]  # store the value of seen param
    while True:
        m = d*a - m
        d = (n - m*m) // d
        a = (a0 + m) // d
        if (a,d,m) in seen_param:
            return a0, param_value[-1][1:]
        else:
            param_value.append(param_value[-1] + [a])
            seen_param.add((a,d,m))

def num_period(n):
    a0, expanded = sqrt2_expand(n)
    return len(expanded)
    
if __name__ == "__main__":
    print(compute())
