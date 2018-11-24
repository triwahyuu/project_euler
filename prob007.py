from euler import is_prime
import itertools

def compute():
    idx = 1     # doesn't need to check for 2
    for n in itertools.count(3, 2): # just check the even number
        if is_prime(n):
            idx += 1
            if idx == 10001:
                break
    return n

if __name__ == "__main__":
    print(compute())
