import itertools
def compute():
    ans = 0
    # let's look for triangle number
    for n in itertools.count(286):
        triag = triangle(n)
        if is_hexagon(triag) and is_pentagon(triag):
            ans = triag
            break
    return ans

list_pentanum = [0]     # list is faster for iterable and indexing 
set_pentanum = set()    # set is faster for search
def is_pentagon(val):
    while list_pentanum[-1] < val:
        n = len(list_pentanum)
        y = n*(3*n - 1)//2
        list_pentanum.append(y)
        set_pentanum.add(y)
    return val in set_pentanum

list_trinum = [0]
def triangle(x):
    while len(list_trinum) <= x:
        n = len(list_trinum)
        val = n*(n + 1)//2
        list_trinum.append(val)
    return list_trinum[x]

list_hexanum = [0]
set_hexanum = set()
def is_hexagon(val):
    while list_hexanum[-1] < val:
        n = len(list_hexanum)
        y = n*(2*n - 1)
        list_hexanum.append(y)
        set_hexanum.add(y)
    return val in set_hexanum

if __name__ == "__main__":
    print(compute())