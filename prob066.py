import itertools

def compute():
    max_x = 0
    for n in range(2,1000):
        print(n)
        x = find_min_x(n)
        if x > max_x:
            max_x = x
            ans = n
    # ans = max(range(2,8), key=find_min_x)
    return ans

def find_min_x(D):
    if (D**0.5)%1 == 0: # no solution if D is perfect square
        return 0
    for x in itertools.count(2):
        x_sq = x*x
        y_sq = (x_sq - 1)/D
        if y_sq%1 != 0:
            continue
        print(x,y_sq)
        if (y_sq**0.5)%1 == 0:
            return x
    
if __name__ == "__main__":
    print(find_min_x(61))
    # print(compute())