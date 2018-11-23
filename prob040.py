from euler import product

## maximum value needed: value >100K has 6 digits, so 100K-200K has 6*100K
## that is 600K digits. for 10K-99K, 5*89k that is 445K. So it is enough to
## just concatenating upto 200K.
def compute():
    dn = [1,10,100,1000,10000,100000,1000000]
    fr = ''.join(str(i) for i in range(200000))
    ans = product([int(fr[a]) for a in dn])
    return ans

## old solution
def compute_old():
    dn = [1,10,100,1000,10000,100000,1000000]
    i = nth = 0
    res = 1
    for n in dn:
        while n > nth:
            i += 1
            nth += len(str(i))
            if nth >= n:
                res *= int(str(i)[n-nth-1])
    return res

if __name__ == "__main__":
    print(compute())
