
def compute():
    [n,d] = expand_e(100)
    return sum([int(x) for x in str(n)])

def expand_e(n):
    seq = [[2,1]]
    for i in range(1, n):   # generate the sequence
        if i%3 == 2:
            seq.append([(i+1)*2//3, 1])
        else:
            seq.append([1,1])
    
    val = seq[-1]
    for i in range(n-2, -1, -1):
        d = seq[i][0]*val[0]+val[1]
        n = val[0]
        val = [d, n]
    return val

if __name__ == "__main__":
    print(compute())