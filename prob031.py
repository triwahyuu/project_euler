## using standard dynamic programming to solve sum of subset to make particular amount 

def compute():
    total = 200
    nways = [1] + [0]*total

    for coin in [1,2,5,10,20,50,100,200]:
        for n in range(coin, total+1):
            nways[n] += nways[n-coin]
    
    return nways[total]

if __name__ == "__main__":
    print(compute())