# colatz sequence
# optimize with recursion and memoization
from functools import lru_cache

def compute():
    return max(range(1,1000000), key=colatz_len)

@lru_cache(maxsize=900000) # this size is the fastest, don't know why
def colatz_len(n):
    if n == 1: 
        return 1
    elif n%2 == 0: # if even
        y = (n // 2)
    else:
        y = (3*n + 1)
    return colatz_len(y) + 1

if __name__ == "__main__":
    print(compute())