# lattice path can be easily solved with combinatorial
# http://mathworld.wolfram.com/LatticePath.html
from euler import factorial

def lattice_path(a, b): # num of latice path with size of axb
    n, k = a+b, a
    c = factorial(n)/(factorial(n-k)*factorial(k))
    return int(c)

if __name__ == "__main__":
    print(lattice_path(20,20))