'''
evenly divisible by two number is also called 
least common multiplier (LCM), which also have
associative properties
https://en.wikipedia.org/wiki/Least_common_multiple
'''
import euler

# using reduction by gcd method
def lcm(a,b):
    return int(a*b/euler.gcd(a,b))


# using associative properties to solve the problem
# lcm(k1,k2,...,k_n) = lcm(k1,lcm(k2,...,lcm(k_n-1,k_n)...)
res = 1
for i in range(20, 2, -1):
    res = lcm(i, res)

print(res)
