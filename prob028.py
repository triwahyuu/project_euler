## using the pattern of the spiral, when creating the spiral from 1,
## the size of current square is always odd and the difference between 
## two adjacent diagonal value is current size -1

def compute():
    s = 1001   # size
    n = 1   # current size
    tot = 1
    x = 1   # the number
    while x < s*s:
        d = n-1
        while x < n*n:
            x += d
            tot += x
        n += 2
    return tot

if __name__ == "__main__":
    print(compute())