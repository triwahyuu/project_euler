# well this is easy, just throw it all to python
from euler import factorial

def compute():
    res = str(factorial(100))
    a = [int(i) for i in res]
    return sum(a)

if __name__ == "__main__":
    print(compute())