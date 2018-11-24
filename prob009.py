## trying to brute force
def compute():
    TOT = 1000
    for a in range(3, TOT):
        for b in range(a+1, TOT):
            c = TOT - b - a
            if c < 0:
                break
            if a*a + b*b == c*c:
                return a*b*c

if __name__ == "__main__":
    print(compute())