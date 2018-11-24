
def compute():
    limit = 28123+1
    sum_div = proper_divisor(limit)
    
    # list abundant number
    abundant_num = [i for i in range(1, limit) if i < sum_div[i]]
    
    writable = [False]*(limit)
    for i in abundant_num:
        for j in abundant_num:
            if i+j < limit: 
                writable[i+j] = True
            else: 
                break
    
    # get the index of value that is true
    # enumerate returns tuple (idx, val)
    # 'idx' -> index of the value; 'val' -> the value
    nonwritable_nums = [i for (i,x) in enumerate(writable) if x == False]
    return sum(nonwritable_nums)

## generate sum of proper divisors of numbers upto 'n'
## imitating sieve of erastosthene
def proper_divisor(n):
    div_sum = [0]*(n)     # list of sum of proper divisor
    for i in range(1, n):
        for j in range(2*i, n, i):    # adding 'i' to index > '2i'
            div_sum[j] += i
    return div_sum

if __name__ == "__main__":
    print(compute())