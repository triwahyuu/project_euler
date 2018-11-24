## solve the problem using Sieve of Eratosthenes
from euler import list_prime

def compute():
    return sum(list_prime(2000000))

if __name__ == "__main__":
    print(compute())