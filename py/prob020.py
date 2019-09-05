## well this is easy, just throw it all to python
from .euler import factorial

def compute():
    return sum(int(i) for i in str(factorial(100)))

if __name__ == "__main__":
    print(compute())