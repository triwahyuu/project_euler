## as you can see that the top right corner of square size 'n' is 'n^2'.
## working the way down the corner counter-clockwise, the difference of
## adjacent corner is (n-1), so it can be calculated that the sum of the 4
## corner is 4*n^2 - 6*(n-1). Then it can be easily calculated with sum

def compute():
    s = 1001
    tot = 1     # initial value of the sum, special case for 1
    tot += sum((4*n*n - 6*(n-1)) for n in range(3, s+1, 2))
    return tot

if __name__ == "__main__":
    print(compute())