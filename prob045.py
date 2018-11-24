import itertools
last_pentanum = [165, 40755]    # [n, value]
last_hexanum = [143, 40755]

def compute():
    ans = 0
    # let's look for triangle number
    for n in itertools.count(286):
        triag = n*(n + 1)//2
        if is_hexagon(triag) and is_pentagon(triag):
            ans = triag
            break
    return ans

def is_pentagon(val):
    while last_pentanum[1] < val:
        n = last_pentanum[0] + 1
        y = n*(3*n - 1)//2
        last_pentanum[:] = [n, y]
    return val == last_pentanum[1]

def is_hexagon(val):
    while last_hexanum[1] < val:
        n = last_hexanum[0] + 1
        y = n*(2*n - 1)
        last_hexanum[:] = [n, y]
    return val == last_hexanum[1]

if __name__ == "__main__":
    print(compute())