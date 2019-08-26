## search the median between two fraction
## two consecutive fractions, a/b and c/d, has a median m = h/k 
## m = (a+c)/(b+d)
## http://mathworld.wolfram.com/Mediant.html
## continue search between 2/5 and 3/7; stop if denominator m > 1M

def compute():
    frac = [(2,5), (3,7)]
    while True:
        m = (frac[0][0]+frac[1][0], frac[0][1]+frac[1][1])
        if m[1] > 1000000: # returns numerator
            return frac[0][0]
        frac[0] = m

if __name__ == "__main__":
    print(compute())