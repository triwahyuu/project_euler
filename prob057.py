## make use of the pattern
## 3/2; 7/5; 17/12; ...
## d[i+1] = d[i]+n[i]
## n[i+1] = 2*d[i]+n[i]

def compute():
    den = num = 1
    c = 0
    for i in range(1000):
        num, den = (2*den+num), (num+den)
        if len(str(num)) > len(str(den)):
            c+= 1
    return c

if __name__ == "__main__":
    print(compute())