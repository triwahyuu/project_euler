import itertools

def compute():
    s = 0
    for n in itertools.count(1):
        c = count_value(n)
        s += c
        if c == 0:
            break
    return s

## returns how many 'n' digit values that is the power of 'n'
def count_value(n):
    c = 0
    for i in itertools.count(1):
        v = i**n
        if len(str(v)) == n:
            c += 1
        elif len(str(v)) > n:
            break
    return c

if __name__ == "__main__":
    print(compute())