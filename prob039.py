## BRUTE FORCE

def compute():
    val = [num_of_solution(n) for n in range(1001)]
    ans = val.index(max(val))
    return ans

def num_of_solution(p):
    n_sol = 0
    for a in range(1,p+1) :
        for b in range(a,((p-a)//2)+1):
            c = p - b - a
            if a*a + b*b == c*c:
                n_sol += 1
                
    return n_sol

if __name__ == "__main__":
    print(compute())