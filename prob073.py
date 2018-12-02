## using mediant, see prob071
import itertools

def compute():
    frac = [(1,3), (1,2)]
    limit = 11
    while True:
        stop = more = 0
        l = len(frac)
        # print(l)
        for n in range(l - 1):
            m = (frac[n][0]+frac[n+1][0], frac[n][1]+frac[n+1][1])
            # tmp.append(m)
            if m[1] >= limit:
                more += 1
            else:
                x = 2*n+1 - more
                frac.insert(x, m)
        if more == l:
            break
        # print()
        # for i in range(len(tmp)):
        #     if tmp[i][1] <= limit:
        #         n = 2*i+1 - stop
        #         frac.insert(n, tmp[i])
        #     else:
        #         stop += 1
        # if stop == len(tmp):
        #     break
    return len(frac)-2

if __name__ == "__main__":
    print(compute())