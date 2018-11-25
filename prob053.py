## combination(n, r): maximum value is when r = n//2;
## if 'n' is even, the value if 'r = (n/2)+1' and 'r = (n/2)+1' is the same; 
## if 'n' is odd, the value if 'r = (n//2)' and 'r = (n//2)+1' is the same
from euler import combination

def compute():
    ans = sum(num_combination(i) for i in range(23, 101))
    return ans

## returns the number of combination which has value >1M
def num_combination(n):
    res = sum(2 for i in range(2, n//2+1) if combination(n, i) > 1000000)
    if n%2 == 0 and combination(n, n//2):
        res -= 1
    return res

if __name__ == "__main__":
    print(compute())