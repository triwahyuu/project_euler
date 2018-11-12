# colatz sequence
# trying to brute force

def compute():
    longest = 0
    val = 0
    for i in range(100000, 1000000):
        n = colatz(i)
        if longest < n: 
            val = i
            longest = n
    return val

def colatz(n):
    l = 1
    while n != 1:
        if n%2 == 0: n = n/2
        else: n = 3*n+1
        l += 1
    
    return l

if __name__ == "__main__":
    print(compute())