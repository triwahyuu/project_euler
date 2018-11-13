## trying to generate it directly
## implementing dynamic programming
from euler import factorial

# the 1M-th permutation of [0,1,2,3,4,5,6,7,8,9]
def compute():
    return nth_permutation(1000000, [0,1,2,3,4,5,6,7,8,9])

## return the 'n'-th permutation of given set of number 'nums'
## assumed that 'nums' is a list of integers
def nth_permutation(n, nums):
    nums.sort()
    l = len(nums)
    n -= 1  # zero doesn't count, so the 1-st num is actually 0-th num here
    res = []
    a = factorial(l-1)    # factorial of length of number left 'l'  minus 1 -> (l-1)!

    for i in range(l-1, -1, -1):
        idx = n//a          # idx = n//(l-1)!
        n = n%a             # n = n%(l-1)!
        val = nums[idx]

        res.append(val)
        nums.remove(val)
        if i != 0: a = a//i            # next factorial
    
    res = ''.join([str(i) for i in res])
    return int(res)

if __name__ == "__main__":
    print(compute())