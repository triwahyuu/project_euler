'''
this script contains some common function used
in solving project euler problems
'''

# gcd (greatest common divisor)
# using euclid's algorithm
# https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid's_algorithm
def gcd(a, b):
    if b > a: a,b = b,a # swap value

    if b == 0: return a
    else: return gcd(b, a%b)

