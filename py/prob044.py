import itertools

def compute():
    min_diff = None

    # let's look for pentagon number each n, counting up
    for n in itertools.count(2):
        # stop the search if the new pentagon number difference is bigger then the one found
        if min_diff is not None and (pentagon(n) - pentagon(n-1)) >= min_diff:
            break
        # let's for the difference, counting down
        for m in range(n-1, 0, -1):
            diff = pentagon(n) - pentagon(m)
            s = pentagon(n) + pentagon(m)
            if min_diff is not None and diff >= min_diff:
                break
            elif is_pentagon(s) and is_pentagon(diff):
                if min_diff is None or min_diff > diff:
                    min_diff = diff

    return min_diff

list_pentanum = [0]     # list is faster for iterable and indexing 
set_pentanum = set()    # set is faster for search
def pentagon(x):
    while len(list_pentanum) <= x:
        n = len(list_pentanum)
        val = n*(3*n - 1)//2
        list_pentanum.append(val)
        set_pentanum.add(val)
    return list_pentanum[x]

def is_pentagon(val):
    while list_pentanum[-1] < val:
        n = len(list_pentanum)
        y = n*(3*n - 1)//2
        list_pentanum.append(y)
        set_pentanum.add(y)
    return val in set_pentanum

if __name__ == "__main__":
    print(compute())