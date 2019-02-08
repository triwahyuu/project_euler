## modified solution of prob031, substracted by 1
## as the sumation has at least 2 positive integer
def compute():
    total = 100
    nways = [1] + [0]*total

    for v in range(1, total+1):
        for n in range(v, total+1):
            nways[n] += nways[n-v]
    
    return nways[total]-1

if __name__ == "__main__":
    print(compute())