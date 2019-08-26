## the equation is call Pell's equation
## can be solved using continued fraction, see Prob064
## with expansion value denoted as 'a',
## x[n] = a*x[n-1] + x[n-2]
## y[n] = a*y[n-1] + y[n-2]
## min 'x' found if x[n]^2 = D*y[n]^2 + 1
## initial value x = {1, a0}; y = {0, 1}
## http://mathworld.wolfram.com/PellEquation.html
import itertools

def compute():
    ans = max(range(2,1001), key=find_min_x)
    return ans

def find_min_x(n):
    if (n**0.5)%1 == 0: # no solution if D is perfect square
        return 0
    m, d = 0, 1         # initial value
    a = a0 = int(n**0.5)
    x = [1, a0]
    y = [0, 1]
    while True:
        m = d*a - m
        d = (n - m*m) // d
        a = (a0 + m) // d

        x.append(a*x[-1] + x[-2])
        y.append(a*y[-1] + y[-2])
        del x[0], y[0]
        if x[-1]*x[-1] == (y[-1]*y[-1]*n + 1):
            return x[-1]
            
if __name__ == "__main__":
    print(compute())