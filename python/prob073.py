## SOLVED, takes 7.54s, maybe it still can be optimized 
## using mediant, see prob071
## search one interval until it has denominator more than limit
import itertools

def compute():
    frac = [(1,3), (1,2)]
    limit = 12000
    for n in itertools.count():
        if n == len(frac)-1:
            break
        while True:
            m = (frac[n][0]+frac[n+1][0], frac[n][1]+frac[n+1][1])
            if m[1] <= limit:
                frac.insert(n+1, m)
            else:
                break
    return len(frac)-2

if __name__ == "__main__":
    print(compute())