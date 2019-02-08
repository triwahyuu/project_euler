## brute force
def compute():
    n = 9
    found = None
    while True:
        # if has more digit, skip to next number of digit
        if len(str(6*n)) > len(str(n)):
            n = 10**len(str(n))
        else:
            n += 1
        for i in range(2,7):
            if not is_permutation(n, n*i):
                break
            if i == 6:
                found = n
        if found is not None:
            break
    return n

def is_permutation(n,m): # are they permutation to one another
    return sorted(str(n)) == sorted(str(m))

if __name__ == "__main__":
    print(compute())