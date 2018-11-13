## the index of the first fibonacci seq that have 1000 digits

## the ratio of two consecutive fibonacci seq is about 1,618 (y) usually called golden ratio
## to get extra digit, we need 'n'-step, which can be calculated: y^n = 10 -> n = log(y) = 0.48121
## so the first 1000-digit fibonacci seq is around index of 4812
## https://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding
def compute():
    dig = 0             # number of digit of current seq
    x,y = 0,1           # first and second seq of fibonacci
    n = 1
    while dig < 1000:
        x, y = y, x+y       # calculate next seq
        dig = len(str(y))
        n += 1
    return n

if __name__ == "__main__":
    print(compute())